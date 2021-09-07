shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

# prices가 3개고 coupons가 2개이므로 index를 사용해서 해결.
def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):
        max_discounted_price += prices[price_index] * (100 - coupons[coupon_index]) / 100
        price_index += 1
        coupon_index += 1

    while price_index < len(prices):
        max_discounted_price += prices[price_index]
        price_index += 1
    return max_discounted_price


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.