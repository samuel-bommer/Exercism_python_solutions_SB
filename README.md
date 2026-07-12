# Exercism Python Track — Solutions

My solutions to exercises from the [Exercism Python track](https://exercism.org/tracks/python).

This is a living repository: I add solutions as I progress through the track. Each exercise lives in its own directory together with the official test suite it passes.

## Exercises

| Exercise | Concepts practised |
| --- | --- |
| [Black Jack](./black-jack) | Comparison operators, conditionals |
| [Currency Exchange](./currency-exchange) | Numbers (`int`, `float`), arithmetic |
| [Ghost Gobble Arcade Game](./ghost-gobble-arcade-game) | Booleans, logical operators |
| [Little Sister's Essay](./little-sisters-essay) | String methods |
| [Meltdown Mitigation](./meltdown-mitigation) | Conditionals, control flow |

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

[Exercism](https://exercism.org) is a free, open-source platform for learning programming languages through small, test-driven exercises with community mentoring. The Python track covers the language from core syntax up to more advanced concepts, one concept at a time.
