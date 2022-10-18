import pytest
from src.fizzbuzz import fizzbuzz

def test_when_1_then_1():
    assert fizzbuzz(1) == '1'

def test_when_2_then_2():
    assert fizzbuzz(2) == '2'

def test_when_4_then_4():
    assert fizzbuzz(4) == '4'