from car import Car
import math

class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int | float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_fuel(self, location2: list) -> float:
        distance = math.sqrt((location2[0] - self.location[0]) ** 2 + (location2[1] - self.location[1]) ** 2)
        fuel_used = distance * self.car.fuel_consumption
        return round(fuel_used, 2)