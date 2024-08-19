"""
Design an Interactive Tic-Tac-Toe Game in Python

Objective:
Build a two-player (X and O) tic-tac-toe game that allows users to take turns placing their symbols on a 3x3 grid.

Board Class:
There will be methods for :
    1. display_board
    2. place a marker
    3. check winner
    4. check if it is a draw
    5. check if a position in the board is free to place a marker

Game Class:
    - play game
    - switch player

combinations =
[0, 1, 2]
[3, 4, 5]
[6, 7, 8]
"""


class Board:
    def __init__(self):
        self.board = [' '] * 9

    def display_board(self):
        for i in range(3):
            print(
                f"{self.board[3*i]} | {self.board[3*i+1]}, | {self.board[3*i+2]}")
            if i < 2:
                print("--+---+---")

    def is_position_free(self, position):
        return self.board[position] == ' '

    def place_marker(self, position, marker):
        if self.is_position_free(position):
            self.board[position] = marker

    def check_for_winner(self, marker):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]
        ]
        return any(all(self.board[i] == marker for i in combo) for combo in win_combinations)

    def is_draw(self):
        return " " not in self.board


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player_marker = 'X'

    def switch_player(self):
        self.current_player_marker = 'O' if self.current_player_marker == 'X' else 'X'

    def play_game(self):
        while True:
            self.board.display_board()
            position = int(
                input(f"Player {self.current_player_marker}, choose your position from 0-8: \n"))

            if position < 0 or position >= 9:
                print("Invalid position. Choose a different number between 0 and 8.")
                continue

            if self.board.is_position_free(position):
                self.board.place_marker(position, self.current_player_marker)

                if self.board.check_for_winner(self.current_player_marker):
                    self.board.display_board()
                    print(f"Player {self.current_player_marker} has won.")
                    break

                elif self.board.is_draw():
                    self.board.display_board()
                    print("It is a draw! Keep playing...")
                    break
                self.switch_player()
            else:
                print("Position is already taken. Choose another one.")


if __name__ == "__main__":
    game = Game()
    game.play_game()
