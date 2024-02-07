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


def play_tourney(best_of):
    """Plays a best of 'X' game of rock, paper, scissors, multiple games played until overall winner determined."""
    user_score, cpu_score = 0, 0
    games_need = best_of // 2 + 1

    while user_score < games_need and cpu_score < games_need:
        result = play_game()

        if "You win!" in result:
            user_score += 1
        elif "It's a tie" in result:
            pass
        else:
            cpu_score += 1

        print(f"Score is - You: {user_score} | Computer: {cpu_score}")

    if user_score > cpu_score:
        print("You have won the Tournament!")
    else:
        print("Computer has won the Tournament!")


def main():
    while True:
        print("Welcome to Rock, Paper, Scissors!")
        game_type = input("Would you like to play a single game or a best of tournament? (Enter 'single' or 'best of'):\n").lower()

        if game_type == "best of":
            """User select the type of game they would like to play"""
            while True:
                try:
                    """Ensure user puts in odd number for proper tourney functionality"""
                    best_of = int(input("Enter the number of games for the Tournament, number should be odd (e.g. 3, 5, 7, 9)\n"))
                    if best_of % 2 == 1:
                        play_tourney(best_of)
                        break
                    else:
                        print("The number entered must be odd")
                except ValueError:
                    print("Please enter a valid number.")

            """If user selects single, directs to play_game function and plays individual game of RPS without stat tracking."""
        elif game_type == "single":
            play_game()

            """If user enters invalid input - 'restarts' loop"""
        else:
            print("Input not valid, please enter 'single' or 'best of")
            continue

        play_again = input("Would you like to play again? (y/n) \n")

        if play_again.lower() == "y":
            continue
        elif play_again.lower() == "n":
            print("Thanks for playing, goodbye!")
            break
        elif play_again.lower() != "y":
            print("Input not valid, directing to home.")
            continue


if __name__ == "__main__":
    main()
