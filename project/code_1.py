class Data:
    def __init__(self, rgbd, rgb):
        self._names = [i[0] for i in rgbd]
        self._ids = [i[1] for i in rgbd]
        self._rgbd = [i[2] for i in rgbd]
        self._rgb = [i[2] for i in rgb]
        print(self._names)
        print(self._ids)
        print(self._rgbd)
        print(self._rgb)

    def calculate(self):
        return [(self._names[i], self._ids[i], max(self._rgbd[i], self._rgb[i])) for i in range(len(self._names))]

# rgbd = [('Knife', 1, .97), ('Pen', 3, .82), ('Cat', 6, .31)]
# rgb = [('Knife', 1, .73), ('Pen', 3, .92), ('Cat', 6, .11)]
# data = Data(rgbd, rgb)
# print(data.calculate())
