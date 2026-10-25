"""Simple function to unit test."""


def calculate_total(price: float, quantity: int) -> float:
    if quantity < 0:
        raise ValueError("quantity must not be negative")
    return price * quantity
