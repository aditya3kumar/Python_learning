import pytest


@pytest.mark.usefixtures("browser")
class Testfixture_demo:

    def test_fixture_demo1(self):
        print("fixture demo1")

    def test_fixture_demo2(self):
        print("fixture demo1")


    def test_fixture_demo3(self):
        print("fixture demo3")

    def test_fixture_demo4(self):
        print("fixture demo4")