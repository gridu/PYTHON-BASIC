from dataclasses import dataclass


@dataclass
class BookRaw:
    title: str
    price_raw: str
    rating_raw: str


@dataclass
class Book:
    title: str
    price: float
    rating: float
