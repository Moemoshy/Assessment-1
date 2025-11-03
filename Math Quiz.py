import random

# Display Menu
def displayMenu():
    print("\nDIFFICULTY LEVEL")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")
    while True:
        choice = input("Choose your difficulty (1-3): ")
        if choice in ["1", "2", "3"]:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# Generate random numbers based on difficulty
def randomInt(difficulty):
    if difficulty == 1:
        return random.randint(1, 9)
    elif difficulty == 2:
        return random.randint(10, 99)
    elif difficulty == 3:
        return random.randint(1000, 9999)


# Decide operation (+ or -)
def decideOperation():
    return random.choice(['+', '-'])


# Display problem and get user answer
def displayProblem(num1, num2, op):
    while True:
        try:
            answer = int(input(f"\nWhat is {num1} {op} {num2}? Your answer: "))
            return answer
        except ValueError:
            print("Invalid input. Please enter a number.")


# Check answer
def isCorrect(num1, num2, op, user_answer):
    correct = num1 + num2 if op == '+' else num1 - num2
    if user_answer == correct:
        print("✓ Correct.")
        return True
    else:
        print("⨉ Incorrect.")
        return False, correct  # return the correct answer for second attempt


# Display final results
def displayResults(score):
    print("\n-----------------------------------")
    print(f"Final Score: {score}/100")

    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"Grade: {grade}")
    print("-----------------------------------")


# Play the quiz
def playQuiz():
    level = displayMenu()
    score = 0

    for i in range(1, 11):
        num1 = randomInt(level)
        num2 = randomInt(level)
        op = decideOperation()
        correct_answer = num1 + num2 if op == '+' else num1 - num2

        print(f"\nQuestion {i}:")
        # First attempt
        answer = displayProblem(num1, num2, op)
        result = isCorrect(num1, num2, op, answer)
        if result is True:
            score += 10
            continue

        # Second attempt
        print("Try once more!")
        answer = displayProblem(num1, num2, op)
        result = isCorrect(num1, num2, op, answer)
        if result is True:
            score += 5
        else:
            # Show correct answer after second wrong attempt
            print(f"The correct answer was {correct_answer}.")

    displayResults(score)


# Main loop
def main():
    while True:
        playQuiz()
        again = input("\nWould you like to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
