print("Fill in the missing word!")
print("")

print("My potato, my Potato. My little _____ Potato.")
answer = "buddy"

guess = input("Fill in the blank: ").strip().lower()

if guess == answer:
    print("Correct! what a big boy")
else:
    print(f"The correct word was '{answer}' little potato.")