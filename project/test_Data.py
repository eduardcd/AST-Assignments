from code_1 import Data

def test_calculate():
    rgbd = [ ('knife', 1, .99), ('scissor',2, .65), ('fork',3, .33), ('spoon',4, .80), ('keys',5, .95)]
    rgb = [('knife', 1, .55), ('scissor', 2, .95), ('fork', 3, .99), ('spoon',4, .99), ('keys',5, .95)]
    data = Data(rgbd, rgb)
    assert data.calculate() == [('knife', 1, .99), ('scissor',2, .95), ('fork',3, .99), ('spoon',4, .99), ('keys',5, .95)]

def test_calculate2():
    rgbd = [ ('knife', 1, .99), ('scissor',2, .65), ('fork',3, .33), ('spoon',4, .80), ('keys',5, .95)]
    rgb = [('knife', 1, .55), ('fork', 3, .99), ('scissor', 2, .95), ('spoon',4, .99), ('keys',5, .95)]
    data2 = Data(rgbd, rgb)
    assert data2.calculate() == [('knife', 1, .99), ('scissor',2, .95), ('fork',3, .99), ('spoon',4, .99), ('keys',5, .95)]
