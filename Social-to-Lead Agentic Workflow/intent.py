def detect_intent(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(word in user_input for word in ["price", "pricing", "plan", "cost"]):
        return "inquiry"

    elif any(word in user_input for word in ["buy", "subscribe", "want", "try", "sign up"]):
        return "high_intent"

    return "unknown"