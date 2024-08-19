class Paint:
    def __init__(self, buckets, color):
        self.buckets = buckets
        self.color = color

    # The price of paint buckets depends on if it is white or not white
    def total_price(self):
        if self.color == "white":
            return self.buckets * 1.99

        else:
            return self.buckets * 2.19

# Make DiscuntedPaint to inherit the Paint class


class DiscuntedPaint(Paint):
    def discounted_price(self, discount_percentage):
        total = self.total_price()

        discout_amt = total * (discount_percentage/100)
        total_price_at_discount = total - discout_amt
        return total_price_at_discount
