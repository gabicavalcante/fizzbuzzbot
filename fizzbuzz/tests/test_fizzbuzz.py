from fizzbuzz.blueprints.restapi.bot import get_response


def test_fizzbuzz_response():
    assert get_response("5") == "Buzz"
    assert get_response("3") == "Fizz"
    assert get_response("15") == "FizzBuzz"


def test_not_fizzbuzz_response():
    assert get_response("17") == 17
    assert get_response("hello") == "Hey, 'hello' is not a valid input :("
