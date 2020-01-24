from http import HTTPStatus

from fizzbuzz.models import db, Chat


def test_get_chats(client):
    data = {"username": "test", "password": "123"}
    response = client.post("/auth/login", json=data)

    assert "token" in response.get_json()
    token = response.get_json()["token"]
    auth_header = {"Authorization": f"Bearer {token}"}

    response = client.get("/chats/all", headers=auth_header)

    assert response.status_code == HTTPStatus.OK, "Get all chats fail"
    assert response.get_json() == []

    chat = Chat(user="@test", message="hello", response="hello")
    db.session.add(chat)
    db.session.commit()

    response = client.get("/chats/all", headers=auth_header)

    assert response.status_code == HTTPStatus.OK, "Get all chats fail"
    assert response.get_json()[0]["user"] == chat.user
    assert response.get_json()[0]["message"] == chat.message
    assert response.get_json()[0]["response"] == chat.response

    response = client.get(f"/chats/{chat.id}", headers=auth_header)

    assert response.status_code == HTTPStatus.OK, "Get one chat fail"
