# Exercism Python Track — My Solutions

My solutions to exercises from the [Exercism Python track](https://exercism.org/tracks/python).

This is a living repository: I add solutions as I progress through the track. Each exercise lives in its own directory together with the official test suite it passes.

## Exercises

| Exercise | Concepts practised |
| --- | --- |
| [Armstrong Numbers](./armstrong-numbers) | Loops, exponentiation, numbers |
| [Black Jack](./black-jack) | Comparison operators, conditionals |
| [Card Games](./card-games) | Lists, indexing, slicing |
| [Cater-Waiter](./cater-waiter) | Sets (`set`, `&`, `<=`, `-`, `set.union`) |
| [Chaitana's Colossal Coaster](./chaitanas-colossal-coaster) | List methods (`append`, `insert`, `remove`, …) |
| [Collatz Conjecture](./collatz-conjecture) | While loops, conditionals, modulo arithmetic |
| [Currency Exchange](./currency-exchange) | Numbers (`int`, `float`), arithmetic |
| [Ellen's Alien Game](./ellens-alien-game) | Classes, class attributes, instance methods |
| [Ghost Gobble Arcade Game](./ghost-gobble-arcade-game) | Booleans, logical operators |
| [Grains](./grains) | Exponentiation (`2**n`), raising exceptions, integer arithmetic |
| [Inventory Management](./inventory-management) | Dictionaries, creating and updating entries |
| [Leap](./leap) | Conditionals, modulo arithmetic |
| [Little Sister's Essay](./little-sisters-essay) | String methods |
| [Little Sister's Vocab](./little-sisters-vocab) | Strings, concatenation, slicing |
| [Locomotive Engineer](./locomotive-engineer) | Unpacking (`*args`, `**kwargs`, `*` in assignments) |
| [Making the Grade](./making-the-grade) | Loops (`for`, `while`), `break`/`continue` |
| [Mecha-Munch Management](./mecha-munch-management) | Dict methods (`\|=`, `sorted()`, `.items()`) |
| [Meltdown Mitigation](./meltdown-mitigation) | Conditionals, control flow |
| [Plane Tickets](./plane-tickets) | Generators (`yield`, generator functions) |
| [Tisbury Treasure Hunt](./tisbury-treasure-hunt) | Tuples, unpacking |
| [Triangle](./triangle) | Functions, conditionals, sets |

## Repository layout

```
<exercise-name>/
├── <solution>.py        # my solution
└── <solution>_test.py   # the Exercism test suite
```

## Running the tests

All solutions are verified against the official Exercism test suites using [pytest](https://docs.pytest.org/):

```bash
# from the repository root
python -m venv .venv
source .venv/bin/activate
pip install pytest

# run all tests
pytest

# or a single exercise
pytest black-jack/
```

## About Exercism

[Exercism](https://exercism.org) is a free, open-source platform for learning programming languages through small, test-driven exercises with community mentoring. The Python track covers the language from core syntax up to more advanced concepts. Thanks to the communit for such an amazing free resource!
