def ask_question(question_text):
    """Asks a question a return the answer from the input"""
    return input (f"{question_text} ?: ")

def check_answer(answer, correct_answer):
    """Checks the aswer against the correct answer. Return bool value """
    return answer == correct_answer

def show_feedback(is_correct):
    """Based on the feedack (is_correct) the returnd value is either "Riktig svar" or "Feil svar" """
    if is_correct:
        return "Riktig svar!"
    else:
        return "Feil svar!"