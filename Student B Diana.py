"""
Student B: Timing & Validation
Author: Diana Quach
Date: 2026-03-27
"""
"""Student B: Timing & Validation
- Track time per problem: record time.time() before displaying the question, and again after the student
answers; compute elapsed time
- Validate numeric input
- Check answer correctness
- Award bonus points for speed (faster = more points, based on elapsed time)
- For Speed Mode: track total elapsed time across all problems and end the round when the limit is
reached
- Note: a live countdown display is not possible in a standard terminal. Use post-answer elapsed time for
all timing logic."""

import time

def timeResponseValidity(question):
    """Tracks the time taken to answer the problem and validates the answer is numeric.
    Returns the time taken and the valid user response."""
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
    """Checks if the user responded with the correct answer and awards points accordingly.
    User receives 5 points for a correct answer, and an additional 2 for a speedy answer (<=5 seconds).
    Returns a boolean for correctness, and points awarded."""
    isCorrect = (userResponse == correctAns)
    if isCorrect == True: # 5 for correct, 2 for bonus speed
        if elapsedTime <= 5:
            pointsAwarded = 5 + 2
        else:
            pointsAwarded = 5
    else:
        pointsAwarded = 0
    return isCorrect, pointsAwarded
"""- For Speed Mode: track total elapsed time across all problems and end the round when the limit is
reached"""

def speedMode():
    """Provides multiple problems to be completed within 2 minutes"""
    timeLimit = 10 # seconds = 2 minutes
    startTime = time.time()
    endTime = 0
    points = 0

    while (endTime - startTime) < timeLimit:
        problem, answer = generateProblem(difficultyLevel) # relies on Student A
        elapsedTime, userResponse = timeResponseValidity(problem)
        endTime = time.time() # total time tracker
        if (endTime - startTime) >= timeLimit: # total time elapsed exceeds time limit
            overTime = round((endTime - startTime ) - timeLimit, 2)
            print(f"TIME'S UP!\nAnswer NOT Accepted - overtime by {overTime} seconds")
            print("Total Points:", points)
            return points
        else:
            correct, pointsAwarded = answerChecker(userResponse, answer, elapsedTime)
            points += pointsAwarded
            if correct == True:
                print(f"CORRECT! +{pointsAwarded}")
            if correct == False:
                print("INCORRECT!")
    print("TIME'S UP")
    print("Total Points:", points)
    return points
