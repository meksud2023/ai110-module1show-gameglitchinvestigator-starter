# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Purpose:** A Streamlit number-guessing game — guess the secret number within a limited number of tries, using higher/lower hints.
- [x] **Bugs found:** Hints were inverted, the game was impossible to win, out-of-range guesses were allowed, and "New Game" didn't fully reset.
- [x] **Fixes applied:** Rewrote `check_guess` as a clean int comparison (no string conversion), corrected the hint text, enforced the guess range, reset all state on "New Game", refactored the logic into `logic_utils.py`, and added passing tests.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. <!--  User enters a guess of 23 -->
2. <!-- Game returns "Go HIGHER!" -->
3. <!-- User enters a guess of 80 → "Too High" -->
4. <!-- Game returns "Go LOWER!" --> 
5. <!--  Score updates correctly after each guess -->

6. <!--  Game ends after the correct guess >
**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
$ pytest tests/ -v
============================= test session starts =============================
platform win32 -- Python 3.10.1, pytest-9.0.3, pluggy-1.6.0
collected 6 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 16%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 33%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 50%]
tests/test_game_logic.py::test_too_high_hint PASSED                      [ 66%]
tests/test_game_logic.py::test_hints_are_not_inverted PASSED             [ 83%]
tests/test_game_logic.py::test_check_guess_returns_plain_string PASSED   [100%]

============================== 6 passed in 0.02s =============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
