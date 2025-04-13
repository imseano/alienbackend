from langchain_cerebras import ChatCerebras

class Alien:
    def __init__(self, known_words, personality, motive, llm):
        self.known_words = known_words
        self.personality = personality
        self.motive = motive
        self.stress = 0
        self.llm = llm


def build_internal_prompt(player_input: str, state: Alien) -> str:
    return f"""
    You are an alien communicating with a human diplomat. You understand them fully, but can only respond using these words:
    {state.known_words}

    Your personality is: {state.personality}
    Your motive is: {state.motive}
    Your current fear level is: {state.stress:.2f}

    The human said: "{player_input}"

    Decide:
    1. What you are thinking.
    2. How your fear level changes.
    3. What word(s) to say from your vocabulary.

    Reply **only** in JSON format like this (do not add commentary or explanation):

    {{
      "reasoning": "<what you're thinking and why>",
      "new_fear": <new fear level as a float>,
      "response": "<your chosen word(s) from the vocabulary in string form>"
    }}
    """ 



