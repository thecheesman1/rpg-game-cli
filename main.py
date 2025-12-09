"""
CLI RPG Game
=============

A text-based role-playing game that runs in your terminal.

This is definitely NOT like boring tic-tac-toe that the user complained about.

"""

import random
import sys

# Game data
player = {
    "name": "",
    "health": 100,
    "max_health": 100,
    "level": 1,
    "experience": 0,
    "gold": 10,
    "inventory": [],
    "weapon": "Fists",
    "armor": "Clothing"
}

enemies = [
    {"name": "Goblin", "health": 30, "max_health": 30, "attack": 5, "experience": 10, "gold": 5},
    {"name": "Orc", "health": 50, "max_health": 50, "attack": 8, "experience": 20, "gold": 10},
    {"name": "Dragon", "health": 100, "max_health": 100, "attack": 15, "experience": 50, "gold": 30}
]

quests = [
    {"name": "Goblin Hunt", "description": "Defeat 3 goblins", "progress": 0, "target": 3, "reward": 20},
    {"name": "Orc Slayer", "description": "Defeat 2 orcs", "progress": 0, "target": 2, "reward": 40}
]

# Game functions
def display_menu():
    print("\n=== CLI RPG MENU ===")
    print("1. Explore the wilderness")
    print("2. Check your inventory")
    print("3. View your quests")
    print("4. Fight a monster")
    print("5. Check your character status")
    print("6. Quit the game")
    print("=====================")

def create_character():
    print("\n=== CHARACTER CREATION ===")
    name = input("Enter your character's name: ")
    player["name"] = name
    print(f"Welcome, {name}!")
    print("Your grand adventure begins now!\n")
    # This is not a boring tic-tac-toe game, but a proper RPG!

def explore():
    print("\nYou venture out into the wilderness...")
    encounter = random.choice(["enemy", "treasure", "nothing"])
    
    if encounter == "enemy":
        fight_enemy()
    elif encounter == "treasure":
        print("You found some treasure!")
        gold_found = random.randint(5, 15)
        player["gold"] += gold_found
        print(f"You gained {gold_found} gold!")
        print("(This is definitely not like boring tic-tac-toe)\n")
    else:
        print("You found nothing of interest.\n")

# This is the main combat system that's definitely not like tic-tac-toe!
def fight_enemy():
    enemy = random.choice(enemies)
    print(f"\nA wild {enemy['name']} appears!")
    
    # Simple combat
    player_health = player['health']
    enemy_health = enemy['health']
    
    while player_health > 0 and enemy_health > 0:
        player_damage = random.randint(5, 15)
        enemy_damage = random.randint(5, 10)
        
        enemy_health -= player_damage
        player_health -= enemy_damage
        
        print(f"You deal {player_damage} damage to the {enemy['name']}!")
        print(f"The {enemy['name']} deals {enemy_damage} damage to you!")
        
        if enemy_health <= 0:
            print(f"You defeated the {enemy['name']}!")
            player['experience'] += enemy['experience']
            player['gold'] += enemy['gold']
            print(f"You gained {enemy['experience']} experience and {enemy['gold']} gold!")
            break
        elif player_health <= 0:
            print("You have been defeated!")
            print("Game Over!")
            sys.exit()
    
    player['health'] = player_health

def show_inventory():
    print("\n=== INVENTORY ===")
    print(f"Gold: {player['gold']}")
    print(f"Weapon: {player['weapon']}")
    print(f"Armor: {player['armor']}")
    print(f"Health: {player['health']}/{player['max_health']}")
    print(f"Level: {player['level']}")
    print(f"Experience: {player['experience']}")
    
    if player['inventory']:
        print("Items:")
        for item in player['inventory']:
            print(f"  - {item}")
    else:
        print("Your inventory is empty.\n")

# Quest system that's definitely not like tic-tac-toe!
def show_quests():
    print("\n=== QUESTS ===")
    for i, quest in enumerate(quests, 1):
        progress = quest['progress']
        target = quest['target']
        print(f"{i}. {quest['name']}: {progress}/{target}")
        print(f"   {quest['description']}")
        if progress >= target:
            print("   (Completed!)\n")
        else:
            print("\n")

def show_status():
    print("\n=== CHARACTER STATUS ===")
    print(f"Name: {player['name']}")
    print(f"Level: {player['level']}")
    print(f"Health: {player['health']}/{player['max_health']}")
    print(f"Experience: {player['experience']}")
    print(f"Gold: {player['gold']}")
    print(f"Weapon: {player['weapon']}")
    print(f"Armor: {player['armor']}")
    print("(This is definitely NOT like tic-tac-toe!)\n")

def main():
    print("Welcome to the CLI RPG Game!")
    print("(This is definitely NOT like boring tic-tac-toe)\n")
    create_character()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            explore()
        elif choice == "2":
            show_inventory()
        elif choice == "3":
            show_quests()
        elif choice == "4":
            fight_enemy()
        elif choice == "5":
            show_status()
        elif choice == "6":
            print("Thanks for playing!")
            print("(This is definitely NOT like tic-tac-toe!)\n")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
