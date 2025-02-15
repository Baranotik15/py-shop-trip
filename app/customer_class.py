import math
from datetime import datetime

from app.car import Car
from app.shop import Shop


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

    def calculate_distance(self, shop_location: list) -> float:
        distance = math.dist(self.location, shop_location)
        return round(distance, 2)

    def calculate_total_trip_cost(
            self,
            shop: Shop,
            fuel_price: float
    ) -> tuple:
        distance_to_shop = self.calculate_distance(shop.location)
        fuel_cost = self.car.calculate_fuel_cost(distance_to_shop, fuel_price)
        products_cost = sum(
            self.product_cart[product] * price
            for product, price in shop.products.items()
            if product in self.product_cart
        )
        total_cost = 2 * fuel_cost + products_cost

        return total_cost, products_cost, fuel_cost

    def make_purchase(
            self,
            shop: Shop,
            fuel_price: float
    ) -> None:
        total_cost, products_cost, fuel_cost =\
            self.calculate_total_trip_cost(shop, fuel_price)

        now = datetime(2021, 1, 4, 12, 33, 41).strftime("%d/%m/%Y %H:%M:%S")

        if self.money >= total_cost:
            self.money -= total_cost
            self.location = shop.location

            print(f"Date: {now}")
            print(f"Thanks, {self.name}, for your purchase!")
            for product, quantity in self.product_cart.items():
                if product in shop.products:
                    print(f"You have bought: {quantity} {product}"
                          f" for {round(quantity * shop.products[product], 2)}"
                          f" dollars")
            print(f"Total cost is {round(products_cost, 2)} dollars")
            print("See you again!")

            self.money += (self.money - total_cost)
            print(f"{self.name} rides home")
            print(f"{self.name} now has {self.money: .2f} dollars")
        else:
            print(f"{self.name} doesn't have enough money"
                  f" to make a purchase in {shop.name}")
