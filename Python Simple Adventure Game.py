

def intro(player_name):
    print(f"\nWelcome, {player_name}, to the Enchanted Forest!")
    print("A hidden treasure is said to be deep within...")
    print("But beware of the dangers ahead!\n")

def choose_path():
    print("You see two paths:")
    print("1. A dark trail into the woods.")
    print("2. A bright path along a river.")
    choice = input("Which path do you take? (1 or 2): ")
    return choice

def forest_path():
    print("\nYou walk into the dark forest.")
    print("Suddenly, you hear growling behind you!")
    action = input("Do you RUN or HIDE? ").lower()
    if action == "run":
        print("You run fast and escape safely!")
        return True
    elif action == "hide":
        print("You hide behind a tree. The creature passes by.")
        return True
    else:
        print("You freeze in fear. The creature finds you. Game Over.")
        return False

def river_path():
    print("\nYou follow the river path and find a small boat.")
    action = input("Do you take the BOAT or WALK along the river? ").lower()
    if action == "boat":
        print("The boat carries you to a cave with treasure inside!")
        return True
    elif action == "walk":
        print("You slip into the river, but swim to safety.")
        return True
    else:
        print("You wait too long. Something bites you. Game Over.")
        return False

def play_game():
    player_name = input("Enter your name, adventurer: ")
    intro(player_name)

    while True:
        path = choose_path()
        if path == "1":
            survived = forest_path()
        elif path == "2":
            survived = river_path()
        else:
            print("Invalid choice. Try again.")
            continue

        if survived:
            print(f"\nWell done, {player_name}! You survived the adventure.")
        else:
            print(f"\nSorry, {player_name}. Your adventure ends here.")

        play_again = input("\nDo you want to play again? (yes or no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break

play_game()
