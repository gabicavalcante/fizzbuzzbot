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
    assert get_response("17") == "17"
    assert get_response("hello") == "Hey, 'hello' is not a valid input :("


def test_get_alternative_response():
    assert get_response("/start") == expected_responses["/start"]
    assert get_alternative_response("/start") == expected_responses["/start"]
    assert get_alternative_response("/help") == expected_responses["/help"]


BIG = "6432567452367546723156745123678548673215467123586475236781456871235476512367458672354786532187645867321548675231867451623754867352867451362785468712354673251876452367154687123587465231674586712354672531674568723154678235674586723514685238176452367815486732154678532187645123867452"


def test_fix_bug():
    assert get_response(BIG) == BIG
