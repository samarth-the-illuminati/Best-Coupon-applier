from strategy_search import search_best_strategy


def smart_agent(order_price, delivery_fee, coupons):

    best, strategies = search_best_strategy(order_price, delivery_fee, coupons)

    return best["strategy"], best["price"]