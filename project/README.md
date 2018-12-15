# Project Object list merger

This project was originally created to merge the input lists that are delivered by 2 different algorithms that perceive objects. Those lists are an array of tuples that contain the following information (name_object,id_object,percentage_certainty). The algorithm presented should be able of get the tuple with the highest perrcentage of certainty, also should be able of handle complex situations. Some of them are defined on the test cases.

The code is also able to recieve the data from more sensors (there is no any limitation). But there is an important point here; the code expect to recieve correct data from sensors. Each sensor should provide data with object_name, objecti_d, and percentage_certainty. Otherwise it would raise an exception, and inform the user that the data is incorrect. We used this logic here because the task of this module is not data correction. It should have done before this module starts to work.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them
In order to be able of execute the tests pytest should be installed on your computer. 
The following command can be used from terminal in order to do so.

```
sudo apt install python-pytest
```

### Installing

A step by step series of examples that tell you how to get a development env running

Firstly from terminal run the above command to install the proper software, this will allow you to execute tests
This should trough a confirmation statement or like my case say that you have already installed the latest version.

![Install Pytest](https://drive.google.com/open?id=1pvsQqOLITP6mSviVgaumesNFUQKrJoyg)

```
eduardo@eduardo-AERO-15XV8:~$ sudo apt install python-pytest
[sudo] password for eduardo: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
python-pytest is already the newest version (2.8.7-4).
The following packages were automatically installed and are no longer required:
  linux-euclid-tools-4.4.0-9028 linux-headers-4.15.0-38
  linux-headers-4.15.0-38-generic linux-headers-4.4.0-139
  linux-headers-4.4.0-139-generic linux-image-4.15.0-38-generic
  linux-image-4.4.0-139-generic linux-image-extra-4.4.0-139-generic
  linux-modules-4.15.0-38-generic linux-modules-extra-4.15.0-38-generic
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 40 not upgraded.
```
Now you will be able of run the test cases



## Running the tests

Explain how to run the automated tests for this system
Secondly, you should chage the path to your folder where the repository was cloned (in my case) 

![Git Folder Test](https://drive.google.com/open?id=1tK7JhUPTPHhvXHqgDhMe-ZJ_wpy9K9PV)

```
 eduardo@eduardo-AERO-15XV8:~/Documents/AST/Project/project$
```

After that you should send the command that allow to execute all the test located inside that folder

![Git Command Execute Test](https://drive.google.com/open?id=1dREvmuJh5iu5HUjntkaMOkb6qNdR5S65)

```
 eduardo@eduardo-AERO-15XV8:~/Documents/AST/Project/project$ PYTHONPATH=. py.test -v
```

This will execute the test cases found which always shall named with the "test_" string if one of the files is not an executable the test will be skipped.

![Test Cases Executed](https://drive.google.com/open?id=195hgjktZBj95MzB60jupotjF0PzdUvQB)

```
eduardo@eduardo-AERO-15XV8:~/Documents/AST/Project/project$ PYTHONPATH=. py.test -v
================================ test session starts =================================
platform linux2 -- Python 2.7.12, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /usr/bin/python
cachedir: .cache
rootdir: /home/eduardo/Documents/AST/Project/project, inifile: 
collected 9 items 

test_Data.py::test_calculate PASSED
test_Data.py::test_calculate2 PASSED
test_Data_update_1.py::test_calculate1 PASSED
test_Data_update_1.py::test_calculate2 PASSED
test_Data_update_1.py::test_calculate3 PASSED
test_Data_update_1.py::test_calculate4 PASSED
test_Data_update_1.py::test_calculate5 PASSED
test_Data_update_1.py::test_calculate6 PASSED
Test Results/test_update_1 passing.txt SKIPPED

======================== 8 passed, 1 skipped in 0.04 seconds =========================
```


### Break down into end to end tests

Those test where defined to attempt executing complex situations for merging the lists

In this case given 2 lists of tuples containign the necessary information the implementation should be able of return the object with the higest probability of certain

```
rgbd = [('knife',1, .94),('knife',1, .69),('knife',1, .89)]
rgb =  [('knife',1, .99),('fork', 3, .99)]

Expected output = [('knife', 1, .99), ('fork',3, .99)]
```

## Deployment

Clone the project to your local repository, we recommend to do some refactoring in order to implement it on to your project

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Vahid MohammadiGahrooei** - *Initial work* 
  **Eduardo Cervantes Dueñas** - *Initial work*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks for the authors of the image recognition algorithms.
* Deebul for being part of this

something


## Apendix Previous Version
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

## badges

![alt text](https://img.shields.io/badge/codecov-95%25-green.svg)
![alt text](https://img.shields.io/badge/Test%20Report-master-blue.svg)
