def find_add_item_strategy(order_price, delivery_fee, coupon):

    min_order = coupon["min_order"]

    if order_price >= min_order:
        return None

    needed = min_order - order_price

    new_order_price = order_price + needed

    if coupon["type"] == "flat":
        final_price = new_order_price + delivery_fee - coupon["value"]

    elif coupon["type"] == "percent":
        final_price = new_order_price - (new_order_price * coupon["value"] / 100) + delivery_fee

    else:
        final_price = new_order_price

    return {
        "add_item_cost": needed,
        "new_total": final_price
    }