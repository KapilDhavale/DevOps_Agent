# llm_interface.py

import os
from dotenv import load_dotenv

try:
    from ollama import Client
except ImportError:
    raise ImportError(
        "The 'ollama' module is not installed.\n"
        "Run this command in your virtual environment:\n"
        "   pip install ollama"
    )

# Load environment variables from .env file
load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "codellama:7b-instruct-q4_K_M")
client = Client(host="http://localhost:11434")


def prompt_llm(prompt: str) -> str:
    """
    Sends a prompt to the local Ollama model and returns the response.
    """
    try:
        response = client.generate(
            model=OLLAMA_MODEL,
            prompt=prompt,
            stream=False,
            options={
                "temperature": 0.3,
                "num_predict": 256
            }
        )
        return response['response'].strip()
    except Exception as e:
        return f"❌ Error communicating with Ollama: {str(e)}"


# Optional standalone test
if __name__ == "__main__":
    test_prompt = "Write a Python function to calculate Fibonacci numbers."
    print("Prompt:", test_prompt)
    print("Response:", prompt_llm(test_prompt))
