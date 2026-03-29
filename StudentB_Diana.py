"""
Student B: Timing & Validation
- Tracks the time taken to respond to a problem, its numeric validity, and accuracy
Author: Diana Quach
Date: 2026-03-27
"""

import time
import problem_generation as stuA
import StudentC as stuC

def timeResponseValidity(question):
    """
    Tracks the time taken to answer the problem and validates the answer is numeric.
    Returns the time taken and the valid user response.
    """

    isNumeric = False
    attempts = 0
    validCharacters = str([1,2,3,4,5,6,7,8,9,0]) # all answers will be in integer format

    startTime = time.time()
    while isNumeric == False: # loops the question until the user enters a valid response (numeric)
        userResponse = input(question)
        isNumeric = True
        for character in userResponse:
            if character not in validCharacters:
                isNumeric = False
    endTime = time.time()
    elapsedTime = round(endTime - startTime, 2) # time elapsed in seconds rounded to 2 decimal places

    return elapsedTime, userResponse

def answerChecker(userResponse, correctAns, elapsedTime):
    """
    Checks if the user responded with the correct answer and awards points accordingly.
    User receives an additional 2 points for a speedy and correct answer (<=5 seconds).
    Returns a boolean for correctness, and bonus points awarded.
    """

    isCorrect = (userResponse == correctAns) # compares user response to correct answer
    if isCorrect == True: # 2 for bonus speed
        if elapsedTime <= 5:
            bonusPoints = 2
    else:
        bonusPoints = 0
    return isCorrect, bonusPoints

def speedMode(difficulty):
    """
    Loops problem generation from Student C
    Ends the game once time limit is reached, allows final answer.
    Does not return anything, instead prints "TIME'S UP."
    """

    timeLimit = 120 # <- seconds = 2 minutes
    startTime = time.time()
    endTime = 0
    answerKey = []
    userAnswers = []

    while (endTime - startTime) < timeLimit: # continues if elapsed time is less than the limit
        stuC.runSpeedmode(difficulty)
        endTime = time.time() # total elapsed time tracker

    print("TIME'S UP")
