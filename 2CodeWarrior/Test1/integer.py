import codewars_test as test
from solution import number_to_string

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(number_to_string(67), '67')
        test.assert_equals(number_to_string(79585), '79585')
        test.assert_equals(number_to_string(79585), "79585")
        test.assert_equals(number_to_string(1+2), '3')
        test.assert_equals(number_to_string(1-2), '-1')

def number_to_string(num):
    return num.format{number_to_string}
    # Return a string of the number here!

def number_to_string(num):
    return f"{num}"
