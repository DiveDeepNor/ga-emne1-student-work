def read_guess():
    guess = int(input("Guess a number: (1-30) "))
    return guess


def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Correct"
    elif guess < secret_number:
        return "To low"
    else:
        return "To high"


def show_feedback(result):
    """Print correct/low/high-guess.feedback
    to the player"""
    if result == "Correct":
        print ("Correct!")
    elif result == "To low":
        print ("Too low!")
    elif result == "To high":
        print ("Too high!")
    else:
        print(f'"error, invalid result: "{result}"')