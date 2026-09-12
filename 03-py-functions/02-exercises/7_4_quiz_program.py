from helpers.quiz_helpers import *

def run_quiz():
    counter = 0

    # Spørsmål 1
    answer = ask_question("Hva heter mannen bak denne koden")
    is_correct = check_answer(answer, "Njaal")
    print(show_feedback(is_correct))

    if is_correct:
        counter += 1

    # Spørsmål 2
    answer = ask_question("Hva hvor gammel er han")
    is_correct = check_answer(answer, "39")
    print(show_feedback(is_correct))

    if is_correct:
        counter += 1

    # Spørsmål 3
    answer = ask_question("Hva hvor bor han")
    is_correct = check_answer(answer, "Kristiansand")
    print(show_feedback(is_correct))

    if is_correct:
        counter += 1


    print(f"Poeng samlet: {counter} av 3 mulige")


run_quiz()



