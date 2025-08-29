class Superhero:
    """A class representing a superhero with unique powers and abilities."""
    
    def __init__(self, name, secret_identity, powers, strength_level, is_alive=True):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers  # List of powers
        self.strength_level = strength_level  # Scale of 1-100
        self.is_alive = is_alive
        self.mission_count = 0
    
    def use_power(self, power_name):
        """Use a specific power if the hero has it."""
        if power_name in self.powers:
            print(f"{self.name} uses {power_name}! ⚡")
            return True
        else:
            print(f"{self.name} doesn't have the power: {power_name}")
            return False
    
    def go_on_mission(self, mission_difficulty):
        """Send the hero on a mission, affecting their strength."""
        if not self.is_alive:
            print(f"{self.name} cannot go on missions - hero is retired! 😢")
            return False
        
        success_chance = min(90, self.strength_level - mission_difficulty + 50)
        success = success_chance > 60
        
        if success:
            print(f"Mission successful! {self.name} saved the day! 🎉")
            self.mission_count += 1
            self.strength_level -= mission_difficulty * 0.1
        else:
            print(f"Mission failed! {self.name} needs to recover. 💔")
            self.strength_level -= mission_difficulty * 0.2
        
        return success
    
    def recover(self):
        """Recover strength through rest."""
        recovery = min(20, 100 - self.strength_level)
        self.strength_level += recovery
        print(f"{self.name} recovered {recovery} strength points! 💪")
    
    def reveal_identity(self):
        """Reveal the hero's secret identity."""
        print(f"{self.name}'s secret identity is: {self.secret_identity} 🎭")
    
    def __str__(self):
        return f"{self.name} (Strength: {self.strength_level}, Powers: {len(self.powers)}, Missions: {self.mission_count})"


# Inheritance layer - Specialized superhero types
class TechHero(Superhero):
    """A superhero who relies on technology and gadgets."""
    
    def __init__(self, name, secret_identity, powers, strength_level, gadgets, is_alive=True):
        super().__init__(name, secret_identity, powers, strength_level, is_alive)
        self.gadgets = gadgets  # List of gadgets
        self.energy_level = 100
    
    def use_gadget(self, gadget_name):
        """Use a specific gadget."""
        if gadget_name in self.gadgets:
            print(f"{self.name} uses {gadget_name}! 🤖")
            self.energy_level -= 10
            return True
        else:
            print(f"{self.name} doesn't have the gadget: {gadget_name}")
            return False
    
    def recharge(self):
        """Recharge energy for gadgets."""
        self.energy_level = 100
        print(f"{self.name}'s gadgets are fully recharged! 🔋")
    
    def go_on_mission(self, mission_difficulty):
        """Override mission method for tech heroes."""
        if self.energy_level < 20:
            print(f"{self.name} needs to recharge before going on a mission! ⚠️")
            return False
        return super().go_on_mission(mission_difficulty)


class MagicHero(Superhero):
    """A superhero with magical abilities."""
    
    def __init__(self, name, secret_identity, powers, strength_level, mana=100, is_alive=True):
        super().__init__(name, secret_identity, powers, strength_level, is_alive)
        self.mana = mana
    
    def cast_spell(self, spell_name, mana_cost):
        """Cast a magical spell."""
        if self.mana >= mana_cost:
            print(f"{self.name} casts {spell_name}! 🔮")
            self.mana -= mana_cost
            return True
        else:
            print(f"Not enough mana to cast {spell_name}! 💫")
            return False
    
    def meditate(self):
        """Regain mana through meditation."""
        self.mana = min(100, self.mana + 30)
        print(f"{self.name} meditates and regains mana! 🧘")