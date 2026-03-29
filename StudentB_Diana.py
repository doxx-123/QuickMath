"""
Student B: Timing & Validation
- Tracks the time taken to respond to a problem, its numeric validity, and accuracy
Author: Diana Quach
Date: 2026-03-27
"""

import time

def timeResponseValidity(question):
    """
    Tracks the time taken to answer the problem and validates the answer is numeric.
    Returns the time taken and the valid user response.
    """

    isNumeric = False
    attempts = 0
    validCharacters = str([1,2,3,4,5,6,7,8,9,0]) # all answers will be in integer format

    startTime = time.time()
    while isNumeric == False: # loops the question until the user enters a valid response
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

    isCorrect = (userResponse == correctAns)
    if isCorrect == True: # 2 for bonus speed
        if elapsedTime <= 5:
            bonusPoints = 2
    else:
        bonusPoints = 0
    return isCorrect, bonusPoints

def speedMode():
    """
    Provides multiple problems to be completed within the time limit.
    Ends the game once time limit is reached, allows final answer.
    Returns a list of correct answers (answerKey) and a list of user
    responses (userAnswers).
    """

    timeLimit = 10 # 2 minutes
    startTime = time.time()
    endTime = 0
    answerKey = []
    userAnswers = []

    while (endTime - startTime) < timeLimit:
        problem, answer = "3 + 2", "5" #generateProblem(difficultyLevel) # relies on Student A
        elapsedTime, userResponse = timeResponseValidity(problem)
        answerKey.append(str(answer))
        endTime = time.time() # total time tracker

        if (endTime - startTime) >= timeLimit: # total time elapsed exceeds time limit
            userAnswers.append("0")
            overTime = round((endTime - startTime ) - timeLimit, 2)
            print(f"TIME'S UP!")
            return answerKey, userAnswers
        else:
            userAnswers.append(userResponse)

            #f"Answer NOT Accepted - overtime by {overTime} seconds")
            #print("Total Points:", points)
            #return points
        #else:
            #correct, pointsAwarded = answerChecker(userResponse, answer, elapsedTime)
            #points += pointsAwarded
            #if correct == True:
            #    print(f"CORRECT! +{pointsAwarded}")
            #if correct == False:
            #    print("INCORRECT!")
    print("TIME'S UP")
    return answerKey, userAnswers
    #print("Total Points:", points)
    #return points