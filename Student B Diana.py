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
    elapsedTime = round(endTime - startTime, 3) # time elapsed in seconds rounded to 4 decimal places

    return elapsedTime, userResponse

def answerChecker(userResponse, correctAns, elapsedTime):
    """Checks if the user responded with the correct answer and awards points accordingly.
    User recieves 5 points for a correct answer, and an additonal 2 for a speedy anser (<=5 seconds).
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
