"""
Quick-Draw Math Challenge
Authors: Retal Sabbahi, Diana Quach, Kareemat Adeagbo
2026-03-28
"""

import problem_generation as stuA # Student A: Problem Generation
import StudentB_Diana as stuB # Student B: Timing & Validation
import StudentC as stuC # Student C: Game Modes & Scoring

"""
Temporary Key
    stuA.generateProblem(difficulty)            # returns problem, answer
    stuB.timeResponseValidity(question)         # returns elapsedTime per problem, userResponse
    stuB.answerChecker(response, answer, time)  # returns isCorrect, bonusPoints
    stuB.speedMode()                            # returns answerKey, userAnswers
    stuC.runSpeedmode(difficulty)               # returns 
"""

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