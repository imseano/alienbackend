import os
from langchain_cerebras import ChatCerebras
from pydantic import SecretStr
from dotenv import load_dotenv

load_dotenv()

class Cerebras:
    def __init__(self):
     api_key = os.environ.get("CEREBRAS_API_KEY")
     safe_api = SecretStr(api_key) if api_key else None

     self.client = ChatCerebras(
       # This is the default and can be omitted
        api_key=safe_api,
        model="llama-4-scout-17b-16e-instruct",
    )
