import random

def load_words():
    # Load from the word list file
    with open("wordle_words.txt") as f:
        return [word.strip().lower() for word in f if len(word.strip()) == 5]

def check_guess(guess, secret):
    result = ""
    correct = []
    misplaced = []

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            result += "🟩"
            correct.append(guess[i])
        elif guess[i] in secret:
            result += "🟨"
            misplaced.append(guess[i])
        else:
            result += "⬛"
    return result, correct, misplaced

def wordle():
    WORDS = load_words()
    secret = random.choice(WORDS)
    attempts = 6

    print("Welcome to Wordle!")
    print("Guess the 5-letter word. You have 6 attempts.")

    for turn in range(attempts):
        guess = input(f"\nAttempt {turn+1}/{attempts}: ").lower()
        
        if guess not in WORDS:
            print("❌ Not a valid word from the list.")
            continue

        feedback, correct, misplaced = check_guess(guess, secret)
        print("Result:", feedback)

        if correct:
            print("✅ Correct letters in the right spot:", ", ".join(correct))
        if misplaced:
            print("⚠️ Correct letters but wrong spot:", ", ".join(misplaced))

        if guess == secret:
            print("🎉 You got it!")
            return

    print(f"😢 Out of attempts! The word was: {secret}")

if __name__ == "__main__":
    wordle()
