import factory

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from faker import Factory as FakerFactory

fkr = FakerFactory.create()
User = get_user_model()


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.LazyAttribute(lambda x: fkr.first_name())
    last_name = factory.LazyAttribute(lambda x: fkr.last_name())
    username = factory.LazyAttribute(lambda x: fkr.first_name().lower())
    email = factory.LazyAttribute(lambda o: "%s@example.org" % o.username)
    password = factory.LazyAttribute(lambda x: fkr.password())
    is_active = True
    is_staff = False

    class Meta:
        model = User

    @classmethod
    def create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        if "is_superuser" in kwargs:
            return manager.create_superuser(*args, **kwargs)
        else:
            return manager.create_user(*args, **kwargs)
