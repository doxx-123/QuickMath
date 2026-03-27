import problem_generation as stuA
import StudentB_Diana as stuB
# import Student C as stuC
"""
Temporary Key
    stuA.generateProblem(difficulty)            # returns problem, answer
    stuB.timeResponseValidity(question)         # returns elapsedTime per problem, userResponse
    stuB.answerChecker(response, answer, time)  # returns isCorrect, pointsAwarded
    stuB.speedMode()                            # returns answerKey, userAnswers
"""
difficultyLevels = ["easy", "medium", "hard"]
gameModes = ["!-temporary-!"]

print("Welcome to Quick-Draw Math!")
difficulty = input(f"Select a Difficulty Level ({difficultyLevels}): ")
while difficulty not in difficultyLevels:
    difficulty = input(f"INVALID \nSelect a Difficulty Level ({difficultyLevels}): ")

"""gameMode = input(f"Choose a Game Mode ({gameModes}): ")
while gameMode not in gameModes:
    gameMode = input(f"INVALID \nChoose a Game Mode ({gameModes}): ")""" #ADD AFTER STUDENT B

# if gameMode == ...

