
class Alien:
    def __init__(self, known_words, personality, motive, llm):
        self.known_words = known_words
        self.personality = personality
        self.motive = motive
        self.stress = 0
        self.llm = llm

    def generate_response(self, message):
        prompt = build_internal_prompt(message, self)
        return self.llm.invoke(prompt)

    def learn_vocab(self, word):
        self.known_words.append(word)

    def calculate_stress_change(self, emotion):
        if emotion == "happy":
            self.stress -= 5
            if (self.stress < 0): self.stress = 0
        elif emotion == "angry":
            self.stress += 10




def build_internal_prompt(player_input: str, state: Alien) -> str:
    return f"""
    You are an alien communicating with a human diplomat. You understand them fully, but can only respond using these words:
    {state.known_words}

    Your personality is: {state.personality}
    Your motive is: {state.motive}
    Your current stress level is: {state.stress:.2f}. If the human says something that makes you angry, your stress level will increase by up to 10.
    If your stress is 50 or more, you will say something random in anger. If the human says something that makes you happy, your stress level will decrease by up to 5.

    The human said: "{player_input}"

    Decide:
    1. What you are thinking.
    2. Which emotion in one word did you feel?
    3. What word(s) to say from your vocabulary and what body cues do you use.

    Reply **only** in JSON format like this (do not add commentary or explanation):

    {{
      "reasoning": "<what you're thinking and why>",
      "main_emotion": <happy|angry|neutral|etc>,
      "response": "<your chosen word(s) from the vocabulary in string form alongside any body cues>"
    }}
    """ 



