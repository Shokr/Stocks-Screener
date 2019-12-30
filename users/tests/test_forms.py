import pytest

from users.forms import UserForm
from users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestUserForm:
    def test_clean_username(self):
        # A user with proto_user params does not exist yet.
        proto_user = UserFactory.build()

        form = UserForm(
            {
                "user_name": proto_user.username,
                "email": proto_user.email,
                "mobile": proto_user.mobile,
                "password": proto_user._password,
            }
        )

        assert form.is_valid()
        assert form.clean_username() == proto_user.username

        # Creating a user.
        form.save()

        # The user with proto_user params already exists,
        # hence cannot be created.
        form = UserForm(
            {
                "user_name": proto_user.username,
                "email": proto_user.email,
                "mobile": proto_user.mobile,
                "password": proto_user._password,
            }
        )

        assert not form.is_valid()
        assert len(form.errors) == 1
        assert "username" in form.errors
