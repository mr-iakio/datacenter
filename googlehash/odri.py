from typing import Dict, List, Any


class Photo:
    def __init__(self, orient, tags):
        self.orient = orient
        self.tags = tags

class Individual:
    def __init__(self, assignlist):
        self.assignlist = assignlist[:]

        # slidelist es una lista de slides
        # cada slide a su vez es una lista de photos_index
        # e.g. [ [photo1] [photo2 photo3] [photo234]]
        self.slidelist = self.computeslidelist()

    def fit(self, problem):

        maxphotosinslide = max([len(slide) for slide in self.slidelist])
        if maxphotosinslide > 2:
            return -1

        for slide in self.slidelist:
            if len(slide) ==2:
                if problem[slide[0]].orient == "H" or problem[slide[1]].orient == "H":
                    return -1
            if len(slide) == 2:
                if problem[slide[0]].orient == "V":
                    return -1

        if len(self.slidelist)<=1:
            return 0
        else:
            interests = [self.interest(i, i+1, problem) for i in list(range(len(self.slidelist)-1))]
            return sum(interests)


    def __str__(self):
        return "PASS"


    def gen_output(self, outf):
        with open(outf, "w") as f:
            f.write("%d" % len(self.slidelist))
            for slide in self.slidelist:
                f.write("\n")
                for photo_index in slide:
                    f.write("%d " % photo_index)


    def computeslidelist(self):
        slidelist: Dict[Any, List[Any]] = {}
        for i_photo in range(len(self.assignlist)):
            i_slide = self.assignlist[i_photo]
            if i_slide is None:
                pass
            else:
                if i_slide in slidelist:
                    slidelist[i_slide].append(i_photo)
                else:
                    slidelist[i_slide] = [i_photo]

        sorted_keys = sorted(slidelist.keys())
        return [slidelist[key] for key in sorted_keys]


    def interest(self, idx1, idx2, problem):
        tagsslide1_list = [problem[idx].tags for idx in self.slidelist[idx1]]
        tagsslide2_list = [problem[idx].tags for idx in self.slidelist[idx2]]
        tagsslide1 = set(flatten(tagsslide1_list))
        tagsslide2 = set(flatten(tagsslide2_list))

        tags_common = tagsslide1.intersection(tagsslide2)
        tags_only1 = set(tagsslide1 - tagsslide2)
        tags_only2 = set(tagsslide2 - tagsslide1)

        return min(len(tags_common), len(tags_only1), len(tags_only2))


def flatten(lst):
    res = []
    for x in lst:
        res = res +x

    return res
