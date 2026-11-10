from dice import Dice


class Weapon: 

    def __init__(self, name: str, damage_dice: Dice) -> None:
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
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
    print(min(rolls), max(rolls))   # expected: 1 8
