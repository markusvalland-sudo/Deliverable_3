# Battle module - Deliverable 3, Task 5

from character import Character


class Battle:
    """Manages turn-based combat between two characters"""

    def __init__(self, hero: Character, enemy: Character) -> None:
        """Initialise a battle between two characters"""
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """Play one round: hero attacks first, then enemy attacks if still alive"""
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> Character:
        """Run rounds until one character is no longer alive, and return the winner"""
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()
        return self.hero if self.hero.is_alive else self.enemy


if __name__ == "__main__":
    # Quick tests for Task 5 - run with: python battle.py
    from character import Warrior, Mage
    from dice import Dice
    from items import Weapon

    hero = Warrior("Wenche", weapon=Weapon("Sword", Dice(sides=12)))
    enemy = Mage("Geir Eskil")

    winner = Battle(hero, enemy).simulate_battle()
    print(f"Winner: {winner.name}")
    print(f"{hero.name}: {hero.hp} HP, {enemy.name}: {enemy.hp} HP")
    # expected: one of them has 0 HP, the other has more than 0

        # Battle without weapons
    hero2 = Warrior("Jørgen")
    enemy2 = Mage("Markus")
    winner2 = Battle(hero2, enemy2).simulate_battle()
    print(f"Without weapons - Winner: {winner2.name}")
    print(f"{hero2.name}: {hero2.hp} HP, {enemy2.name}: {enemy2.hp} HP")