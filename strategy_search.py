from coupon_engine import apply_coupon
from optimizer import find_add_item_strategy


def search_best_strategy(order_price, delivery_fee, coupons):

    strategies = []

    # baseline strategy
    strategies.append({
        "strategy": "No Coupon",
        "price": order_price + delivery_fee
    })

    for coupon in coupons:

        # direct coupon
        final = apply_coupon(order_price, delivery_fee, coupon)

        if final:
            strategies.append({
                "strategy": f"Apply {coupon['code']}",
                "price": final
            })

        # add-item trick
        trick = find_add_item_strategy(order_price, delivery_fee, coupon)

        if trick:
            strategies.append({
                "strategy": f"Add ₹{trick['add_item_cost']} item + {coupon['code']}",
                "price": trick["new_total"]
            })

    best = min(strategies, key=lambda x: x["price"])

    return best, strategies