import time
import problem_generation

#Speed mode
def runSpeedmode(difficulty="medium"):
    """
    Runs the 2-minute speed mode game loop.
    :param difficulty: 'easy', 'medium', or 'hard' to pass to the problem generator.
    """
    print("\n" + "="*30)
    print("Speed Mode: 2 Minutes")
    print("="*30)
    #Game State variables
    problemsAttempted = 0
    timeLimit = 120 #  2 minutes in seconds
    correctAnswers = 0
    #start_time = time.time()
    stateTime = time.time()
    # The loop keeps running as long as the elapsed time is under 120 seconds
    while (time.time() - stateTime) < timeLimit:
        #1. Fetch the problem using student A's library function
        problemString, correctAnswers = problem_generation.generateProblem(difficulty)
        print(f"Solve: {problemString}")
        #Track how long this specific question takes
        qStart = time.time()
        userInput = input("Your answer:").strip()
        qEnd = time.time()
        timeTaken = qEnd - qStart
        problemsAttempted += 1
        # 2. Convert user input to an integer to match your generator's output
        try:
            userGuess = int(userInput)
        except ValueError:
            # If they typed a letter of left it blank force it to be wrong
            userGuess = None
            print("Invalid input! Please type a number.")
        # 3. Check the answer
        isCorrect = (userGuess == correctAnswers)
        if isCorrect:
            correctAnswers += 1
            print("Correct!")
        else:
            print(f"Incorrect. The answer was {correctAnswers}.")
        # 4. Calculate and show remaining time
        timeLeft = timeLimit - (time.time() - stateTime)
        if timeLeft > 0:
            print(f"Time remaining: {int(timeLeft)} seconds.")
    #--- End of Game ---
    totalTimeSpent = time.time() - stateTime
    print("\n" + "="*30)
    print("Time's up!")
    print("="*30)
    #Return the final stats so the stats screen can display them
    return {
        "mode": "Speed",
        "attempted": problemsAttempted,
        "correctAnswers": correctAnswers,
        "totalTime": totalTimeSpent
    }
speedStats = runSpeedmode('medium')
calculateEndGameStats(speedStats)

#Scoring system
currentScore = 0
pointsCorrectAnswers = 10
def updateBasescore(isCorrect):
    """
    Updates the score based on whether the answer was correct.
    Returns the points added so the UI can display real-time feedback.
    """
    global currentScore
    if isCorrect:
        currentScore += pointsCorrectAnswers
        return pointsCorrectAnswers
    else:
        # Base scoring doesn't penalize, so we add 0
        return 0
userGotitRight = True
pointsEarned = updateBasescore(userGotitRight)
print(f"Score is now: {currentScore}")


#Streak mode
def runStreakmode(difficulty="medium"):
    """
    Runs the Streak Mode game loop (Sudden Death).
    The game ends as soon as the player gets one answer wrong.
    """
    print("\n" + "="*30)
    print("Streak Mode: Sudden Death")
    print("="*30)
    print("Keep answering correctly to build multiplier.")
    print("One wrong answer ends the game!\n")

    #Game State Variables
    problemAttempted = 0
    correctAnswerCounter = 0
    currentScore = 0
    currentStreak = 0
    streakMultiplier = 1.0
    startTime = time.time()
    gameActive = True
    while gameActive:
        # 1. Fetch the problem from your library
        problemString, correctAnswers = problem_generation.generateProblem(difficulty)
        print(f"--- Current Streak: {currentStreak} ---")
        print(f"Solve: {problemString}")
        # Track time for the time bonus
        qStart = time.time()
        userInput = input("Your answer: ").strip()
        qEnd = time.time()
        timeTaken = qEnd - qStart
        problemsAttempted += 1
        # 2. Safely convert input to match the generator's integer output
        try:
            userGuess = int(userInput)
        except ValueError:
            userGuess = None
            print(" Invalid input! That counts as a wrong answer.")
            # 3. Check the answer
            isCorrect = (userGuess == correctAnswers)

            if isCorrect:
                correctAnswersCounter += 1
                currentStreak += 1
                # --- STREAK MULTIPLIER LOGIC ---
                if currentStreak >= 10:
                    streakMultiplier = 2.0
                elif currentStreak >= 5:
                    streakMultiplier = 1.5
                else:
                    streakMultiplier = 1.0
                    # --- TIME BONUS LOGIC ---
                    timeBonus = 0
                    if timeTaken <= 3:
                        timeBonus = 5
                    elif timeTaken <= 5:
                        timeBonus = 2
                        # --- CALCULATE POINTS ---
                        basePoints = 10
                        pointsEarned = (basePoints * streakMultiplier) + timeBonus
                        currentScore += pointsEarned

                        print(f"Correct! (+{pointsEarned} pts) | Multiplier: {streakMultiplier}x | Score: {currentScore}\n")
            else:
                    # They got it wrong. Break the loop!
                    print(f" Incorrect. The answer was {correctAnswers}.")
                    print(" Streak Broken! Game Over. \n")
                    gameActive = False
        # --- End of Game ---
        totalTimeSpent = time.time() - startTime
        print("=" * 30)
        print(" STREAK MODE COMPLETE! ")
        print("=" * 30)


        # Return the final stats (including their highest streak!)
        return {
            "mode": "Streak",
            "attempted": problemsAttempted,
            "correct": correctAnswersCounter,
            "totalTime": totalTimeSpent,
            "finalScore": currentScore,
            "highestStreak": currentStreak
        }
streakStats = runStreakmode('medium')
calculateEndGameStats(streakStats)
currentStreak = 0
streakMultiplier = 1.0
def updateStreak(isCorrect):
    global currentStreak, streakMultiplier
    if isCorrect:
        currentStreak += 1
        # Upgrade multiplier based on milestones
        if currentStreak >= 10:
            streakMultiplier = 2.0
        elif currentStreak >= 5:
            streakMultiplier = 1.5
        else:
            streakMultiplier = 1.0
    else:
        #Reset on incorrect answer
        currentStreak = 0
        streakMultiplier = 1.0
    return streakMultiplier
def calculateTimebonus(timeTaken):
    bonus = 0
    #Fastest answers get the highest bonus
    if timeTaken <= 3:
        bonus = 5
    elif timeTaken <= 5:
        bonus = 2
    #Anything over 5 seconds gets 0 bonus points
    return bonus
totalScore = 0
def processAnswer(isCorrect, timeTaken, gameMode):
    global totalScore
    if isCorrect:
        # 1. Update streak and get the current multiplier
        multiplier = updateStreak(True)
        # 2. Calculate time bonus
        timeBonus = calculateTimebonus(timeTaken)
        # 3. Aggregate points for this specific question
        # Math: (Base * Multiplier) + Time Bonus
        pointsEarned = (pointsCorrectAnswers * multiplier) + timeBonus
        #4. Add to running total
        totalScore += pointsEarned
        return pointsEarned # Returns points earned to show on the UI
    else:
        #Wrong answer: Reset streak, multiplier drops to 1.0
        updateStreak(False)
        #If they are in Accuracy mode, apply the penalty
        if gameMode == "ACCURACY":
            totalScore == applyAccuracypenalty(totalScore, penaltyAmount=5)
        return 0 # 0 points earned
def applyAccuracypenalty(currentScore, penaltyAmount=5):
    """
    Subtract the penalty, but use max() to keep the score at or above 0
    """
    newScore = max(0, currentScore - penaltyAmount)
    return newScore
#Time trackers
#Accuracy
def runAccuracymode(difficulty="medium"):
    """
    Runs the Accuracy Mode game loop (20 questions).
    :param difficulty: 'easy', 'medium' or 'hard' to pass to the problem generator.
    """
    print("\n" + "="*30)
    print("Accuracy Mode: 20 Problems")
    print("="*30)
    print("Take your time. Mistakes will cost you points!\n")
    #Game State Varibales
    totalProblems = 20
    problemsAttempted = 0
    correctAnswers = 0
    currentStreak = 0
    currentScore = 0
    #Start the master clock just for end-game stats
    startTime = time.time()
    # The loop runs exactly 20 times
    for i in range(totalProblems):
        # 1. Fetch the problem
        problemString, correctAnswers = problems.generateProblems(difficulty)
        print(f"--- Problem{i + 1} of {totalProblems} ---")
        print(f"solve {problemString}")
        # Track how long this specific question takes
        qStart = time.time()
        userInput = input("Your answer:").strip()
        qEnd = time.time()
        timeTaken = qEnd - qStart
        problemsAttempted += 1
        # 2. Safely convert user input to an integer
        try:
            userGuess = int(userInput)
        except ValueError:
            userGuess = None
            print("Invalid input! That count as a wrong answer.")
        # 3. Check the answer & apply accuracy penalty
        isCorrect = (userGuess == correctAnswers)
        if isCorrect:
            correctAnswers += 1
            currentScore += 10 #Base points
            print(f"Correct! (+10 pts) | Score: {currentScore}\n")
        else:
            # Here is the Accuracy Penalty logic:\
            penalty = 5
            # max(0, ...) ensure the score never goes into the negatives
            currentScore = max(0, currentScore - penalty)
            print(f"Incorrect. The answer was {correctAnswers}.")
            print(f"Penalty applied: (-{penalty}pts)| Score: {currentScore}\n")
    # --- End of Game ---
    totalTimeSpent = time.time() - startTime
    print("="*30)
    print("Accuracy Mode Complete!")
    print("="*30)
    # Return the final stats
    return {
        "mode": "Accuracy",
        "attempted": problemsAttempted,
        "correct": correctAnswers,
        "totalTime": totalTimeSpent,
        "finalScore": currentScore
    }
accuracyStats = runAccuracymode('medium')
calculateEndGameStats(accuracyStats)
# End game stats
def calculateEndGameStats(statsDictionary):
    """
    Takes the dictionary returned by a game mode and calculates
    the final Accuracy Percentage and Average Time Per Problem.
    """
    attempted = statsDictionary["attempted"]
    correct = statsDictionary["correct"]
    totalTime = statsDictionary["totalTime"]

    # We must check if attempted > 0 to prevent a "Division by Zero" crash!
    if attempted > 0:
        accuracyPercent = (correct / attempted) * 100
        avgTime = totalTime / attempted
    else:
        accuracyPercent = 0.0
        avgTime = 0.0

    print("\n" + "=" * 30)
    print(" FINAL STATISTICS")
    print("=" * 30)
    print(f"Mode Played:        {statsDictionary['mode']}")
    print(f"Problems Attempted: {attempted}")
    print(f"Correct Answers:    {correct}")
    # The :.1f formats the number to 1 decimal place (e.g., 85.5%)
    print(f"Accuracy:           {accuracyPercent:.1f}%")
    print(f"Avg Time/Problem:   {avgTime:.2f} seconds")

    # If the mode tracked a final score, display it
    if "finalScore" in statsDictionary:
        print(f"Final Score:        {statsDictionary['finalScore']}")

    # If the mode tracked a highest streak, display it
    if "highestStreak" in statsDictionary:
        print(f"Highest Streak:     {statsDictionary['highestStreak']}")
    print("=" * 30 + "\n")