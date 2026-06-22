# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  The hints were not reliable, for example, the hint displays go lower for input 4 even though the secrete was 100. 
  The range are not restricted, for example for range 1 to 100, it says go higher for input 100, and it will allows you to enter > 100.




**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guess of 6 | "Go LOWER!" | "Go HIGHER!" | none |
| guess of 0 | "Range enforced" | "Go LOWER!" | none |
| guess too high on an even attempt (e.g. 90 when secret is 40) | wrong guess → score should drop or stay the same | score increased by 5 | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used an AI coding assistant (Claude Code in agent mode inside VS Code) as a debugging partner. I described the symptoms I saw while playing, the hints pointing the wrong way and never being able to win, and the AI traced the logic back to the root cause and applied the fixes while I reviewed each change.

**A correct suggestion:** The AI identified that the secret was being converted to a string on even attempts, which broke the comparison in `check_guess`, and it rewrote the function as a clean integer comparison that returns a single outcome string. I verified this by running `pytest` (all 6 tests passed, including the regression test for the inverted hint) and by confirming in the app that a guess above the secret now correctly says "Go LOWER."

**A misleading suggestion:** The AI first reported that all tests passed, but it had run them with `python -m pytest`. When I ran plain `pytest` myself, the command the instructions asked for, I got `ModuleNotFoundError: No module named 'logic_utils'`. The "all tests pass" claim was misleading because the launch command was quietly adding the project root to the import path and hiding a real problem. I verified the issue by reproducing it in my own terminal, and we fixed it by adding a `conftest.py` so the import works no matter how pytest is launched.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was really fixed by checking it two ways: running the automated tests and then playing the game in the browser to see the behavior with my own eyes. A bug only counted as fixed when both agreed — for example, the hint bug was only "done" once `pytest` passed and a guess above the secret actually told me to go LOWER in the app.

The most useful test I ran was `pytest tests/`, which showed 6 passing tests. The regression test, `test_hints_are_not_inverted`, that checks several guesses above the secret return "Too High" and several below return "Too Low." This mattered because the same test would have *failed* on the original broken code (which returned a tuple and swapped the hints), so a green result proves the fix actually addresses that specific bug rather than just happening to pass.

AI helped me both design and understand the tests. It suggested the regression test that pins the hint direction and explained why a good test should fail on the old code, not just pass on the new code. It also helped me understand a confusing `ModuleNotFoundError` — it explained that `pytest` wasn't adding the project root to the import path, and we fixed it by adding a `conftest.py`.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I'd explain it like this: every time you interact with a Streamlit app — clicking a button, typing in a box — Streamlit re-runs the *entire* script from top to bottom, like refreshing a page. That means any normal variable gets reset to its starting value on every click, which is why the secret number kept "resetting" and the game felt glitchy. `st.session_state` is Streamlit's memory box that survives those reruns: anything you store there (the secret, the score, the attempt count) stays put between clicks. The big lesson for me was that in Streamlit you have to be deliberate about what lives in session state versus what gets recalculated, because the script running again is the normal behavior, not a bug.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to keep is writing a regression test for every bug I fix, a test that would have failed on the broken code, so I can prove the fix works and catch it if it ever breaks again. The thing I'd do differently next time is to run the tests myself instead of trusting the AI's "all tests pass," because I learned that the exact command matters (`pytest` vs. `python -m pytest` gave different results and hid a real import bug). Overall, this project changed how I think about AI-generated code: it can write a lot of confident, professional-looking code that is quietly broken, so I now treat AI output as a draft to verify and test, not as a finished answer to trust.
