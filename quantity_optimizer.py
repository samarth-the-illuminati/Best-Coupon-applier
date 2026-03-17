from itertools import product


def generate_orders(menu, max_quantity=3):

    prices = [item["price"] for item in menu]
    names = [item["item"] for item in menu]
    categories = [item["category"] for item in menu]

    orders = []

    for quantities in product(range(max_quantity + 1), repeat=len(prices)):

        total = 0
        order_items = []
        main_present = False
        valid = True

        for q, price, name, cat in zip(quantities, prices, names, categories):

            if q > 0:

                if cat == "addon" and q > 1:
                    valid = False
                    break

                if cat == "drink" and q > 2:
                    valid = False
                    break

                total += q * price
                order_items.append((name, q))

                if cat == "main":
                    main_present = True

        if valid and total > 0 and main_present:
            orders.append({
                "total": total,
                "items": order_items
            })

    return orders