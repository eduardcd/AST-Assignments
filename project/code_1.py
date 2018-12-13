class Data:
    def __init__(self, sensors):
        self.d = {}
        for i in sensors:
            for j in i:
                if j[1] not in self.d:
                    self.d[j[1]] = []
                self.d[j[1]].append(j)
                
    def calculate(self):
        return sorted([max(self.d[i], key=lambda item:item[2]) for i in self.d])
