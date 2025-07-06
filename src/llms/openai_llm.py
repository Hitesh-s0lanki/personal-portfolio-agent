import os
from openai import OpenAI
from dotenv import load_dotenv

class OpenAILLM:
    def __init__(self):
        load_dotenv()        
        self.model_name = "gpt-4o"

    def get_llm_model(self) -> OpenAI:

        os.environ["OPENAI_API_KEY"] = self.api_key = os.getenv("OPENAI_API_KEY")

        if not self.api_key:
            raise ValueError("API key is required to call OpenAI.")

        try:
            llm = OpenAI()
            return llm
        except Exception as e:
            error_msg = f"OpenAI initialization error: {e}"
            raise ValueError(error_msg)