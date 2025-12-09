"""RPG Game CLI

A simple command-line RPG game.
"""

import sys


def main():
    print("Welcome to the RPG Game CLI!")
    print("Type 'help' for available commands.")
    
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
        elif command == "start":
            print("Starting new game...")
            # Game logic would go here
        else:
            print(f"Unknown command: {command}")
            print("Type 'help' for available commands.")


if __name__ == "__main__":
    main()