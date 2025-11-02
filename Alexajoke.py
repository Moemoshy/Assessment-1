# Exercise 2 - Alexa tell me a Joke
# Your solution must be no more than 100 lines of code.
# The randomJokes.txt file in the resources folder contains a dataset of random jokes.
# Each joke is on a new line and consists of a setup and punchline separated by a question mark.
# For example:
# - Why did the chicken cross the road?To get to the other side.
# - What happens if you boil a clown?You get a laughing stock.
# Write a program that when prompted with the phrase "Alexa tell me a Joke" responds with a 
# random joke from the dataset. The program should first present the setup then allow the user 
# to enter a key to display the punchline.
# The user should be able to continue requesting new jokes until they decide to quit the program.

def file_handle_jokes():
    jokes = []
    try:
        with open("jokes.txt", "r", encoding="utf-8") as file: #open the text file
            for line in file: # For loop to loop through each line in the file.
                line = line.strip() 
                if "?" in line: #Checks if the line has a "?"
                    parts = line.split("?", 1) # Splits the "?" to the answer. "1" means to split it once. "?" is removed because of the split.
                    setup = parts[0].strip() + "?" # Add the question mark back.
                    punchline = parts[1].strip() #Removes unwanted space.
                    jokes.append((setup, punchline)) #Stroes in the tuple jokes = []
    except FileNotFoundError:
        print("Error: The file 'jokes.txt' was not found.")
    return jokes


def alexa(joke):
    setup, punchline = joke
    print("\nAlexa:", setup)
    input("\n(Press Enter to hear the punchline...)\n")
    print("Alexa:", punchline)
    print()


def main():
    jokes = file_handle_jokes()

    if not jokes:
        print("No jokes found in jokes.txt.")
        return

    print("Type 'Alexa tell me a joke' to hear one, or 'quit' to exit.\n")

    index = 0 # Counts jokes. 0 means we're at the first one. Everything will be stored in the tuple.
    while True:
        user_input = input("You: ").strip().lower() #removes unwanted space and makes everything lowercase for uniformity.

        if user_input == "quit":
            print("\nAlexa: Thank you! Ask more jokes later.")
            break

        elif user_input == "alexa tell me a joke": # Makes sure all jokes are used, it doesn't repeat until all of them are opened.
            if index < len(jokes):
                alexa(jokes[index])
                index += 1
            else:
                print("Alexa: I don't have jokes anymore\n")

        else:
            print("Alexa: INVALID. TYPE 'Alexa tell me a joke'.\n")


