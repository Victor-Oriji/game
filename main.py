import random

user = input("Enter Player name: ")
print(f"Hi {user}!, Welcome to Rock Paper Scissors game.\n\
make a Selecion:\n\
R for ROCK\nP for PAPER\nS for SCISSORS")

while True:
    possible_actions = ["R", "P", "S"]

    user_action = input("Enter a choice (R, P, S): ")
    if user_action.upper() not in possible_actions:
        print(f"{user} you made a wrong move")
        continue
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action.upper()}, computer chose {computer_action}.\n")

    if user_action.upper() == computer_action.upper():
        print(f"Both players selected {user_action}. It's a tie!")
        continue
    elif user_action.upper() == possible_actions[0]:
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action.upper() == possible_actions[1]:
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action.upper() == possible_actions[2]:
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

    