# Python Wordle Game 🎮

A simple Wordle-style game built with Python.

## Features
- Randomly selects a 5-letter word from a word list (`wordle_words.txt`).
- You have 6 attempts to guess the word.
- Feedback is given after each guess:
  - 🟩 = Correct letter in the correct spot
  - 🟨 = Correct letter in the word but wrong spot
  - ⬛ = Letter not in the word
- Shows which letters are correct and misplaced after each guess.

## Setup
1. Make sure you have Python 3 installed.
2. Download the following files into the same folder:
   - `wordle.py` (the game code)
   - `wordle_words.txt` (the word list)
3. Run the game with:

```bash
python wordle.py
```

## Example Gameplay

```
Welcome to Wordle!
Guess the 5-letter word. You have 6 attempts.

Attempt 1/6: apple
Result: 🟩⬛🟨⬛⬛
✅ Correct letters in the right spot: a
⚠️ Correct letters but wrong spot: p

Attempt 2/6: apart
Result: 🟩⬛🟩⬛⬛
✅ Correct letters in the right spot: a, a
```

## Custom Word List
You can edit `wordle_words.txt` to add or remove words. Just make sure they are all **5 letters** long.

---

Enjoy playing! 🎉
