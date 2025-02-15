import json

from car import Car
from shop import Shop
from customer_class import Customer


def shop_trip():
    customers = []
    shop_list = []

    try:
        with open("config.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("The config.json file was not found")
        return
    except json.JSONDecodeError:
        print("The config.json file is not in the correct format")
        return

    for people in data['customers']:
        car = Car(
            brand=people["car"]["brand"],
            fuel_consumption=people["car"]["fuel_consumption"]
        )
        customer = Customer(
            name=people["name"],
            product_cart=people["product_cart"],
            location=people["location"],
            money=people["money"],
            car=car
        )
        customers.append(customer)

    for shop in data["shops"]:
        shop_data = Shop(
            name= shop["name"],
            location=shop["location"],
            products=shop["products"],
        )
        shop_list.append(shop_data)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shop_list:
            fuel_cost = round(customer.calculate_fuel(shop.location) * data["FUEL_PRICE"], 2)
            print(f"{customer.name}`s trip to the {shop.name} costs {fuel_cost}")


shop_trip()