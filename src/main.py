import json
import re
from alien import Alien, build_internal_prompt
from llmclient import Cerebras

client = Cerebras().client 
known_words = ["yes", "no", "you", "me", "help", "danger", "safe", "friend", "enemy"]


robert = Alien(known_words, "funny", "destroy Earth", client)

robert_prompt = build_internal_prompt("Why are you here?", robert)
messages=[
        (
            "user",
            robert_prompt,
        ),
]


reply = client.invoke(robert_prompt)

def extract_json_from_text(text: str):
    try:
        # Match the first full JSON object in the text
        json_match = re.search(r"\{.*?\}", text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(0))
    except json.JSONDecodeError as e:
        print("JSON decode error:", e)
    return None

json_data = extract_json_from_text(reply.content)

print(json_data)

print(json_data['response'])
