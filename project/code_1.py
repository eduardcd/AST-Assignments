def takeSecond(elem):
    return elem[1]

class Data:
    def __init__(self, rgbd, rgb):
        if len(rgbd) != 0 and len(rgb) != 0:
            if len(rgbd) != len(rgb):
                raise ValueError('Invalid Data')
            for i in range(len(rgbd)):
                if len(rgbd[i]) != len(rgb[i]):
                    raise ValueError('Invalid Data')
            self._names = [i[0] for i in sorted(rgbd, key=lambda x: x[0])]
            self._ids = [i[1] for i in sorted(rgbd, key=lambda x: x[0])]
            self._rgbd = [i[2] for i in sorted(rgbd, key=lambda x: x[0])]
            self._rgb = [i[2] for i in sorted(rgb, key=lambda x: x[0])]
        else:
            self._rgbd = sorted(rgbd)
            self._rgb = sorted(rgb)
        
    def calculate(self):
        if len(self._rgbd) == 0 and len(self._rgb) == 0:
            return []
        if len(self._rgbd) == 0:
            return self._rgb
        if len(self._rgb) == 0:
            return self._rgbd
        lista = []
        for i in range(len(self._names)):
            value = (self._names[i], self._ids[i], max(self._rgbd[i], self._rgb[i]))
            lista.append(value)
            lista.sort(key=takeSecond, reverse = False)
        return lista
