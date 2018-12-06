class Data:
    def __init__(self, rgbd, rgb):
        d = {}
        for i in rgbd + rgb:
            if i[1] in d:
                d[i[1]].append(i)
            else:
                d[i[1]] = [i]
        self.d = d

    def calculate(self):
        return sorted([max(self.d[i], key=lambda item:item[2]) for i in self.d])
