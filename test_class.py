from Project import Data


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


# def test_calculate():
#     rgbd = [('Knife', 1, .97), ('Pen', 3, .82), ('Cat', 6, .31)]
#     rgb = [('Knife', 1, .73), ('Pen', 3, .92), ('Cat', 6, .11)]
#     data = Data(rgbd, rgb)
#     assert data.calculate() == [('Knife', 1, 0.97), ('Pen', 1, 0.92), ('Cat', 6, 0.31)]
#
#
# def test_calculate():
#     rgbd = [ ('Pen', 3, .82), ('Knife', 1, .97), ('Cat', 6, .31)]
#     rgb = [('Knife', 1, .73), ('Pen', 3, .92), ('Cat', 6, .11)]
#     data = Data(rgbd, rgb)
#     assert data.calculate() == [('Knife', 1, 0.97), ('Pen', 1, 0.92), ('Cat', 6, 0.31)]
#
# def test_calculate2():
#     rgbd = [('Knife', 1, .97), ('Pen', 3, .82), ('Cat', 6, .31)]
#     rgb = [('Knife', 1, .73), ('Pen', 3, -.01), ('Cat', 6, .11)]
#     data2 = Data(rgbd, rgb)
#     assert data2.calculate() == [('Knife', 1, 0.97), ('Pen', 1, 0.92), ('Cat', 6, 0.31)]
#
# def test_calculate3():
#     rgbd = [('Knife', 1, .97), ('Pen', 3, .82), ('Cat', 6, .31)]
#     rgb = [('Pen', 1, .73), ('Knife', 3, .92), ('Cat', 6, .11)]
#     data3 = Data(rgbd, rgb)
#     assert data3.calculate() == [('Knife', 1, 0.97), ('Pen', 1, 0.92), ('Cat', 6, 0.31)]

# import pytest
# def f():
#     raise SystemExit(1)
#
# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()

#Test case #1
# Hi Vahid I have found some problems that I think we should take in consideration
# When you change the order of the inputs the code doesn't deliver the expected result
# for example
# rgbd = [ ('Pen', 3, .82), ('Knife', 1, .97), ('Cat', 6, .31)]
# rgb = [('Knife', 1, .73), ('Pen', 3, .92), ('Cat', 6, .11)]
# The result is
# E         - [('Pen', 3, 0.82), ('Knife', 1, 0.97), ('Cat', 6, 0.31)]
# When should be
# E         + [('Knife', 1, 0.97), ('Pen', 1, 0.92), ('Cat', 6, 0.31)]

#Test case #2
# Also if for some reason one of the inputs are not available the code throw an error saying that the tuple is not complete
# E   IndexError: tuple index out of range

#Test case #3
# I have changed the name of two of the tuples and for being sincere I do not understand the error
# We should check it tomorrow .
# Result
# _______________________________ test_calculate3 ________________________________
#
#     def test_calculate3():
#         rgbd = [('Knife', 1, .97), ('Pen', 3, .82), ('Cat', 6, .31)]
#         rgb = [('Pen', 1, .73), ('Knife', 3, .92), ('Cat', 6, .11)]
#         data3 = Data(rgbd, rgb)
# >       assert data3.calculate() == [('Knife', 1, 0.97), ('Pen', 1, 0.92), ('Cat', 6, 0.31)]
# E       assert [('Knife', 1,...at', 6, 0.31)] == [('Knife', 1, ...at', 6, 0.31)]
# E         At index 1 diff: ('Pen', 3, 0.92) != ('Pen', 1, 0.92)
# E         Full diff:
# E         - [('Knife', 1, 0.97), ('Pen', 3, 0.92), ('Cat', 6, 0.31)]
# E         ?                              ^
# E         + [('Knife', 1, 0.97), ('Pen', 1, 0.92), ('Cat', 6, 0.31)]
# E         ?                              ^
#
# test_class.py:28: AssertionError
# ----------------------------- Captured stdout call -----------------------------
# ['Knife', 'Pen', 'Cat']
# [1, 3, 6]
# [0.97, 0.82, 0.31]
# [0.73, 0.92, 0.11]
