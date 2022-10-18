import pytest
from src.fizzbuzz import fizzbuzz

def test_when_1_then_1():
    assert fizzbuzz(1) == '1'