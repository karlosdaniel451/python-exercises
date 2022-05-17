from dataclasses import dataclass

from src.dish import Dish


@dataclass(eq=False)
class Order:
    client_name: str
    dish: Dish
    quantity: int

    #  def __eq__(self, other):
    #      return self.client_name == other.client_name and \
    #          self.dish == other.dish and self.quantity == quantity

    def get_total_price_in_cents(self) -> int:
        """
        Get the total price in cents of the order, which is equals to
        the unit price of the dish times the quantity.
        """
        return self.dish.unit_price_in_cents * self.quantity
