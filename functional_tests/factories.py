import random

import factory

from .models import Bid, Comment, Listing, User


class UserFactory(factory.Factory):
    class Meta:
        model = User

    user_profile = factory.Faker("profile")
    cash = factory.LazyFunction(lambda: (random.randint(100000, 200000) / 100))


class ListingFactory(factory.Factory):
    class Meta:
        model = Listing

    title = factory.Faker("text", max_nb_chars=20)
    description = factory.Faker("sentence", nb_words=30)
    image = factory.Faker("file_path", depth=3)
    start_price = factory.LazyFunction(lambda: (random.randint(100, 119999) / 100))
    owner = factory.SubFactory(UserFactory)


class BidFactory(factory.Factory):
    class Meta:
        model = Bid

    bid = factory.LazyFunction(lambda: (random.randint(99, 50000) / 100))
    owner = factory.SubFactory(UserFactory)
    listing = factory.SubFactory(ListingFactory)


class CommentFactory(factory.Factory):
    class Meta:
        model = Comment

    text = factory.Faker("paragraph", nb_sentences=5)
    owner = factory.SubFactory(UserFactory)
    listing = factory.SubFactory(ListingFactory)
