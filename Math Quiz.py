# Exercise 1 - Maths Quiz
# Your solution must be no more than 250 lines of code.
# Develop a program that presents the user with quiz of arithmetic problems. Each "play" of the quiz should be 10 questions. The user should initially be presented with a short menu of options to select a difficulty level. It could look something like this:

# DIFFICULTY LEVEL
#  1. Easy
#  2. Moderate
#  3. Advanced
# The difficulty levels determine the number of digits in the numbers to be added or subtracted. Easy means only single digit numbers; moderate means double digit numbers; and advanced means 4-digit numbers. After the user picks the level they desire, your program presents problems that look like this:
# 45 + 9 =
# 34 - 88 =
# etc
# For each problem presented, the user is given a chance to answer. If the answer is correct, another problem is presented. If the answer is wrong, the user is to be given one more chance at that problem. The program should keep a tally of the users score, awarding 10 points for a correct answer on first attempt and 5 points on the second attempt. You should implement a random number generator (see the resources folder) to determine:
# •	The values to be added or subtracted
# •	Whether the problem is addition or subtraction
#   The program should include the functions listed below. These functions should make use of parameters and return values as appropriate. You may include others or extend the functionality of the program if you see fit.
# •	displayMenu: A function that displays the difficulty level menu at the beginning of the quiz.
# •	randomInt: A function that determines the values used in each question. The min and max values of the numbers should be based on the difficulty level chosen as described above.
# •	decideOperation: A function that randomly decides whether the problem is an addition or subtraction problem and returns a char.
# •	displayProblem: A function that displays the question to the user and accepts their answer.
# •	isCorrect: A function that checks whether the users answer was correct and outputs an appropriate message
# •	displayResults: function that outputs the users final score out of a possible 100 and ranks the user based on their score (e.g. A+ for a score over 90)
#   Once the user has finished the quiz, prompt them to see if they'd like to play it again.


import random


#displayMenu

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



#randomInt

def randomInt(difficulty):
    if (difficulty) == 1:      
        return random.randint(1, 9)
    elif (difficulty) == 2:    
        return random.randint(10, 99)
    elif (difficulty) == 3:    
        return random.randint(1000, 9999)



#decideOperation

def decideOperation():
    return random.choice(['+', '-']) 



#displayProblem

def displayProblem(num1, num2, op):
    print(f"\nWhat is {num1} {op} {num2}?")
    try:
        answer = int(input("Your answer: "))
        return answer
    except ValueError:
        print("Invalid input. Please enter a number.")
        return displayProblem(num1, num2, op)



#isCorrect

def isCorrect(num1, num2, op, user_answer):
    if op == '+':
        correct = num1 + num2
    else:
        correct = num1 - num2

    if user_answer == correct:
        print("✓ Correct.")
        return True
    else:
        print(f"⨉ Incorrect. The correct answer was {correct}.")
        return False



#displayResults

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



# playQuiz

def playQuiz():
    level = displayMenu()
    score = 0

    for i in range(1, 11):
        num1 = randomInt(level)
        num2 = randomInt(level)
        op = decideOperation()

        # First attempt
        print(f"\nQuestion {i}:")
        answer = displayProblem(num1, num2, op)
        if isCorrect(num1, num2, op, answer):
            score += 10
            continue

        # Second attempt
        print("Try once more!")
        answer = displayProblem(num1, num2, op)
        if isCorrect(num1, num2, op, answer):
            score += 5

    displayResults(score)



# Loop

def main():
    while True:
        playQuiz()
        again = input("\nWould you like to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! Goodbye!")
            break


# Run the program
if __name__ == "__main__":
    main()
