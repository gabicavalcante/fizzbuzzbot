import pytest
from fizzbuzz.ext.commands import create_user
from fizzbuzz.models import User


def test_create_user():
    user = create_user("user", "pwd")
    assert user == User.query.filter_by(username="user").first()


@pytest.mark.xfail(raises=RuntimeError)
def test_create_user_error():
    create_user("user", "pwd")
    create_user("user", "pwd")
