from code_1 import Data
from unittest import TestCase
def test_calculate1():
    rgbd = [('knife',1, .99), ('scissor', 2, .65), ('spoon', 3, .33), ('spoon', 4, .80), ('keys', 5, .95)]
    rgb =  [('keys', 5, .95), ('spoon', 4, .99),('fork', 3, .99), ('scissor', 2, .95), ('knife',1, .55)]
    data = Data([rgbd, rgb])
    assert sorted(data.calculate())==sorted([('knife', 1, .99), ('scissor',2, .95), ('fork',3, .99), ('spoon',4, .99), ('keys',5, .95)])

def test_calculate2():
    rgbd = []
    rgb = []
    data2 = Data([rgbd, rgb])
    assert sorted(data2.calculate()) == sorted([])

def test_calculate3():
    rgbd = [('knife',1, .99), ('scissor', 2, .65), ('spoon', 3, .33)]
    rgb =  []
    data3 = Data([rgbd, rgb])
    assert sorted(data3.calculate()) == sorted([('knife',1, .99), ('scissor', 2, .65), ('spoon', 3, .33)])

def test_calculate4():
    rgbd = [('knife',1, .99), ('scissor', 2, .65), ('spoon', 3, .33)]
    rgb =  [('KNIFE',1, .99), ('SCISSOR', 2, .65), ('SPOON', 3, .33)]
    data4 = Data([rgbd, rgb])
    assert sorted(data4.calculate()) == sorted([('knife',1, .99), ('scissor', 2, .65), ('spoon', 3, .33)])

def test_calculate5():
    rgbd = [('knife',1, .99), ('scissor', 2, .65)]
    rgb =  [('fork', 3, .99), ('spoon', 4, .99)]
    data5 = Data([rgbd, rgb])
    assert sorted(data5.calculate()) == sorted([('knife', 1, .99), ('scissor',2, .65), ('fork',3, .99), ('spoon',4, .99)])

def test_calculate6():
    rgbd = [('knife',1, .94),('knife',1, .69),('knife',1, .89)]
    rgb =  [('knife',1, .99),('fork', 3, .99)]
    data6 = Data([rgbd, rgb])
    assert sorted(data6.calculate()) == sorted([('knife', 1, .99), ('fork',3, .99)])

def test_calculate7():
    rgbd = [('knife',1, .97), ('scissor', 2, .65), ('spoon', 3, .33), ('spoon', 4, .80), ('keys', 5, .95)]
    rgb =  [('keys', 5, .95), ('spoon', 4, .99),('fork', 3, .99), ('scissor', 2, .95), ('knife',1, .55)]
    camera_3d =  [('keys', 5, .95), ('spoon', 4, .97),('fork', 3, .15), ('scissor', 2, .98), ('knife',1, .55)]
    extra_rgb = [('keys', 5, .99), ('spoon', 4, .98),('fork', 3, .02), ('scissor', 2, .956), ('knife',1, .99)]
    data = Data([rgbd, rgb, camera_3d, extra_rgb])
    assert sorted(data.calculate())==sorted([('knife', 1, .99), ('scissor',2, .98), ('fork',3, .99), ('spoon',4, .99), ('keys',5, .99)])
