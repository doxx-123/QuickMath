# Quick Draw Math Challenge
# Authors: Kareemat Adeagbo
# 2026-3-28

import time
import problem_generation as stuA
#from StudentB_Diana import answerChecker as stuB
#from StudentB_Diana import timeResponseValidity as stuB
from StudentB_Diana import answerChecker
from StudentB_Diana import timeResponseValidity

def calculateEndGameStats(stats):
    """Unified stats display across all modes."""
    attempted = stats["attempted"]
    correct = stats["correct"]
    totalTime = stats["totalTime"]

    if attempted > 0:
        accuracy = (correct / attempted) * 100
        avgTime = totalTime / attempted
    else:
        accuracy = avgTime = 0.0

    print("\n" + "=" * 40)
    print("FINAL STATISTICS")
    print("=" * 40)
    print(f"Mode:     {stats['mode']}")
    print(f"Attempted:{attempted:>8} | Correct: {correct:>3}")
    print(f"Accuracy: {accuracy:>6.1f}% | Avg Time: {avgTime:>6.2f}s")
    if "score" in stats:
        print(f"Score:    {stats['score']}")
    if "streak" in stats:
        print(f"Max Streak:{stats['streak']:>7}")
    print("=" * 40)


def runSpeedMode(difficulty):
    """Speed: 120s unlimited problems (uses Student B timing)."""
    print("\nSPEED MODE (120s): Solve as many as possible!")
    print("=" * 40)

    timeLimit = 120
    startTime = time.time()
    attempted, correct, score = 0, 0, 0
    answerKey = []

    while (time.time() - startTime) < timeLimit:
        # Student A: Generate problem
        print("\nTIME REMAINING:", round(timeLimit - (time.time() - startTime), 2), "seconds!")
        problemString, correctAns = stuA.generateProblem(difficulty)
        print(problemString)

        # Student B: Time + validate input
        elapsed, userResp = timeResponseValidity(correctAns)

        # Check if overtime
        if (time.time() - startTime) >= timeLimit:
            print("TIME'S UP!")
        else:
            # Put all of your checking and scoring logic right here inside this else block!
            # It will only run if they answered before the timer ran out.

            if userResp == correctAns:
                print("Correct!")
                # Add points, track stats, etc.
            else:
                print("Incorrect!")

        attempted += 1
        answerKey.append(correctAns)

        # Student B: Check answer + bonus
        isCorrect, bonus = answerChecker(str(userResp), str(correctAns), elapsed)
        if isCorrect:
            correct += 1
            score += 10 + bonus
            print(f"CORRECT! +{10 + bonus} pts (time: {elapsed}s)")
        else:
            print(f"WRONG (ans: {correctAns}). Score: {score}")

    totalTime = time.time() - startTime
    calculateEndGameStats({
        "mode": "Speed", "attempted": attempted, "correct": correct,
        "totalTime": totalTime, "score": score
    })
    return answerKey, [str(correctAns) for correctAns in answerKey]  # For analysis


def runAccuracyMode(difficulty):
    """Accuracy: Exactly 20 problems, -5pt penalties."""
    print("\nACCURACY MODE (20 problems): Precision matters!")
    print("=" * 40)

    totalProblems = 20
    attempted, correct, score = 0, 0, 0
    answerKey = []

    for i in range(totalProblems):

        problemString, correctAns = stuA.generateProblem(difficulty)
        print(f"\n#{i + 1}/20: {problemString}")

       # elapsed, userResp = stuB.timeResponseValidity(correctAns)
        elapsed, userResp = timeResponseValidity(correctAns)

        attempted += 1
        answerKey.append(correctAns)

        isCorrect, bonus = answerChecker(str(userResp), str(correctAns), elapsed)
        if isCorrect:
            correct += 1
            score += 10 + bonus
            print(f"CORRECT! +{10 + bonus} pts")
        else:
            score = max(0, score - 5)  # Penalty
            print(f"WRONG (-5 pts). Ans: {correctAns}. Score: {score}")

    totalTime = time.time() - startTime if 'startTime' in locals() else 0
    calculateEndGameStats({
        "mode": "Accuracy", "attempted": attempted, "correct": correct,
        "totalTime": totalTime, "score": score
    })
    return answerKey


def runStreakMode(difficulty):
    """Streak: Ends on first wrong, multipliers + time bonus."""
    print("\nSTREAK MODE: One wrong = GAME OVER!")
    print("=" * 40)

    streak, score, attempted, correct = 0, 0, 0, 0
    answerKey = []

    # Create a control variable to run the loop
    gameActive = True

    while gameActive:
        problemString, correctAns = stuA.generateProblem(difficulty)
        print(f"\nStreak: {streak} | {problemString}")

        # elapsed, userResp = stuB.timeResponseValidity(correctAns)
        elapsed, userResp = timeResponseValidity(problemString)
        attempted += 1
        answerKey.append(correctAns)

        # isCorrect, bonus = stuB.answerChecker(str(userResp), str(correctAns), elapsed)
        isCorrect, bonus = answerChecker(str(userResp), str(correctAns), elapsed)

        if isCorrect:
            streak += 1
            multiplier = 2.0 if streak >= 10 else 1.5 if streak >= 5 else 1.0
            points = (10 * multiplier) + bonus
            score += points
            correct += 1
            print(f"CORRECT! +{points:.1f} pts ({multiplier}x +{bonus} time)")
        else:
            print(f"STREAK BROKEN! Ans: {correctAns}")
            # Change the variable to False to naturally
            gameActive = False

    calculateEndGameStats({
        "mode": "Streak", "attempted": attempted, "correct": correct,
        "totalTime": 0, "score": score, "streak": streak
    })
    return answerKey


