import random

bugs = ['caterpillar', 'beetle', 'moth', 'larva', 'dragonfly', 'butterfly', 'ant', 'termite']

def scramble(word):
    return ''.join(random.sample(word, len(word)))

print("🐛 Welcome to GUESS THE BUG!")
score = 0

while True:
    word = random.choice(bugs)
    puzzle = scramble(word)
    print(f"\nGuess this bug: {puzzle}")

    guess = input("Your guess (or 'q' to quit): ").lower()
    
    if guess == 'q':
        print(f"Thanks for playing! Your score: {score}")
        break
    elif guess == word:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The answer was: {word}")