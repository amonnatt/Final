from function import validate_number,chack_car
import pytest

@pytest.mark.number  # pytest -m number
def test_input_0():
    input = 0
    exected_result = "No Passenger"
    actual_result = chack_car(input)
    assert exected_result == actual_result

@pytest.mark.number  # pytest -m number
def test_input_1():
    input = 1
    exected_result = "van: 0"+" "+"car: 1"
    actual_result = chack_car(input)
    assert exected_result == actual_result

@pytest.mark.number  # pytest -m number
def test_input_4():
    input = 4
    exected_result = "van: 0"+" "+"car: 1"
    actual_result = chack_car(input)
    assert exected_result == actual_result

@pytest.mark.number  # pytest -m number
def test_input_11():
    input = 11
    exected_result = "van: 1"+" "+"car: 0"
    actual_result = chack_car(input)
    assert exected_result == actual_result


@pytest.mark.number  # pytest -m number
def test_input_11():
    input = 12
    exected_result = "van: 1"+" "+"car: 0"
    actual_result = chack_car(input)
    assert exected_result == actual_result

# @pytest.mark.number  # pytest -m number
# def test_input_22():
#     input = 22
#     exected_result = "van: 2"+" "+"car: 0"
#     actual_result = chack_car(input)
#     assert exected_result == actual_result

# @pytest.mark.number  # pytest -m number
# def test_input_23():
#     input = 23
#     exected_result = "van: 2"+" "+"car: 1"
#     actual_result = chack_car(input)
#     assert exected_result == actual_result

@pytest.mark.validate  # pytest -m validate
def test_input_integer_input_a():
    input = "a"
    exected_result = "input integer"
    actual_result = validate_number(input)
    assert exected_result == actual_result

@pytest.mark.validate  # pytest -m validate
def test_input_integer_input_sharp():
    input = "#"
    exected_result = "input integer"
    actual_result = validate_number(input)
    assert exected_result == actual_result

@pytest.mark.validate  # pytest -m validate
def test_input_integer_input_sharp():
    input = 0.1
    exected_result = "input integer"
    actual_result = validate_number(input)
    assert exected_result == actual_result