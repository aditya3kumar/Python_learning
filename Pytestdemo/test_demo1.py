#Any pytest file always start with test_ or it can end with test_ ,this is mandatory to alert machine this is pytest file
# method or function name always start with test
#Any method must have test name
# If yoy have methods with same name ,it will not throw error it just overrides the old with new method
#Method name must have sense
#-k stands for method name execution,-s logs in output,-v stands for more metadata
#You can run specific file by py.test filename
#you can mark (tag)tests @pytest.mark.smoke and then run with -m
#You can skip test with mark @pytest.mark.skip -its predefined in pytest.
# You can pass the test but not want to show in report @pytest.mark.xfail
# You have to use fixture in conftest file only when same fixture will be used for many files
#fixtures are used to rum some code before test method
#data driven and paramterization can be done with return params in tuple format
#when you define fixture scope as class only, it run once before class initiated and class method executes

import pytest


@pytest.mark.smoke
@pytest.mark.skip
def  test_firstprogram():
    print("Pytest framework start")

@pytest.mark.xfail # for pass the test but not want to show in report
def  test_creditcard_demo1():
    print("Credit card statement")

