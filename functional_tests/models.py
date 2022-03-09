class User(object):
    def __init__(self, user: object, cash: float) -> None:
        self.user_profile = user
        self.cash = cash


class Listing(object):
    def __init__(
        self, title: str, description: str, image_path: str, price: float, owner: User
    ) -> None:
        self.title = title
        self.description = description
        self.image = image_path
        self.start_price = price
        self.owner = owner


class Bid(object):
    def __init__(self, bid: object, owner: User, listing: Listing) -> None:
        self.bid = bid
        self.owner = owner
        self.listing = listing


class Comment(object):
    def __init__(self, text: str, owner: User, listing: Listing) -> None:
        self.text = text
        self.owner = owner
        self.listing = listing
