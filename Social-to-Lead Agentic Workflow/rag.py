import json

with open("knowledge_base.json") as f:
    kb = json.load(f)

def retrieve_answer(query):
    query = query.lower()

    if "price" in query or "plan" in query:
        return f"{kb['pricing']['basic']}\n{kb['pricing']['pro']}"

    elif "refund" in query:
        return kb["policies"]["refund"]

    elif "support" in query:
        return kb["policies"]["support"]

    return "Sorry, I couldn't find that information."