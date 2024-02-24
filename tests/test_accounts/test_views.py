import json
import pytest
from pytest_factoryboy.fixture import register
from http import HTTPStatus
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.reverse import reverse
from apps.accounts.models import User
from tests.factories.accounts import UserFactory

pytestmark = pytest.mark.django_db

register(UserFactory, "another_user")


def test_list_users(api_client, user_factory, another_user):
    user_factory().save()
    another_user.email = "new_test@email.com"
    another_user.save()
    url = reverse("user-list")
    response = api_client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()["results"]) == 3


def test_create_user(api_client, user_payload):
    url = reverse("user-list")
    response = api_client.post(url, user_payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(email=user_payload["email"]).exists()


@pytest.mark.parametrize(
    "field", ["first_name", "email", "password"]
)
def test_create_user_without_field(field, api_client, user_payload):
    user_payload.pop("last_name")
    user_payload.pop(field)
    url = reverse("user-list")
    response = api_client.post(url, user_payload)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_detail_user(api_client, user):
    user.save()
    url = reverse("user-detail", kwargs={"pk": user.id})
    response = api_client.get(url)
    assert response.status_code == HTTPStatus.OK


def test_detail_user_nonexistent(api_client):
    url = reverse("user-detail", kwargs={"pk": 123})
    response = api_client.get(url)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_user(api_client, user):
    user.save()
    url = reverse("user-detail", kwargs={"pk": user.id})
    payload = {
        "email": "test@mail.com"
    }
    response = api_client.patch(url, json.dumps(payload), content_type="application/json")

    assert response.status_code == HTTPStatus.OK
    assert user.id == response.json()["id"]
    assert user.email != response.json()["email"]


def test_login(api_client):
    User.objects.create_user(
        email="test@example.com", password="testpassword", first_name="test", last_name="user"
    )
    url = reverse("user-login")
    login_data = {
        "email": "test@example.com",
        "password": "testpassword"
    }

    response = api_client.post(url, login_data, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["message"] == "User successfully logged in"


def test_logout(user, api_client):
    user.save()
    url = reverse("user-logout")
    token = Token.objects.create(user=user)

    header = {"Authorization": f"Token {token.key}"}
    response = api_client.post(url, format="json", headers=header)

    assert response.status_code == status.HTTP_200_OK
    assert not Token.objects.filter(user=user).exists()
