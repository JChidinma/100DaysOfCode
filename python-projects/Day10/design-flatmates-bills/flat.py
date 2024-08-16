class Bill:
    """
    Object containing data about a bill, such as total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate who is a person that lives in the house and pays part of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def amount_paid(self, bill, flatmate2):
        weight = self.days_in_house / \
            (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay
