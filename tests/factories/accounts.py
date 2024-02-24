import factory
from apps.accounts.models import User


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Sequence(lambda n: 'email{}@test.com'.format(n))
    first_name = "foo"
    last_name = "bar"
    password = "password123"

    class Meta:
        model = User
