import sqlite3


class Seat:
    database = "cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        """Get the price of a certain seat"""
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            SELECT "price" FROM "Seat" WHERE "seat_id" = ?
            """, [self.seat_id])
            # price = cursor.fetchall()[0][0]
            # return price
            price = cursor.fetchone()
            if price:
                return price[0]
            else:
                raise ValueError(
                    f"Seat with ID {self.seat_id} is not available.")

    def is_free(self):
        """Check in the database if a Seat is taken or not"""
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            SELECT "price" FROM "Seat" WHERE "seat_id" = ?
            """, [self.seat_id])
            # result = cursor.fetchall()[0][0]
            result = cursor.fetchone()
            if result is not None:
                return result[0] == 0
            else:
                raise ValueError(f"Seat with ID {self.seat_id} not found.")

    def occupy(self):
        """Change value of taken in the database from 0 to 1 if Seat is free"""
        if self.is_free():
            with sqlite3.connect(self.database) as connection:
                cursor = connection.cursor()
                connection.execute("""
                UPDATE "Seat" SET "taken"=1 WHERE "seat_id"=?
                """, [self.seat_id])
                connection.commit()
        else:
            raise ValueError(f"Seat {self.seat_id} is already occupied.")
