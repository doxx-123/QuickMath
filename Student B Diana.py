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

def timeTracker(question):
    """Tracks the time taken to answer the problem, and returns the time taken and user response."""
    startTime = time.time()
    userResponse = input(question)
    endTime = time.time()
    elapsedTime = endTime - startTime
    return elapsedTime, userResponse

def 

