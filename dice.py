import random

class Dice:
    """Represents an n-sided dice (n >= 2)"""

    def __init__(self, sides: int = 6) -> None:
        """
        Initialise the Dice

        Args:
            sides (int): Number of sides on the dice (default = 6, must be >= 2)
        """
        if sides < 2: 
            raise ValueError("A dice must atleast have 2 sides")
        self.sides = sides
    
    # ------------------------------------------------------------------
    # Task 2a: roll()
    # ------------------------------------------------------------------
    def roll(self) -> int:
        """Roll the dice and return a random number between 1 and sides"""
        return random.randint(1, self.sides)

    # ------------------------------------------------------------------
    # Task 2b: __repr__
    # ------------------------------------------------------------------
    def __repr__(self) -> str:
        """Representation of dice object, e.g. Dice(sides=6)"""
        return f"Dice(sides={self.sides})"

    # ------------------------------------------------------------------
    # Task 2c: __call__ - makes d20() do the same as d20.roll()
    # ------------------------------------------------------------------
    def __call__(self) -> int:
        """Roll the dice when the object is called like a function"""
        return self.roll()
    
if __name__ == "__main__":
    # Quick tests for Task 2 - run with: python dice.py
    d6 = Dice()
    d20 = Dice(sides=20)

    print(repr(d6))          # expected: Dice(sides=6)
    print(d20)               # expected: Dice(sides=20)  (print uses __repr__ when there is no __str__)

    print(d6.roll())         # expected: a number from 1 to 6
    print(d20())             # expected: a number from 1 to 20  (uses __call__)

    # Roll many times and check that all results are within range
    rolls = [d6.roll() for _ in range(1000)]
    print(min(rolls), max(rolls))   # expected: 1 6
    print(sorted(set(rolls)))       # expected: [1, 2, 3, 4, 5, 6]

    try:
        Dice(sides=1)        # should fail, a dice needs at least 2 sides
    except ValueError:
        print("OK: Dice with fewer than 2 sides rejected")

