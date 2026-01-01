import random

def get_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "You win"
    else:
        return "Computer wins"


def main():
    choices = ["rock", "paper", "scissors"]

    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Learn to type properly.")
        return

    computer_choice = random.choice(choices)

    print(f"Computer chose: {computer_choice}")

    result = get_winner(user_choice, computer_choice)
    print(result)


if __name__ == "__main__":
    main()