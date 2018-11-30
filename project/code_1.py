class Data:
    def __init__(self, rgbd, rgb):
        if len(rgbd) != len(rgb):
            raise ValueError('Invalid Data')
        for i in range(len(rgbd)):
            if len(rgbd[i]) != len(rgb[i]):
                raise ValueError('Invalid Data')
        self._names = [i[0] for i in sorted(rgbd, key=lambda x: x[0])]
        self._ids = [i[1] for i in sorted(rgbd, key=lambda x: x[0])]
        self._rgbd = [i[2] for i in sorted(rgbd, key=lambda x: x[0])]
        self._rgb = [i[2] for i in sorted(rgb, key=lambda x: x[0])]
        
    def calculate(self):
        return [(self._names[i], self._ids[i], max(self._rgbd[i], self._rgb[i])) for i in range(len(self._names))]
