import pytest
from src.fizzbuzz import fizzbuzz

def test_when_1_then_1():
# FIXTURE
    input_value = '1'

    # EXERCISE
    result = fizzbuzz(input_value)

    # ASSERT
    assert result == '1'
    

def test_when_2_then_2():
# FIXTURE
    input_value = '2'

    # EXERCISE
    result = fizzbuzz(input_value)

    # ASSERT
    assert result == '2'
    

def test_when_4_then_4():
# FIXTURE
    input_value = '4'

    # EXERCISE
    result = fizzbuzz(input_value)

    # ASSERT
    assert result == '4'


def test_when_3_then_fizz():
# FIXTURE
    input_value = '3'

    # EXERCISE
    result = fizzbuzz(input_value)

    # ASSERT
    assert result == 'fizz'


def test_when_6_then_fizz():
# FIXTURE
    input_value = '6'

    # EXERCISE
    result = fizzbuzz(input_value)

    # ASSERT
    assert result == 'fizz'


def test_when_9_then_fizz():
    # FIXTURE
    input_value = '9'

    # EXERCISE
    result = fizzbuzz(input_value)

    # ASSERT
    assert result == 'fizz'


def test_when_12_then_fizz():
    # FIXTURE
    input_value = '12'

    # EXERCISE
    result = fizzbuzz(input_value)

    # ASSERT
    assert result == 'fizz'


def test_when_5_then_buzz():
    # FIXTURE
    input_value = '5'

    # EXERCISE
    result = fizzbuzz(input_value)

    # ASSERT
    assert result == 'buzz'


def test_when_10_then_buzz():
    # FIXTURE
    input_value = '10'

    # EXERCISE
    result = fizzbuzz(input_value)

    # ASSERT
    assert result == 'buzz'


def test_when_invalid_then_exception():
    # FIXTURE
    input_value = "invalid string"

    # EXERCISE
    with pytest.raises(Exception) as error:
        fizzbuzz(input_value)

    # ASSERT
    assert error.value.args[0] == "A entrada precisa ser um número"