import random


def player_choice():
    """Get the player choice - rock, paper or scissors."""

    while True:
        uChoice = input("Choose rock, paper or scissors: \n").lower()
        if uChoice in ["rock", "paper", "scissors"]:
            return uChoice
        else:
            print("Invalid choice. Choose rock, paper or scissors.")


def cpu_choice():
    """Generate a random choice for the cpu."""
    return random.choice(["rock", "paper", "scissors"])


def winner(player_choice, cpu_choice):
    """Show the winner of the game."""

    if player_choice == cpu_choice:
        return "It's a tie!"

    elif (
        (player_choice == "rock" and cpu_choice == "scissors") or
        (player_choice == "paper" and cpu_choice == "rock") or
        (player_choice == "scissors" and cpu_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"


def play_again():
    """Prompt the player for a rematch - function based on input"""
    answer = input("Would you like to play again? (yes/no)\n")

    if (answer == "yes"):
        play_game()

    else:
        print("Thanks for playing, goodbye!")
        


def play_game():
    """Plays rock, paper, scissors."""
    play_choice = player_choice()
    computer_choice = cpu_choice()
    print(f"You chose: {play_choice}\n")
    print(f"The computer chose: {computer_choice}\n")
    win = winner(play_choice, computer_choice)
    print(win)
    play_again()


if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        play_game()
        if play_again != "yes":
            break
