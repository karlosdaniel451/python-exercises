from dataclasses import dataclass

@dataclass
class Dish:
    name: str
    ingredients: list[str]
    unit_price_in_cents: int

    def __eq__(self, other):
        return self.name == other.name
