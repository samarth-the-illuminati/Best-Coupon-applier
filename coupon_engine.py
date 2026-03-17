def apply_coupon(order_price, delivery_fee, coupon):

    if order_price < coupon["min_order"]:
        return None

    final_price = order_price + delivery_fee

    if coupon["type"] == "flat":
        final_price -= coupon["value"]

    elif coupon["type"] == "percent":
        final_price -= order_price * coupon["value"] / 100

    elif coupon["type"] == "delivery":
        final_price -= delivery_fee

    return final_price


def find_best_coupon(order_price, delivery_fee, coupons):

    best_coupon = None
    best_price = order_price + delivery_fee

    for coupon in coupons:

        final_price = apply_coupon(order_price, delivery_fee, coupon)

        if final_price and final_price < best_price:
            best_price = final_price
            best_coupon = coupon["code"]

    return best_coupon, best_price