from items import Weapon


class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10,
                weapon: Weapon | None = None ) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage dealt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicates private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon


    # ------------------------------------------------------------------
    # Task 1a: take_damage()
    # ------------------------------------------------------------------
    def take_damage(self, amount: int) -> None:
        """
        Reduce this character's own HP by `amount`.
        HP can never go below 0.

        Args:
            amount (int): Damage to take (must be >= 0)
        """
        if amount < 0:
            raise ValueError("Damage amount can not be negative")
        self._hp = max(self._hp - amount, 0) 

    # ------------------------------------------------------------------
    # Task 1b: heal()
    # ------------------------------------------------------------------
    def heal(self, amount: int) -> None:
        """
        Increase this character's own HP by `amount`.
        HP can never go above hp_max.

        Args:
            amount (int): HP to restore (must be >= 0)
        """
        if amount < 0:
            raise ValueError("Heal amount can not be negative")
        self._hp = min(self._hp + amount, self.hp_max)


    # ------------------------------------------------------------------
    # Task 1c: attack() - must NOT touch target._hp directly
    # ------------------------------------------------------------------
    def attack(self, target: "Character") -> None:
        """Attack and deal damage to target character"""
        if self.weapon is not None:
            dmg = self.weapon.roll_damage()
        else:
            dmg = self.damage
        target.take_damage(dmg)

    # ------------------------------------------------------------------
    # Task 1d: is_alive (read-only property)
    # ------------------------------------------------------------------
    @property 
    def is_alive(self) -> bool:
        """True if the character has more than 0 HP, otherwise False"""
        return self.hp > 0 

    # ------------------------------------------------------------------
    # Unchanged from lecture (except the repr bug fix)
    # ------------------------------------------------------------------
    def introduce(self) -> None:
        """Prints a string that introduces the character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp


if __name__ == "__main__":
    # Quick tests for Task 1 - run with: python character.py
    a = Character("Arne")
    b = Character("Bjorg", hp_max=15)

    a.attack(b)
    print(b.hp, b.is_alive)  # expected: 5 True

    a.attack(b)
    print(b.hp, b.is_alive)  # expected: 0 False  (not -5!)

    b.heal(100)
    print(b.hp)              # expected: 15  (not 115!)

    try:
        b.is_alive = True    # should fail, property is read-only
    except AttributeError:
        print("OK: is_alive is read-only")

    try:
        b.take_damage(-5)    # should fail, negative damage not allowed
    except ValueError:
        print("OK: negative damage rejected")

    # Tests for Task 3
    from dice import Dice

    sword = Weapon("Sword", Dice(sides=8))
    c = Character("Cecilie", weapon=sword)
    d = Character("Dag")

    c.attack(d)
    print(d.hp)        # expected: between 92 and 99 (weapon: 1-8 damage)

    d.attack(c)
    print(c.hp)        # expected: 90 (no weapon: base damage 10)

       




