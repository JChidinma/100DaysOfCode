import sqlite3


class Card:
    """Represents a bank card needed to fnalize a Seat purchase"""
    database = "banking.db"

    def __init__(self, card_type, number, cvc, holder_name):
        self.holder_name = holder_name
        self.card_type = card_type
        self.number = number
        self.cvc = cvc

    def validate(self, price):
        """
        Checks if card is valid and has balance.
        Subtracts price from balance.
        """
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT "balance" FROM "Card" WHERE "number"=? and "cvc"=?
                """, [self.number, self.cvc])
            result = cursor.fetchone()

            if result:
                balance = result[0]
                if balance >= price:
                    new_balance = balance - price
                    cursor.execute("""
                UPDATE "Card" SET "balance" = ? WHERE "number"=? and "cvc"=?
                """, [new_balance, self.number, self.cvc])
                    connection.commit()
                    # connection.close()
                    return True

                else:
                    return False  # Insufficient balance
            else:
                raise ValueError("Card validation faild. Check your details.")
