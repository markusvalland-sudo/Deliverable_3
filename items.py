# Items module - Deliverable 3, Task 3

from dice import Dice


class Weapon:
    """Represents a weapon that deals damage based on a dice roll"""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialise the Weapon

        Args:
            name (str): The name of the weapon
            damage_dice (Dice): The dice used to calculate damage
        """
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Roll the weapon's damage dice and return the damage dealt"""
        return self.damage_dice.roll()

    def __repr__(self) -> str:
        """Representation of weapon object, e.g. Weapon(name=Sword, damage_dice=Dice(sides=8))"""
        return f"Weapon(name={self.name}, damage_dice={self.damage_dice})"


if __name__ == "__main__":
    # Quick tests for Task 3 - run with: python items.py
    sword = Weapon("Sword", Dice(sides=8))

    print(sword)                 # expected: Weapon(name=Sword, damage_dice=Dice(sides=8))
    print(sword.roll_damage())   # expected: a number from 1 to 8

    rolls = [sword.roll_damage() for _ in range(1000)]
    print(min(rolls), max(rolls))   # expected: 1 8"




  