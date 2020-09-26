import pytest


@pytest.fixture(scope='class') #This fixture has scope of class after defining scope as class
def browser():
    print("browser starts")
    yield
    print("execute after fixture_demo")

@pytest.fixture()
def load_data():
    print("user profile data is being created")
    return ['TEST1','TEST2','TEST3']

#test fixture of browser where you need to instantiate every time for your test case method
@pytest.fixture(params=['Chrome','firefox','IE'])
def browser(request):
    return request.param

@pytest.fixture(params=[('Chrome','Aditya','IT'),('firefox','test','name'),('IE')]) #tuple format
def browser_tupleset(request):
    return request.param


