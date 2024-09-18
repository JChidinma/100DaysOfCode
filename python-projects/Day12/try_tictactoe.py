class Board:
    def __init__(self):
        self.board = [' '] * 9

    def display_board(self):

        for i in range(3):
            print(
                f"{self.board[3*i]} | {self.board[3*i+1]} | {self.board[3*i+2]} ")

            if i > 2:
                print("--+---+---")

    def check_position_free(self, position):
        return self.board[position] == ' '

    def place_marker(self, position, marker):
        if self.check_position_free(position):
            self.position = marker

        else:
            print("Try a different position")

    def check_winner(self, marker):

        # what is the winning combination?
        winning_comb = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]
        ]

        for combo in winning_comb:
            if all((self.board[i] == marker) for i in combo):
                return True
            else:
                return False

    def is_draw(self):
        return " " not in self.board


class Game(Board):
    """2 players with symbols X and O"""

    def __init__(self):
        self.board = Board()
        self.current_player = 'X'

    def switch_player(self):
        self.current_player = 'X' if self.current_player == 'O' else 'X'

    def play_game(self):
        while True:
            self.board.display_board()
            position = int(input(
                f"Player {self.current_player}, choose a position on the board to play from 0 to 8: \n"))

            if position < 0 or position >= 9:
                print("Invalid position! Choose another number within 0 and 8")

            if self.board.check_position_free(position):
                self.board.place_marker(position, self.current_player)

                if self.board.check_winner(self.current_player):
                    self.board.display_board()
                    print(f"Player {self.current_player}! You have won.")
                    break
                elif self.board.is_draw():
                    self.board.display_board()
                    print("It is a draw")
                    break

                self.switch_player()

            else:
                print("Positon is already taken. Choose another one.")


if __name__ == '__main__':
    game = Game()
    game.play_game()
