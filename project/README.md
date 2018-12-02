1. Select language of working 
Python

2. Select the coding standard 
PEP-8

3. Select testing framework 
For execute the test cases Pytest will be used which one of his main advantages respect to unittest is that the test cases are easy to code, deriving on quicker developments.

4. Select the data structure you will use to communicate the object list to your code 
Based on the input parameters given by the 2 different methods:
A list of tuples containing (“Name of the object”,id_object,percentage of certainty) will be used. And then passed to a class that will process all data

5. Design the code structure along with the class/function type and define the class/function names 
	Class Data (first_list_of_tuples, second_list_of_tuples):
		method
		calculate()
	
6. Decide on the input and output formats of data 
The inputs taken in consideration will be a list of tuples containing the 3 types of data (“Name of the object”,id_object,percentage of certainty).

The output will be a list of tuples with the same data but selecting the one with the highest percentage of certainty 

7. Write test cases for the input and expected output 
The test cases are already pushed into github

8. Make the test cases work and fail for expected outputs don’t match 
The first test case is passing the other has a little swap into the input parameters the output should be the same.
	Test Failing.txt

9. Write the actual implementation 
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

10. Now pass the test cases 
Test Passing.txt
