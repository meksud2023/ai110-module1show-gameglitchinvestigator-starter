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

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
