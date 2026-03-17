from restaurant_agent import find_best_restaurant
from coupons import coupons

user_location = (12.9716, 77.5946)
results = find_best_restaurant(coupons, user_location)
print("\nTop Food Deals:\n")

for i, r in enumerate(results, start=1):

    print(f"{i}. {r['restaurant']} ({r['distance']} km) — ₹{r['price']}")

    for item, qty in r["order_items"]:
        print(f"   {qty} x {item}")

    print("   Strategy:", r["strategy"])
    print()