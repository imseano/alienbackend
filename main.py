import os
from langchain_cerebras import ChatCerebras
from pydantic import SecretStr, BaseModel
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("CEREBRAS_API_KEY")
safe_api = SecretStr(api_key) if api_key else None

client = ChatCerebras(
    # This is the default and can be omitted
    api_key=safe_api,
 model="llama-4-scout-17b-16e-instruct",
)

messages=[
        (
            "user",
            "You are an alien from a distant planet. You came here on your spaceship to destroy Earth. You can understand human speech but you have a limited vocabulary, only being able to say the following words: hello, goodbye, please, kill, mock, steel, Italy. A diplomat has arrived from Earth and you must try to convince them that you are of no threat, disguising your intentions if you wish to destroy the earth. What do you say? Keep in mind you may only say up to 3 words at a time from your vocabulary for each sentence.",
        ),
]

reply = client.invoke(messages)

print(reply.content)
