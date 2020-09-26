import pytest
#How to pass data to your test fixture from conftest file
from Pytestdemo.baseclass import Baseclass


@pytest.mark.usefixtures("load_data")
class Testexample2(Baseclass):
    def test_editprofile(self,load_data): # we are returning from fixture test thats why we have to pass return argument to this to test method
        log=self.getlogger()

        log.info(load_data[0])
        log.info(load_data[2])
        print(load_data[1])

    def test_crossbrowser(self,browser): #using params to return in test methods
        print(browser)

    def test_crossbrowser(self,browser_tupleset):  # run in tuple format
        print(browser_tupleset[0])
        #print(browser_tupleset)