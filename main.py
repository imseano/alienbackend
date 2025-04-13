import os
import json
from typing import List
from langchain_cerebras import ChatCerebras
from pydantic import SecretStr, BaseModel, Field
from alien import Alien, build_internal_prompt
from dotenv import load_dotenv
from llmclient import Cerebras

load_dotenv()

api_key = os.environ.get("CEREBRAS_API_KEY")
safe_api = SecretStr(api_key) if api_key else None

client = Cerebras().client 
known_words = ["yes", "no", "you", "me", "help", "danger", "safe", "friend", "enemy"]


robert = Alien(known_words, "funny", "destroy Earth", client)

robert_prompt = build_internal_prompt("Why are you here?", robert)

class AlienResponse(BaseModel):
    reasoning: str = Field(description="Reasoning for the response.")
    new_fear: float = Field(description="New fear level after the response.")
    response: str = Field(description="The response.")

structured_llm = client.with_structured_output(AlienResponse)

messages=[
        (
            "user",
            robert_prompt,
        ),
]

try:

    reply = structured_llm.invoke(robert_prompt)
except Exception as e:
    print("Structured call failed, falling back to manual parsing.")
    reply = client.invoke(robert_prompt)

print(reply.content)

# Parse JSON response from LLM
#parsed = json.loads(reply.content)

#print(parsed)
