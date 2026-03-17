import json


def load_restaurants():

    with open("data/restaurants.json") as f:
        restaurants = json.load(f)

    return restaurants