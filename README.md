# Rock, Paper, Scissors!

![image](https://github.com/barcodin9/PP3-rock-paper-scissors/assets/109236559/f6acc68a-4e81-482b-8ad4-86df7c0cfde5)

Rock, Paper, Scissors is a game built entirely using Python. This site is targeted toward anybody who wishes to play Rock, Paper, Scissors against a computer.

I built this game in order to gain a greater understanding of Python and its functionalities. Having built a similar project in JavaScript previously, I feel I came into this project better prepared with a better understanding and found it to be a smoother process than it's JS counterpart.


# Features

## The Intro Tag

I included an intro tag that welcomes you to the game before prompting you to pick your move.

<img width="325" alt="Screenshot 2023-09-14 at 00 07 34" src="https://github.com/barcodin9/PP3-rock-paper-scissors/assets/109236559/e8c0e162-ff11-4276-b6fb-4365fc03a3c5">

## The Choice Display 

Once you have picked a move out of the three valid options, it will display said move and the cpu's move.

<img width="244" alt="Screenshot 2023-09-14 at 00 09 28" src="https://github.com/barcodin9/PP3-rock-paper-scissors/assets/109236559/2cdf462c-9ae7-40da-89ba-7f00e5304d0f">

## The Winners Display

Once the moves have been displayed, the game will determine who won the round and then display it below.

<img width="158" alt="Screenshot 2023-09-14 at 00 11 10" src="https://github.com/barcodin9/PP3-rock-paper-scissors/assets/109236559/be9a72f1-0f44-4556-9e00-eb0045b6b4ea">

## The Score 

The game will track the score as long as the rounds are played consecutively, once the loop is broken, the score will reset.

<img width="361" alt="Screenshot 2023-09-14 at 00 13 36" src="https://github.com/barcodin9/PP3-rock-paper-scissors/assets/109236559/575117b8-7efb-4455-be16-03c7939683cd">



# Vaildator Testing

I ran the code through the CI Code Linter and returned no errors.

![Screenshot 2023-09-13 at 23 51 09](https://github.com/barcodin9/PP3-rock-paper-scissors/assets/109236559/a21b6824-19e4-483d-8903-080a0cd02ff9)


# Bugs 

Whilst in the process of coding, I created a bug due to an empty field in the Score function which generated about 1.2 million wins for the cpu before I managed to terminate the code. - This has since been resolved.

I was unable to find any other bugs in the finished code. 


# Deployment

- The site was deployed to Heroku via Github. The steps to deploy are as follows: 
  - In Heroku - I created a new app, naming it "rock-paper-scissors-pp3.
  - Once created, I navigated to the settings menu and installed the two necessary buildpacks (python & nodejs).
  - I then navigated to the Deploy section and selected GitHub as the deployment method.
  - I selected Automatiic Deploys and then navigated to Manual Deploy and selected deploy from the main branch.
 
The live link can be found here - https://rock-paper-scissors-ci-pp3-cfc0f0244e4f.herokuapp.com/

# Thank you for reading, I hope you enjoyed my project.
