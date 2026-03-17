from agent import smart_agent
from coupons import coupons

order_price = 180
delivery_fee = 40

strategy, price = smart_agent(order_price, delivery_fee, coupons)

print("Best Strategy:", strategy)
print("Final Price:", price)