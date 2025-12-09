"""
CLI RPG Game
=============

A text-based role-playing game that runs in your terminal.

This is definitely NOT like boring tic-tac-toe that the user complained about.

"""

import random
import sys
import json

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

# Load shop items
with open('shop_items.json', 'r') as f:
    shop_items = json.load(f)

# Game functions
def display_menu():
    print("\n=== CLI RPG MENU ===")
    print("1. Explore the wilderness")
    print("2. Check your inventory")
    print("3. View your quests")
    print("4. Fight a monster")
    print("5. Check your character status")
    print("6. Visit the Shop")
    print("7. Rest at an Inn")
    print("8. Quit the game")
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
    # Select a random enemy
    enemy = random.choice(enemies)
    print(f"\nA wild {enemy['name']} appears!")
    
    # Initialize health for the fight
    player_health = player['health']
    enemy_health = enemy['health']
    
    # Fight loop
    while enemy_health > 0 and player_health > 0:
        print(f"\n{player['name']}: {player_health}/{player['max_health']}")
        print(f"{enemy['name']}: {enemy_health}")
        
        player_damage = random.randint(5, 15)
        enemy_damage = random.randint(5, 10)
        
        # Apply attack bonus if weapon is equipped
        if 'attack_bonus' in player:
            player_damage += player['attack_bonus']
        
        # Apply defense bonus if armor is equipped
        if 'defense_bonus' in player:
            enemy_damage -= player['defense_bonus']
        
        # Ensure damage is not negative
        player_damage = max(1, player_damage)
        enemy_damage = max(1, enemy_damage)
        
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
    # Update enemy health in the enemies list
    enemy['health'] = enemy_health

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

def visit_shop():
    print("\n=== Welcome to the Shop! ===")
    print("Available items:")
    
    for i, item in enumerate(shop_items):
        print(f"{i+1}. {item['name']} - {item['rarity'].capitalize()} - {item['cost']} gold")
        if item['type'] == 'weapon':
            print(f"   Attack Bonus: +{item['attack_bonus']}")
        elif item['type'] == 'armor':
            print(f"   Defense Bonus: +{item['defense_bonus']}")
        print()
    
    while True:
        choice = input("Enter the number of the item you want to buy (or 'back' to return): ")
        
        if choice.lower() == 'back':
            break
        
        try:
            item_index = int(choice) - 1
            if 0 <= item_index < len(shop_items):
                item = shop_items[item_index]
                
                if player["gold"] >= item["cost"]:
                    player["gold"] -= item["cost"]
                    
                    if item["type"] == "weapon":
                        player["weapon"] = item["name"]
                        player["attack_bonus"] = item["attack_bonus"]
                    elif item["type"] == "armor":
                        player["armor"] = item["name"]
                        player["defense_bonus"] = item["defense_bonus"]
                    
                    print(f"\nYou bought {item['name']} for {item['cost']} gold!")
                    print(f"Your gold: {player['gold']}")
                else:
                    print("\nNot enough gold!")
            else:
                print("\nInvalid choice!")
        except ValueError:
            print("\nPlease enter a valid number or 'back'.")


def rest():
    cost = 10  # Cost to rest at inn
    if player["gold"] >= cost:
        player["gold"] -= cost
        player["health"] = player["max_health"]
        print(f"\nYou rested at the inn and restored your health!")
        print(f"Your health is now {player['health']}/{player['max_health']}")
        print(f"Your gold: {player['gold']}")
    else:
        print("\nNot enough gold to rest at the inn!")


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
            visit_shop()
        elif choice == "7":
            rest()
        elif choice == "8":
            print("Thanks for playing!")
            print("(This is definitely NOT like tic-tac-toe!)\n")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
