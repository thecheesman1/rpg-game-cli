import random

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        
    def attack(self, attacker, defender):
        # Calculate damage with some randomness
        base_damage = attacker['attack']
        damage_variance = random.randint(-5, 5)
        actual_damage = max(1, base_damage + damage_variance)
        defender['health'] -= actual_damage
        return actual_damage
    
    def player_attack(self):
        return self.attack(self.player, self.enemy)
    
    def enemy_attack(self):
        return self.attack(self.enemy, self.player)
    
    def is_player_alive(self):
        return self.player['health'] > 0
    
    def is_enemy_alive(self):
        return self.enemy['health'] > 0
    
    def battle(self):
        print(f"A wild {self.enemy['name']} appears!")
        while self.is_player_alive() and self.is_enemy_alive():
            print(f"\n{self.player['name']}: {self.player['health']} HP")
            print(f"{self.enemy['name']}: {self.enemy['health']} HP")
            
            damage = self.player_attack()
            print(f"{self.player['name']} attacks {self.enemy['name']} for {damage} damage!")
            
            if self.is_enemy_alive():
                damage = self.enemy_attack()
                print(f"{self.enemy['name']} attacks {self.player['name']} for {damage} damage!")
        
        if self.is_player_alive():
            print(f"{self.player['name']} defeated {self.enemy['name']}!")
        else:
            print(f"{self.player['name']} was defeated by {self.enemy['name']}!")
