from fizzbuzz.blueprints.restapi.bot import get_response, get_alternative_response


expected_responses = {
    "/start": "Hey, send me a integer, and I'll do my work ;)",
    "/help": "My work is check if the message is a integer multiples of three (Fizz), five (Buzz) or both (FizzBuzz).",
}


def test_fizzbuzz_response():
    assert get_response("5") == "Buzz"
    assert get_response("3") == "Fizz"
    assert get_response("15") == "FizzBuzz"


def test_not_fizzbuzz_response():
    assert get_response("17") == 17
    assert get_response("hello") == "Hey, 'hello' is not a valid input :("


def test_get_alternative_response():
    assert get_response("/start") == expected_responses["/start"]
    assert get_alternative_response("/start") == expected_responses["/start"]
    assert get_alternative_response("/help") == expected_responses["/help"]
