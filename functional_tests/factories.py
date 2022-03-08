import factory


class UserFactory(factory.Factory):
    user_profile = factory.Faker("profile")


class ListingFactory(factory.Factory):
    title = factory.Faker("title")
