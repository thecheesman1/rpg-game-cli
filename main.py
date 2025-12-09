"""RPG Game CLI

A simple command-line RPG game.
"""

import sys
import random


class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True


def start_battle():
    # Simple battle system
    player = {'name': 'Hero', 'health': 100, 'attack': 20}
    enemy = {'name': 'Goblin', 'health': 50, 'attack': 15}
    
    from combat import Combat
    combat = Combat(player, enemy)
    combat.battle()


def main():
    print("Welcome to the RPG Game CLI!")
    print("Type 'help' for available commands.")
    
    game = Game()
    
    while True:
        command = input("\n> ").strip().lower()
        
        if command == "quit" or command == "exit":
            print("Thanks for playing!")
            sys.exit(0)
        elif command == "help":
            print("Available commands:")
            print("  help - Show this help message")
            print("  quit/exit - Exit the game")
            print("  start - Start a new game")
            print("  move <row> <col> - Make a move")
            print("  board - Show the board")
            print("  battle - Start a battle")
        elif command == "start":
            print("Starting new game...")
            game = Game()  # Reset game
            game.display_board()
        elif command.startswith("move "):
            try:
                parts = command.split()
                row, col = int(parts[1]), int(parts[2])
                if game.make_move(row, col):
                    winner = game.check_winner()
                    if winner:
                        print(f"Player {winner} wins!")
                        game.display_board()
                    elif game.is_board_full():
                        print("It's a tie!")
                        game.display_board()
                    else:
                        game.display_board()
                else:
                    print("Invalid move!")
            except (ValueError, IndexError):
                print("Invalid move format. Use: move <row> <col>")
        elif command == "board":
            game.display_board()
        elif command == "battle":
            start_battle()
        else:
            print(f"Unknown command: {command}")
            print("Type 'help' for available commands.")


if __name__ == "__main__":
    main()