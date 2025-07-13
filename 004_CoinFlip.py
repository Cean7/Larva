import random

print("Coin Flip, Heads or Tails? h or t: ")

choice = input("Your guess: ").lower()
flip = random.choice(['h', 't'])

if choice == flip:
    print("Correct little bug!")
else:
    print(f"Wrong! It was {'heads' if flip == 'h' else 'tails'} hahaha!.")