import factory
from apps.accounts.models import User


class UserFactory(factory.Factory):
    email = "email@test.com"
    first_name = "foo"
    last_name = "bar"
    password = "password123"

    class Meta:
        model = User
