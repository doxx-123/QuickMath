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

def timeAndResponse(question):
    """Tracks the time taken to answer the problem, and returns the time taken and user response."""
    startTime = time.time()
    userResponse = input(question)
    endTime = time.time()
    elapsedTime = round(endTime - startTime, 4) # time elapsed in seconds rounded to 4 decimal places

    return elapsedTime, userResponse

def numericValidation(userResponse):
    """Validates that the user responded with a numeric input. Returns a boolean value"""
    validCharacters = str([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # all answers will be in integer format
    isNumeric = True
    for character in userResponse:
        if character not in validCharacters:
            isNumeric = False
    return isNumeric

def answerChecker(userResponse, correctAns):
    """Checks if the user responded with the correct answer and returns a boolean"""
    isCorrect = (userResponse == correctAns) #5 for correct, 2 for bonus speed
    return isCorrect
