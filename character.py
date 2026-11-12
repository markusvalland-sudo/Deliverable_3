

from items import Weapon


class Character:
    """Represents a character in the RPG"""

    # ------------------------------------------------------------------
    # Task 3: From lecture, updated in task 3
    # ------------------------------------------------------------------
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10,
                 weapon: Weapon | None = None) -> None: 
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Base damage dealt when attacking without a weapon (default = 10)
            weapon (Weapon | None): Equipped weapon (default = None)
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
    # Task 1c + Task 3: attack() - uses take_damage(), and weapon if equipped
    # ------------------------------------------------------------------
    def attack(self, target: "Character") -> None:
        """Attack target, using weapon damage if a weapon is equipped"""
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


# ----------------------------------------------------------------------
# Task 4a: Warrior subclass (defensive specialist)
# ----------------------------------------------------------------------
class Warrior(Character):
    """A defensive character whose armor reduces incoming damage"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10,
                 weapon: Weapon | None = None, armor: int = 5) -> None:
        """
        Initialise the Warrior

        Args:
            name, hp_max, damage, weapon: Same as Character
            armor (int): Reduces all incoming damage by this amount (default = 5)
        """
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor

    def take_damage(self, amount: int) -> None:
        """Reduce incoming damage by armor before applying it (never below 0)"""
        if amount < 0:
            raise ValueError("Damage amount can not be negative")
        reduced = max(amount - self.armor, 0)
        super().take_damage(reduced)

#---------------------------------------------------------------------------
#Task 4b: Mage subclass (resocurce based attacker)
#---------------------------------------------------------------------------
class Mage(Character):
    """A magic user who spends mana on powerful spell attacks"""

    SPELL_COST = 10     # mana needed for one spell
    MANA_REGEN = 5      # mana restored after a base attack

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10,
                 weapon: Weapon | None = None, mana_max: int = 30) -> None:
        """
        Initialise the Mage

        Args:
            name, hp_max, damage, weapon: Same as Character
            mana_max (int): Maximum mana (default = 30). The mage starts with full mana.
        """
        super().__init__(name, hp_max, damage, weapon)
        self.mana_max = mana_max
        self.mana = mana_max

    def attack(self, target: "Character") -> None:
        """
        Cast a spell if enough mana, otherwise do a base attack.

        - mana >= 10: spend 10 mana, deal double base damage (ignores weapon)
        - mana < 10: normal attack (uses weapon if equipped), restore 5 mana
        """
        if self.mana >= self.SPELL_COST:
            self.mana -= self.SPELL_COST
            target.take_damage(self.damage * 2)
        else:
            super().attack(target)
            self.mana = min(self.mana + self.MANA_REGEN, self.mana_max)
   


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

    sword = Weapon("Sword", Dice(sides=20))
    c = Character("Cecilie", weapon=sword)
    d = Character("Dag")

    c.attack(d)
    print(d.hp)        # expected: between 92 and 99 (weapon: 1-8 damage)

    d.attack(c)
    print(c.hp)        # expected: 90 (no weapon: base damage 10)

    # Tests for Task 4a
    w = Warrior("Wenche")
    a.attack(w)            # Arne: 10 damage, minus 5 armor
    print(w.hp)            # expected: 95

    weak = Character("Weak", damage=3)
    weak.attack(w)         # 3 damage, minus 5 armor -> 0
    print(w.hp)            # expected: 95 (armor blocks everything)

        # Tests for Task 4b
    m = Mage("Mia")
    t = Character("Target")
    for i in range(6):
        m.attack(t)
        print(f"Attack {i + 1}: target hp={t.hp}, mana={m.mana}")

    staff = Weapon("Staff", Dice(sides=20))
    m2 = Mage("Geir Eskil", weapon=staff, mana_max=10)
    t2 = Character("Target2")
    m2.attack(t2)
    print(t2.hp)       # expected: 80 (spell: 2 x 10, staff not used)
    m2.attack(t2)
    print(t2.hp)       # expected: between 76 and 79 (base attack with staff: 1-4)