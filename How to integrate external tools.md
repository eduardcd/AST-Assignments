## Linking Travis with this repository
One of the characteristics of travis is to run a test every time a new commit is being made into the master (or other branch if specified)

1. Enter to travis webpage  [travis-ci.com](https://travis-ci.com/).
2. In the upper right corner click on your name (or choose Accounts) to open your Travis-ci profile.
3. Select a repository to be tested continously
4. Create a .yml file that should contain information about how to execute the test this file should be located in the root of your project
```
branches:
  only:
  - master
  - stable

language: python
python: 
  - "2.7"
  - "3.4" 
# command to install dependencies
install:
  - pip install pytest
  - pip install codecov
# command to run tests
script:
- pytest
after_success:
- bash <(curl -s https://codecov.io/bash)
```

It's possible to add the badge of the status of you r code directly on your readme file
just add the following line of code which is just the link to your travis account
```
## Status
[![Build Status](https://travis-ci.org/eduardcd/AST-Assignments.png?branch=master)](https://travis-ci.org/eduardcd/AST-Assignments)
```

#Somehting is not working properly when try too link this repository to codecov webpage so no further instructions were added #
