# Rock, Paper, Scissors!

<img width="749" alt="Screenshot 2024-02-07 at 03 14 02" src="https://github.com/barcodin9/PP3-rock-paper-scissors/assets/109236559/74d9d597-0dfa-40eb-bf2a-5b98e63f7cc5">


Rock, Paper, Scissors is a game built entirely using Python. This site is targeted toward anybody who wishes to play Rock, Paper, Scissors against a computer.

I built this game in order to gain a greater understanding of Python and its functionalities. Having built a similar project in JavaScript previously, I feel I came into this project better prepared with a better understanding and found it to be a smoother process than it's JS counterpart.


# Features

## The Intro Tag

I included an intro tag that welcomes you to the game before prompting you to pick a game mode, single or best of x.

<img width="730" alt="Screenshot 2024-02-07 at 03 12 17" src="https://github.com/barcodin9/PP3-rock-paper-scissors/assets/109236559/40ed809e-5350-46f3-b042-5dfccfb969da">


## The Choice Display 

If you pick single, you will be directed into a game, once you have picked a move out of the three valid options, it will display said move and the cpu's move.

<img width="244" alt="Screenshot 2023-09-14 at 00 09 28" src="https://github.com/barcodin9/PP3-rock-paper-scissors/assets/109236559/2cdf462c-9ae7-40da-89ba-7f00e5304d0f">

## Best of X

If you select "best of" you will be prompted to choose the number of games you wish to play (e.g. best of 3, 5, 7 etc..) - this has to be an odd number to ensure there is only one winner.

<img width="730" alt="Screenshot 2024-02-07 at 03 52 53" src="https://github.com/barcodin9/PP3-rock-paper-scissors/assets/109236559/9cf6016e-3615-49d2-8b59-73d26134f60f">


## The Winners Display

Once the moves have been displayed, the game will determine who won the round and then display it below.

<img width="158" alt="Screenshot 2023-09-14 at 00 11 10" src="https://github.com/barcodin9/PP3-rock-paper-scissors/assets/109236559/be9a72f1-0f44-4556-9e00-eb0045b6b4ea">

## The Score 

In 'single' match mode - the score will not be tracked, each game is played individually. However, in 'best of' match modes, the score will be tracked until a winner is determined.

<img width="743" alt="Screenshot 2024-02-07 at 03 16 27" src="https://github.com/barcodin9/PP3-rock-paper-scissors/assets/109236559/c637ff41-2bcc-4d3a-a50b-37ce9909962e">


## Attributes

This document outlines the functional attributes of the Rock, Paper, Scissors game, including descriptions of global functions, variables, and expected behaviors.

### Global Functions

- **`player_choice()`**: Prompts the user to select "rock", "paper", or "scissors". Validates the input to ensure it matches one of the valid choices. Returns the player's choice as a lowercase string.

- **`cpu_choice()`**: Generates a random selection of "rock", "paper", or "scissors" for the computer's choice. Returns this choice as a string.

- **`winner(player_choice, cpu_choice)`**: Compares the player's choice against the computer's to determine the game's outcome. Returns a string indicating whether the result is a tie, a player win, or a computer win.

- **`play_game()`**: Conducts a single game round by obtaining choices from the player and the computer, determining the winner, and printing both choices and the result. Returns the result as a string.

- **`play_tourney(best_of)`**: Manages a tournament mode, playing multiple games until one side wins a majority. It tracks and announces scores and the overall winner based on the `best_of` parameter.

- **`main()`**: Serves as the entry point for the program. It handles user input for selecting a single game or a tournament, manages the tournament's game count input, and allows replaying. It ensures input validation and controls the overall game flow.

### Variables

- **`game_type`**: A string that captures the user's selection between a single game and a tournament.

- **`best_of`**: An integer determining the total number of games in a tournament, as input by the user. Must be odd to ensure a definitive winner.

- **`user_score`, `cpu_score`**: Integer counters used in `play_tourney` to track the number of games won by the player and the computer, respectively.

- **`games_need`**: An integer calculated as `best_of // 2 + 1`, representing the number of wins required to claim the tournament victory.

- **`result`**: A string variable that holds the outcome of each game within `play_game` or `play_tourney`, utilized for score updating and player notification.

### Expected Behaviors

- **Replaying Option**: After concluding a game or tournament, players are prompted to play again, allowing for continuous engagement until opting out.

- **Input Validation**: Ensures the integrity of user inputs for game type, tournament game count, and replay choice, with corrective feedback and reprompting as necessary.



# Vaildator Testing

I ran the code through the CI Code Linter and returned no errors (long strings are being flagged).

<img width="1334" alt="Screenshot 2024-02-07 at 03 31 34" src="https://github.com/barcodin9/PP3-rock-paper-scissors/assets/109236559/7aa4a4cf-ba66-4989-9141-3a8107052071">


# Manual Testing

### Test Case 1: Player Choice Validation

**Objective**: Ensure the program accepts only "rock", "paper", or "scissors" as valid inputs for the player's choice.

- **Steps**:
    1. Run the program.
    2. Select either "single" or "best of" game mode.
    3. When prompted for a choice, enter an invalid input (e.g., "test").
- **Expected Result**: The program should display "Invalid choice. Choose rock, paper or scissors." and prompt for a valid choice again.
- **Actual Result**: When an invalid input is entered, "Invalid choice. Choose rock, paper or scissors." displays and the user is prompted again for a valid choice.

### Test Case 2: CPU Choice Randomness

**Objective**: Confirm that the CPU's choice is random among "rock", "paper", and "scissors".

- **Steps**:
    1. Run the program multiple times in any game mode.
    2. Note the CPU's choice each time.
- **Expected Result**: Over several runs, the CPU should select "rock", "paper", and "scissors" at random, with no discernible pattern.
- **Actual Result**: Over several runs on both 'single' and 'best of' game modes - although there was the occasional repetition, there was no discernable pattern.

### Test Case 3: Game Outcome Correctness

**Objective**: Verify the game correctly identifies a win, loss, or tie based on the choices made.

- **Steps**:
    1. Run the program and select "single" game mode.
    2. Play at least one game with each choice (rock, paper, scissors), ensuring the CPU makes varied choices.
- **Expected Result**: The program should correctly announce the game outcome (win, loss, tie) for each scenario.
- **Actual Result**: The program correctly announces the winner based on the outcome of the game.

### Test Case 4: Best of Tournament Functionality

**Objective**: Test the "best of" tournament mode, including validation for an odd number of games.

- **Steps**:
    1. Run the program and select "best of" game mode.
    2. Enter an even number when prompted for the tournament size, then enter a valid odd number (e.g., 3) and complete the tournament.
- **Expected Result**: The program should reject the even number with a warning and accept the odd number, running the tournament correctly to determine the winner.
- **Actual Result**: The program rejects even numbers and prompts the player to input a valid number. Once a valid number is entered, it will proceed to the games and the winner is correctly determined based on the games played and points earned.

### Test Case 5: Replay Functionality

**Objective**: Ensure the program allows users to play again or exit appropriately after a game or tournament.

- **Steps**:
    1. Complete a game or tournament.
    2. When prompted to play again, first enter "y", then "n" after the subsequent game/tournament.
- **Expected Result**: The program should restart when "y" is entered and exit with a goodbye message when "n" is entered.
- **Actual Result**: When "y" is entered, the program will restart, if "n" is entered, a goodbye message will display and the user will exit, when an invalid option is entered, an error message will display and redirect to the start of the application.

### Test Case 6: Input Validation for Game Type Selection

**Objective**: Confirm the game handles invalid game type selections gracefully.

- **Steps**:
    1. Run the program.
    2. At the game type selection prompt, enter an invalid option (e.g., "double").
- **Expected Result**: The program should display "Input not valid, please enter 'single' or 'best of'" and re-prompt for a valid selection.
- **Actual Result**: Discovered and remedied a typo in the error message. Error message displays correctly and re-prompts the user for a valid input.

# Programs Used
- VScode - Used as Coding Environment.
- Github - Used for creating application repository, version control, organising workflow utilising agile functionality of GitHub issues.
- Heroku - Used as a coding environment.
- CI Python Linter - Used to validate Python.


# Bugs 

Whilst in the process of coding, I created a bug due to an empty field in the Score function which generated about 1.2 million wins for the cpu before I managed to terminate the code. - This has since been resolved.

Whilst building the play_tourney function and supporting elements, I encountered a bug that would not update the scoreboard and would continuously prompt the user to input rock, paper or scissors, I narrowed this down to a rogue play_game() function and remedied.


# Deployment

- The site was deployed to Heroku via Github. The steps to deploy are as follows: 
  - In Heroku - I created a new app, naming it "rock-paper-scissors-pp3.
  - Once created, I navigated to the settings menu and installed the two necessary buildpacks (python & nodejs).
  - I then navigated to the Deploy section and selected GitHub as the deployment method.
  - I selected Automatiic Deploys and then navigated to Manual Deploy and selected deploy from the main branch.
 
The live link can be found here - https://rock-paper-scissors-ci-pp3-cfc0f0244e4f.herokuapp.com/

# Thank you for reading, I hope you enjoyed my project.
