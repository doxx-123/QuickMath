import random

def generateAddition(minVal, maxVal):
    """
    Generates a random addition problem within the specified range.

    :param minVal: minimum number for the operands
    :param maxVal: maximum number for the operands
    :return: A tuple containing (problemString, correctAnswer)
    """
    num1 = random.randint(minVal, maxVal)
    num2 = random.randint(minVal, maxVal)

    correctAnswer = num1 + num2
    problemString = f"{num1} + {num2}"

    return problemString, correctAnswer


def generateSubtraction(minVal, maxVal):
    """
    Generates a random subtraction problem ensuring a non-negative result.

    :param minVal: minimum number for the operands
    :param maxVal: maximum number for the operands
    :return: A tuple containing (problemString, correctAnswer)
    """
    num1 = random.randint(minVal, maxVal)
    num2 = random.randint(minVal, maxVal)

    # Ensure num1 is the larger number to avoid negative answers
    if num2 > num1:
        num1, num2 = num2, num1

    correctAnswer = num1 - num2
    problemString = f"{num1} - {num2}"

    return problemString, correctAnswer


def generateMultiplication(minVal, maxVal):
    """
    Generates a random multiplication problem within the specified range.

    :param minVal: minimum number for the operands
    :param maxVal: maximum number for the operands
    :return: A tuple containing (problemString, correctAnswer)
    """
    num1 = random.randint(minVal, maxVal)
    num2 = random.randint(minVal, maxVal)

    correctAnswer = num1 * num2
    problemString = f"{num1} * {num2}"

    return problemString, correctAnswer


def generateDivision(minVal, maxVal):
    """
    Generates a random division problem ensuring an integer result.

    :param minVal: minimum number for the divisor and the answer
    :param maxVal: maximum number for the divisor and the answer
    :return: A tuple containing (problemString, correctAnswer)
    """
    # Step 1: Pick a random divisor and a random answer
    divisor = random.randint(minVal, maxVal)
    correctAnswer = random.randint(minVal, maxVal)

    # Step 2: Multiply them to get the starting number (dividend)
    dividend = divisor * correctAnswer

    # Step 3: Create the string so the user sees dividend / divisor
    problemString = f"{dividend} / {divisor}"

    return problemString, correctAnswer


def generateProblem(difficultyLevel):
    """
    Generates a random math problem based on the chosen difficulty.

    :param difficultyLevel: string ('easy', 'medium', or 'hard')
    :return: A tuple containing (problemString, correctAnswer)
    """
    # Step 1: Set the ranges based on the rubric's difficulty scaling
    if difficultyLevel == 'easy':
        minVal, maxVal = 1, 10
    elif difficultyLevel == 'medium':
        minVal, maxVal = 1, 50
    elif difficultyLevel == 'hard':
        minVal, maxVal = 1, 100
    else:
        # A safety fallback just in case the Student sends a weird input
        minVal, maxVal = 1, 10

    # Step 2: Randomly pick one of the four operations
    operations = ['add', 'subtract', 'multiply', 'divide']
    chosenOperation = random.choice(operations)

    # Step 3: Call the correct helper function and return its result
    if chosenOperation == 'add':
        return generateAddition(minVal, maxVal)
    elif chosenOperation == 'subtract':
        return generateSubtraction(minVal, maxVal)
    elif chosenOperation == 'multiply':
        return generateMultiplication(minVal, maxVal)
    elif chosenOperation == 'divide':
        return generateDivision(minVal, maxVal)
