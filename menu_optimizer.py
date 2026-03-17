from itertools import combinations


def generate_orders(menu):

    items = [item["price"] for item in menu]

    orders = []

    for r in range(1, len(items) + 1):
        for combo in combinations(items, r):
            orders.append(sum(combo))

    return orders