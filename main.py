import random

class Player:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.health = 100
        self.level = 1
        self.experience = 0
        
    def attack(self):
        damage = random.randint(10, 25)
        return damage
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0


def main():
    print("Welcome to the RPG Game CLI!")
    print("============================")
    
    name = input("Enter your character's name: ")
    
    print("Choose your class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        character_class = "Warrior"
    elif choice == "2":
        character_class = "Mage"
    elif choice == "3":
        character_class = "Rogue"
    else:
        character_class = "Adventurer"
        
    player = Player(name, character_class)
    
    print(f"\nWelcome, {player.name} the {player.character_class}!")
    print(f"You have {player.health} health.")
    
    # Simple game loop
    while player.health > 0:
        print("\nWhat would you like to do?")
        print("1. Explore")
        print("2. Rest")
        print("3. Quit")
        
        action = input("Enter your choice (1-3): ")
        
        if action == "1":
            print("You explore the area...")
            encounter = random.choice(["monster", "treasure", "nothing"])
            
            if encounter == "monster":
                print("You encountered a monster!")
                damage = random.randint(5, 20)
                player.take_damage(damage)
                print(f"You took {damage} damage. Health: {player.health}")
            elif encounter == "treasure":
                print("You found some treasure!")
                heal = random.randint(10, 30)
                player.health += heal
                print(f"You healed for {heal} health. Health: {player.health}")
            else:
                print("You found nothing of interest.")
                
        elif action == "2":
            print("You rest and recover some health.")
            heal = random.randint(5, 15)
            player.health += heal
            print(f"You healed for {heal} health. Health: {player.health}")
            
        elif action == "3":
            print("Thanks for playing!")
            break
        
        else:
            print("Invalid choice. Please try again.")
            
        if player.health <= 0:
            print("\nGame Over! You have been defeated.")
            break

if __name__ == "__main__":
    main()