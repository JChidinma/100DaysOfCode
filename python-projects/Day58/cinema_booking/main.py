import sqlite3
from seat import Seat
from ticket import Ticket
from user import User
from payment_card import Card


def initialize_db():
    cinema_db = "cinema.db"
    banking_db = "banking.db"

    """Initialize the cinema and banking databases for the demo"""
    # Cinema database initialization
    connection = sqlite3.connect(cinema_db)
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS "Seat" (
        "seat_id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "price" REAL NOT NULL,
        "taken" INTEGER NOT NULL DEFAULT 0
    )
    """)
    cursor.execute("""
    INSERT OR IGNORE INTO "Seat" ("seat_id", "price", "taken") VALUES
    (1, 10.0, 0), (2, 12.0, 0), (3, 15.0, 0)
    """)
    connection.commit()
    connection.close()

    # Banking database initialization
    connection = sqlite3.connect(banking_db)
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS "Card" (
        "number" TEXT PRIMARY KEY,
        "cvc" TEXT NOT NULL,
        "holder_name" TEXT NOT NULL,
        "balance" REAL NOT NULL
    )
    """)
    cursor.execute("""
    INSERT OR IGNORE INTO "Card" ("number", "cvc", "holder_name", "balance") VALUES
    ('1234567812345678', '123', 'John Doe', 100.0)
    """)
    connection.commit()
    connection.close()


def main():
    """Simulate a user buying a cinema ticket with their bank card"""
    initialize_db()

    username = input("Enter your name: ")
    seat_id = int(input("Enter the seat number you prefer (1, 2, 3, ...): "))

    # Create User object
    user = User(name=username)
    seat = Seat(seat_id=seat_id)

    # Get user's card details
    card_number = input("Enter your 16 digit card number: ")
    cvc = input("Enter the 3 digit numbers (CVC) at the back of your card: ")
    holder_name = input("Enter card holder name: ")
    card = Card(card_type="VISA", number=card_number,
                cvc=cvc, holder_name=holder_name)
    result = user.buy_ticket(seat=seat, card=card)
    print(result)


if __name__ == "__main__":
    main()
