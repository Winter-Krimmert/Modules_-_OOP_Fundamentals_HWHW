# Mood responses.py

def mood_response(mood):

    if mood.lower() == "happy":
        return "Great to hear that you are happy!"
    elif mood.lower() == "sad":
        return " I'm sorry to hear that you are feeling sad."
    elif mood.lower() == "angry":
        return "Take a deep breathe and try to relax."
    else:
        return "I'm not sure how to respond to that mood."