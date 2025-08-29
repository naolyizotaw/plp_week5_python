class Animal:
    """Base class for all animals."""
    
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat
    
    def move(self):
        """Base move method - to be overridden by subclasses."""
        print(f"{self.name} moves in a generic way.")
    
    def speak(self):
        """Base speak method."""
        print(f"{self.name} makes a sound.")


class Bird(Animal):
    """A bird that can fly."""
    
    def __init__(self, name, habitat, wingspan):
        super().__init__(name, habitat)
        self.wingspan = wingspan
    
    def move(self):
        print(f"{self.name} is flying through the air! 🕊️")
    
    def speak(self):
        print(f"{self.name} says: Tweet tweet! 🎵")


class Fish(Animal):
    """A fish that can swim."""
    
    def __init__(self, name, habitat, fin_count):
        super().__init__(name, habitat)
        self.fin_count = fin_count
    
    def move(self):
        print(f"{self.name} is swimming in the water! 🐠")
    
    def speak(self):
        print(f"{self.name} says: Blub blub! 💦")


class Mammal(Animal):
    """A mammal that can run."""
    
    def __init__(self, name, habitat, leg_count):
        super().__init__(name, habitat)
        self.leg_count = leg_count
    
    def move(self):
        print(f"{self.name} is running on the ground! 🐾")
    
    def speak(self):
        print(f"{self.name} says: Grrr! 🐯")


# Demonstration function showing polymorphism
def demonstrate_movement(animals):
    """Demonstrate polymorphism by making different animals move."""
    print("\n" + "="*50)
    print("POLYMORPHISM DEMONSTRATION! 🎭")
    print("="*50)
    
    for animal in animals:
        animal.move()
        animal.speak()
        print("-" * 30)


# Main program to test everything
if __name__ == "__main__":
    print("SUPERHERO CLASS DEMONSTRATION! 🦸")
    print("="*50)
    
    # Create superhero instances
    iron_man = TechHero(
        "Iron Man", 
        "Tony Stark", 
        ["Flight", "Repulsor Beams", "AI Assistance"], 
        85,
        ["Arc Reactor", "Repulsors", "Jarvis AI"]
    )
    
    doctor_strange = MagicHero(
        "Doctor Strange", 
        "Stephen Strange", 
        ["Magic", "Time Manipulation", "Portal Creation"], 
        90,
        100
    )
    
    superman = Superhero(
        "Superman", 
        "Clark Kent", 
        ["Flight", "Super Strength", "Heat Vision", "X-Ray Vision"], 
        95
    )
    
    # Test superhero methods
    print(iron_man)
    iron_man.use_power("Flight")
    iron_man.use_gadget("Repulsors")
    iron_man.go_on_mission(30)
    
    print(f"\n{doctor_strange}")
    doctor_strange.cast_spell("Time Manipulation", 40)
    doctor_strange.meditate()
    
    print(f"\n{superman}")
    superman.use_power("Heat Vision")
    superman.reveal_identity()
    
    # Test polymorphism with animals
    animals = [
        Bird("Eagle", "Mountains", 2.1),
        Fish("Salmon", "Rivers", 7),
        Mammal("Lion", "Savannah", 4),
        Bird("Sparrow", "Cities", 0.3),
        Fish("Shark", "Ocean", 8),
        Mammal("Cheetah", "Grasslands", 4)
    ]
    
    demonstrate_movement(animals)