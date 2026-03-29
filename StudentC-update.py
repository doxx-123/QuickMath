import time
import random
from problem_generation


def calculateEndGameStats(stats):
    """Displays final game statistics."""
    attempted = stats["attempted"]
    correct = stats["correct"]
    totalTime = stats["totalTime"]

    if attempted > 0:
        accuracyPercent = (correct / attempted) * 100
        avgTime = totalTime / attempted
    else:
        accuracyPercent = 0.0
        avgTime = 0.0

    print("\n" + "=" * 30)
    print("FINAL STATISTICS")
    print("=" * 30)
    print(f"Mode:              {stats['mode']}")
    print(f"Problems Attempted: {attempted}")
    print(f"Correct:           {correct}")
    print(f"Accuracy:          {accuracyPercent:.1f}%")
    print(f"Avg Time/Problem:  {avgTime:.2f}s")
    if "finalScore" in stats:
        print(f"Final Score:       {stats['finalScore']}")
    if "highestStreak" in stats:
        print(f"Highest Streak:    {stats['highestStreak']}")
    print("=" * 30 + "\n")


def updateStreak(currentStreak, isCorrect):
    """Updates streak and returns new streak + multiplier."""
    if isCorrect:
        currentStreak += 1
        if currentStreak >= 10:
            multiplier = 2.0
        elif currentStreak >= 5:
            multiplier = 1.5
        else:
            multiplier = 1.0
    else:
        currentStreak = 0
        multiplier = 1.0
    return currentStreak, multiplier


def calculateTimeBonus(timeTaken):
    """Returns time bonus based on response speed."""
    if timeTaken <= 3:
        return 5
    elif timeTaken <= 5:
        return 2
    return 0


def runSpeedMode(difficultyLevel='medium'):
    """Speed mode: 2 minutes, as many problems as possible."""
    print("\n" + "=" * 30)
    print("SPEED MODE: 2 Minutes")
    print("=" * 30)

    problemsAttempted = 0
    correctAnswers = 0
    currentScore = 0
    timeLimit = 120
    startTime = time.time()

    while (time.time() - startTime) < timeLimit:
        problemString, correctAnswer = generate_problem(difficultyLevel)
        print(f"Solve: {problemString}")

        qStart = time.time()
        userInput = input("Your answer: ").strip()
        timeTaken = time.time() - qStart

        problemsAttempted += 1
        try:
            userGuess = int(userInput)
            isCorrect = (userGuess == correctAnswer)
        except ValueError:
            userGuess = None
            isCorrect = False
            print("Invalid input!")

        if isCorrect:
            correctAnswers += 1
            currentScore += 10
            print(f"Correct! (+10 pts) | Score: {currentScore}")
        else:
            print(f"Incorrect. Answer: {correctAnswer} | Score: {currentScore}")

        timeLeft = timeLimit - (time.time() - startTime)
        if timeLeft > 0:
            print(f"Time left: {int(timeLeft)}s\n")

    totalTimeSpent = time.time() - startTime
    return {
        "mode": "Speed",
        "attempted": problemsAttempted,
        "correct": correctAnswers,
        "totalTime": totalTimeSpent,
        "finalScore": currentScore
    }


def runStreakMode(difficultyLevel='medium'):
    """Streak mode: ends on first wrong answer."""
    print("\n" + "=" * 30)
    print("STREAK MODE: Sudden Death")
    print("=" * 30)
    print("One wrong answer ends the game!\n")

    problemsAttempted = 0
    correctAnswers = 0
    currentScore = 0
    currentStreak = 0
    startTime = time.time()

    while True:
        problemString, correctAnswer = generate_problem(difficultyLevel)
        print(f"Streak: {currentStreak} | Solve: {problemString}")

        qStart = time.time()
        userInput = input("Your answer: ").strip()
        timeTaken = time.time() - qStart

        problemsAttempted += 1
        try:
            userGuess = int(userInput)
            isCorrect = (userGuess == correctAnswer)
        except ValueError:
            isCorrect = False

        if isCorrect:
            currentStreak, multiplier = updateStreak(currentStreak, True)
            timeBonus = calculateTimeBonus(timeTaken)
            pointsEarned = (10 * multiplier) + timeBonus
            currentScore += pointsEarned
            correctAnswers += 1
            print(f"Correct! (+{pointsEarned} pts, {multiplier}x) | Score: {currentScore}")
        else:
            print(f"Incorrect. Answer: {correctAnswer}")
            print("Streak broken! Game Over.")
            break

        print()

    totalTimeSpent = time.time() - startTime
    return {
        "mode": "Streak",
        "attempted": problemsAttempted,
        "correct": correctAnswers,
        "totalTime": totalTimeSpent,
        "finalScore": currentScore,
        "highestStreak": currentStreak
    }


def runAccuracyMode(difficultyLevel='medium'):
    """Accuracy mode: 20 problems with penalties."""
    print("\n" + "=" * 30)
    print("ACCURACY MODE: 20 Problems")
    print("=" * 30)
    print("Mistakes cost 5 points!\n")

    totalProblems = 20
    problemsAttempted = 0
    correctAnswers = 0
    currentScore = 0
    startTime = time.time()

    for i in range(totalProblems):
        problemString, correctAnswer = generate_problem(difficultyLevel)
        print(f"Problem {i + 1}/20: {problemString}")

        qStart = time.time()
        userInput = input("Your answer: ").strip()
        timeTaken = time.time() - qStart

        problemsAttempted += 1
        try:
            userGuess = int(userInput)
            isCorrect = (userGuess == correctAnswer)
        except ValueError:
            isCorrect = False

        if isCorrect:
            correctAnswers += 1
            currentScore += 10
            print(f"Correct! (+10 pts) | Score: {currentScore}")
        else:
            currentScore = max(0, currentScore - 5)
            print(f"Incorrect. Answer: {correctAnswer} (-5 pts) | Score: {currentScore}")
        print()

    totalTimeSpent = time.time() - startTime
    return {
        "mode": "Accuracy",
        "attempted": problemsAttempted,
        "correct": correctAnswers,
        "totalTime": totalTimeSpent,
        "finalScore": currentScore
    }


# Demo: Run all modes
if __name__ == "__main__":
    speedStats = runSpeedMode('easy')
    calculateEndGameStats(speedStats)

    streakStats = runStreakMode('medium')
    calculateEndGameStats(streakStats)

    accuracyStats = runAccuracyMode('hard')
    calculateEndGameStats(accuracyStats)