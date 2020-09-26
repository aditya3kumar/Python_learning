import pytest


@pytest.mark.smoke # We mark as smoke testing thats why we mark with this tag
def test_firstprogram():
    msg='HI'
    assert msg =='HELLO','Test fails due to strings do not match'


def test_secondprogram(browser):
    a=4
    b=6

    assert a+2 ==6 ,'Addition do not match'

def test_creditcard_demo2():
    print("Second credit card statement")


