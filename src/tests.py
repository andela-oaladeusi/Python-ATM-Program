# TalaAtm
# Created by Seroney on 04-Dec-16 7:15 PM
from mock import patch


def multiple(c):
    a = int(input("Enter x"))
    b = c * a
    return b


def get_input(text):
    return text


@patch('tests.get_input', return_value = 300)
def test_multiple(input):
    assert (multiple(3), 6)


test_multiple(3)

