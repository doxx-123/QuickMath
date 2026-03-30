"""
Quick-Draw Math Challenge
Authors: Retal Sabbahi, Diana Quach, Kareemat Adeagbo
2026-03-28
"""

"""
README
Welcome to the Quick-Draw Math Challenge! 

This game will challenge your accuracy and speed 
when answering basic math problems involving addition, 
subtraction, division, and multiplication.

To initiate the game, click the run button on PyCharm
with the main.py file open. Follow the instructions 
and input your responses into the console window to proceed. 
It will first prompt you to choose a difficulty from a
list of options: easy, medium, or hard. Depending on the 
difficulty, the range of numbers you will be working
with will vary. For example, easy mode generates
equations using integers from 1-10, medium mode uses 
integers from 1-50, and hard mode uses integers from 1-100. 
But be careful, these ranges apply only to the numbers 
in the equation. The answers may exceed this range!

Next, you will select a game mode from the following
options: speed, accuracy, or streak. In speed mode, 
you will have the opportunity to gain a large sum 
of points by answering as many problems as possible 
within a 2-minute limit. Accuracy mode generates 
twenty problems to solve. There is no time limit, 
so take your time, as incorrect answers will be 
penalized! Lastly, streak mode will reward you for 
consistently correct answers. If your streak is great
enough, a multiplier will be applied. An incorrect
answer in streak mode will end the game.

Across all game modes, correct answers will award you 
with +10 points. A speedy answer within 5 seconds will 
earn you an additional +2 points.

Once the difficulty and game mode have been selected, 
the game will begin! Good luck, and remember to input your 
answers as integers in the console window.
"""

import problem_generation as stuA # Student A: Problem Generation
import StudentB_Diana as stuB # Student B: Timing & Validation
import StudentC as stuC # Student C: Game Modes & Scoring

difficultyLevels = ["easy", "medium", "hard"]
gameModes = ["speed", "accuracy", "streak"]
print("=" * 50)
print("Welcome to Quick-Draw Math!")
print("=" * 50)

difficulty = input(f"Select a Difficulty Level {difficultyLevels}\n Choice: ").lower()
while difficulty not in difficultyLevels:
    print(f" INVALID - please choose {difficultyLevels}")
    difficulty = input(" Choice: ")

print("-" * 50)
gameMode = input(f"Select a Game Mode {gameModes}\n Choice: ").lower()
while gameMode not in gameModes:
    print(f" INVALID - please choose {gameModes}")
    gameMode = input(" Choice: ")

print("=" * 50)
print(f"You've chosen {difficulty.title()} {gameMode.title()} Mode!")
print("Let The Game Begin!")
print("=" * 50)

if gameMode == "speed":

#    stuC.GAMEMODE()

    elapsedTime, user88Response = stuC.runSpeedMode(difficulty)

if gameMode == "accuracy":

#    stuC.GAMEMODE()

    #elapsedTime, userResponse = stuC.runAccuracyMode(difficulty)

    answerKey = stuC.runAccuracyMode(difficulty)
if gameMode == "streak":

#    stuC.GAMEMODE()

    answerKey = stuC.runStreakMode(difficulty)