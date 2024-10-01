from seat import Seat
from ticket import Ticket
from payment_card import Card


class User:
    """Represents a user that can buy a cinema Seat"""

    def __init__(self, name):
        self.name = name

    def buy_ticket(self, seat, card):
        """Buys the ticket if the card is valid"""
        try:
            if seat.is_free():
                price = seat.get_price()
                if card.validate(price=price):
                    seat.occupy()
                    ticket = Ticket(
                        user=self, price=seat.get_price(), seat_number=seat_id)
                    ticket.save_ticket_to_pdf()
                    return "Purchase successful!"
                else:
                    return "Invalid Payment Card!"
            else:
                return "Seat is already taken."
        except ValueError as e:
            return f"Error: {str(e)}"
