def calculate_total(prices):
    sum = 0
    for price in prices:
        sum += price
    return sum

def apply_tax(amount):
    return amount*1.05