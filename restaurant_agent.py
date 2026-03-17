from data_loader import load_restaurants
from quantity_optimizer import generate_orders
from agent import smart_agent
from geo_utils import distance_km


def find_best_restaurant(coupons, user_location, top_k=5):

    restaurants = load_restaurants()

    MIN_ORDER_VALUE = 150
    MAX_DISTANCE = 8 # km

    user_lat, user_lon = user_location

    results = []

    for restaurant in restaurants:

        # Get restaurant location
        lat, lon = restaurant["location"]

        # Compute distance
        dist = distance_km(user_lat, user_lon, lat, lon)

        # Skip far restaurants
        if dist > MAX_DISTANCE:
            continue

        orders = generate_orders(restaurant["menu"])

        for order in orders:

            order_price = order["total"]

            if order_price < MIN_ORDER_VALUE:
                continue

            strategy, price = smart_agent(
                order_price,
                restaurant["delivery_fee"],
                coupons
            )

            results.append({
                "restaurant": restaurant["name"],
                "distance": round(dist, 2),
                "order_items": order["items"],
                "order_price": order_price,
                "strategy": strategy,
                "price": price
            })

    results.sort(key=lambda x: (x["price"], len(x["order_items"]), x["order_price"]))

    return results[:top_k]