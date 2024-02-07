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
        return "It's a tie!\n"

    elif (
        (player_choice == "rock" and cpu_choice == "scissors") or
        (player_choice == "paper" and cpu_choice == "rock") or
        (player_choice == "scissors" and cpu_choice == "paper")
    ):
        return "You win!\n"
    else:
        return "Computer wins!\n"


def play_game():
    """Plays rock, paper, scissors."""
    play_choice = player_choice()
    computer_choice = cpu_choice()
    print(f"You chose: {play_choice}\n")
    print(f"The computer chose: {computer_choice}\n")
    win = winner(play_choice, computer_choice)
    print(win)
    return win


if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    game_type = input("Would you like to play a single game or a best of tournemant? (Enter 'single' or 'best of'):").lower()

    user_score = 0
    cpu_score = 0

    while True:
        result = play_game()
        if "You win" in result:
            user_score += 1
        elif "It's a tie" in result:
            user_score += 1
            cpu_score += 1
        else:
            cpu_score += 1

        print(f"Your score: {user_score} || Computer score: {cpu_score}")

        while True:
            play_again = input("Would you like to play again? (y/n) \n")
            if play_again.lower() == "y":
                break
            elif play_again.lower() == "n":
                print("Thanks for playing, goodbye!")
                exit()
            else:
                print("Input not valid, please enter y/n")
            
            