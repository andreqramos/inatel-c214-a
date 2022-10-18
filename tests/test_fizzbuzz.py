import pytest
from src.fizzbuzz import fizzbuzz

def test_when_1_then_1():
    assert fizzbuzz(1) == '1'

def test_when_2_then_2():
    assert fizzbuzz(2) == '2'

def test_when_4_then_4():
    assert fizzbuzz(4) == '4'

def test_when_3_then_fizz():
    assert fizzbuzz(3) == 'fizz'

def test_when_6_then_fizz():
    assert fizzbuzz(6) == 'fizz'

def test_when_9_then_fizz():
    assert fizzbuzz(9) == 'fizz'