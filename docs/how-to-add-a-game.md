# How to add a game

**This is the best first contribution in the repository.** You write one new
file, add one line to a list, and you are done. You do not need to understand
any other part of the codebase.

Time: about 20–30 minutes.

The walkthrough uses Coin Flip as its worked example. Coin Flip is already in
the arcade (`arcade/games/coinflip.py`, and you can read it for reference), so
for your own pull request follow the same steps with your game's name in place
of `coinflip`.

---

## The idea

Every game is a single file in `arcade/games/`. A file becomes a game when it
provides three things:

| Name | What it is |
|---|---|
| `NAME` | The title shown in the menu |
| `DESCRIPTION` | One line under the title |
| `play()` | A function that runs the game and returns a score |

That is the entire contract. Nothing else in the project needs to know what
your game does.

---

## Step by step

### 1. Claim an issue

Find one labelled `good first issue` that is not marked `status: claimed`,
and comment `/claim`. A bot assigns it to you.

### 2. Fork, clone, branch

```bash
git clone https://github.com/YOUR-USERNAME/terminal-arcade.git
cd terminal-arcade
git checkout -b feat/coin-flip-game
```

### 3. Create your file

Create `arcade/games/coinflip.py`. Here is a complete, working game you can
start from — copy it, then change it into yours:

```python
"""Coin Flip.

Call heads or tails. Get it right three times in a row to win.
"""

from __future__ import annotations

import random

from arcade import art
from arcade.input_utils import ask_choice

NAME = "Coin Flip"
DESCRIPTION = "Call it right three times in a row"

ROUNDS = 3


def flip() -> str:
    """Flip a coin. Returns "heads" or "tails"."""
    return random.choice(["heads", "tails"])


def play() -> int:
    """Run one game of Coin Flip.

    Returns:
        The player's score. 0 if they got one wrong.
    """
    print(art.banner("COIN FLIP"))
    print(f"\n  Call it right {ROUNDS} times in a row.\n")

    for round_number in range(1, ROUNDS + 1):
        call = ask_choice(f"  Round {round_number} — heads or tails?", ["heads", "tails"])
        result = flip()
        print(f"  The coin lands on {art.bold(result)}.")

        if call != result:
            print(art.red(f"\n  Wrong. You got {round_number - 1} in a row.\n"))
            return 0

        print(art.green("  Correct.\n"))

    print(art.green(f"  {ROUNDS} in a row. Very nice.\n"))
    return ROUNDS * 30
```

### 4. Register it

Open `arcade/main.py`. Two small edits:

```python
# add your module to this import line
from arcade.games import coinflip, guess, hangman, yourgame, rps, tictactoe

GAMES: list[ModuleType] = [
    guess,
    hangman,
    rps,
    tictactoe,
    coinflip,
    yourgame,  # <- add your module here
]
```

### 5. Play it

```bash
python3 -m arcade
```

Your game should appear in the menu. Play it through at least twice — once
winning, once losing.

### 6. Add a test

Create `tests/test_coinflip.py`. Test the *logic*, not the printing:

```python
"""Tests for Coin Flip."""

from arcade.games import coinflip


def test_flip_returns_heads_or_tails():
    for _ in range(50):
        assert coinflip.flip() in ("heads", "tails")


def test_the_game_has_a_name_and_description():
    assert coinflip.NAME
    assert coinflip.DESCRIPTION
```

Run it:

```bash
python3 -m pytest
```

### 7. Open the pull request

```bash
git add arcade/games/coinflip.py arcade/main.py tests/test_coinflip.py
git commit -m "feat: add Coin Flip game

Closes #<issue number>"
git push origin feat/coin-flip-game
```

Then open the PR on GitHub and fill in the template. **Paste a snippet of your
terminal output** showing the game being played — reviewers love that and it
gets your PR merged faster.

---

## House rules for games

- **Standard library only.** No `pip install`. Use `random`, `time`, `math` —
  that is plenty
- **Use the input helpers.** `ask`, `ask_int`, `ask_choice`, `ask_letter` from
  `arcade.input_utils`, not bare `input()`. They handle invalid answers for you
- **Use `arcade.art` for colour**, not raw escape codes — it turns colour off
  automatically when output is piped
- **`play()` must return a number.** Higher is better. Return 0 for a loss
- **`play()` must always end.** No `while True` without a way out
- **Keep it under about 150 lines.** If it is longer, it may be too ambitious
  for a first PR
- **Write docstrings.** Look at `arcade/games/guess.py` for the style

## Ideas that are not claimed yet

Rock Paper Scissors Lizard Spock · Higher or Lower (with cards) · Simon Says
(with a sequence you type back) · Anagram Hunt · Countdown Numbers · Nim ·
Mastermind. Check the open issues first, since some of these may already have
an owner.

Do not see yours? Open a **Feature request** issue and propose it.

---

## If you get stuck

1. Read `arcade/games/guess.py` — it is the simplest game and does everything
   yours needs to
2. Comment on your issue. Genuinely, ask. That is not a failure
3. Bring your branch to a PR Debug Clinic if your community is running one

The first pull request is the hardest one you will ever make. Everything after
this is easier.
