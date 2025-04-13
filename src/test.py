from typing import List, Optional
from langchain_cerebras import ChatCerebras
from langchain_core.pydantic_v1 import BaseModel, Field
from alien import Alien, build_internal_prompt
from llmclient import Cerebras
from dotenv import load_dotenv

client = Cerebras().client

class Joke(BaseModel):
    '''Joke to tell user.'''

    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline to the joke")
    rating: Optional[int] = Field(description="How funny the joke is, from 1 to 10")

structured_llm = client.with_structured_output(Joke)

reply = structured_llm.invoke("Tell me a joke about cats")
print(reply.content)

# Parse JSON response from LLM
#parsed = json.loads(reply.content)

#print(parsed)
