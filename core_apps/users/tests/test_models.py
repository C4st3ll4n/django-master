import pytest


def test_user_str(base_user):
    assert base_user.__str__() == f"{base_user.username}"


def test_user_short_name(base_user):
    short_name = f"{base_user.first_name}"
    assert base_user.get_short_name() == short_name


def test_user_full_name(base_user):
    full_name = f"{base_user.first_name} {base_user.last_name}"
    assert base_user.get_full_name == full_name


def test_user_email_normalized(base_user):
    email = base_user.email
    assert email == email.lower()


def test_super_user_email_normalized(super_user):
    email = super_user.email
    assert email == email.lower()


def test_super_user_is_not_staff(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=False)
    assert str(err.value) == "Superusers must have is_staff=True"


def test_super_user_is_not_superuser(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=False, is_staff=False)
    assert str(err.value) == "Superusers must have is_superuser=True"


def test_create_user_without_email(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None)
    assert str(err.value) == "Base User Account: An email address is required"


def test_create_user_without_username(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(username=None)
    assert str(err.value) == "You must provide a valid username"


def test_create_user_without_first_name(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(first_name=None)
    assert str(err.value) == "You must provide a valid first name"


def test_create_user_without_last_name(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(last_name=None)
    assert str(err.value) == "You must provide a valid last name"


def test_create_super_user_without_email(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None, is_superuser=True, is_staff=True)
    assert str(err.value) == "Admin Account: An email address is required"


def test_create_super_user_without_password(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(password=None, is_superuser=True, is_staff=True)
    assert str(err.value) == "You must provide a valid password"


def test_create_user_with_email_incorrect(user_factory):
    with pytest.raises(ValueError) as err:
        user_factory.create(email="testebemlidos.com",)
    assert str(err.value) == "You must provide a valid password"
