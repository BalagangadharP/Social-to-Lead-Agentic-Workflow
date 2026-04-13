from intent import detect_intent
from rag import retrieve_answer
from tools import mock_lead_capture


class AgentState:
    def __init__(self):
        self.intent = None
        self.name = None
        self.email = None
        self.platform = None
        self.stage = "start"


def run_agent():
    state = AgentState()

    print("AutoStream Agent: Hello! How can I help you?\n")

    while True:
        user_input = input("You: ")

        # Detect intent only at start
        if state.stage == "start":
            state.intent = detect_intent(user_input)

            if state.intent == "greeting":
                print("Agent: Hello! Ask me anything about AutoStream")

            elif state.intent == "inquiry":
                answer = retrieve_answer(user_input)
                print(f"Agent: {answer}")

            elif state.intent == "high_intent":
                print("Agent: Great! Let's get you started")
                print("Agent: What's your name?")
                state.stage = "get_name"

            else:
                print("Agent: Sorry, I didn't understand that.")

        elif state.stage == "get_name":
            state.name = user_input
            print("Agent: Please provide your email:")
            state.stage = "get_email"

        elif state.stage == "get_email":
            state.email = user_input
            print("Agent: Which platform do you create content on? (YouTube/Instagram/etc.)")
            state.stage = "get_platform"

        elif state.stage == "get_platform":
            state.platform = user_input

            # Call tool ONLY after all inputs
            mock_lead_capture(state.name, state.email, state.platform)

            print("Agent: Thank you! Our team will contact you soon")
            break