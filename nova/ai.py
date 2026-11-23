import os

from dotenv import load_dotenv
from openai import OpenAI, APIConnectionError, APIStatusError, RateLimitError

conversation_history = []

MAX_HISTORY = 10


# Load environment variables from .env
load_dotenv()


def get_ai_response(message: str) -> str:
    """
    Send a message to the AI model and maintain conversation history.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "API key is missing."

    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    conversation_history.append({
        "role": "user",
        "content": message
    })

    try:
        client = OpenAI(api_key=api_key)

        response = client.responses.create(
            model=model,
            instructions=(
                "You are NOVA, a helpful personal assistant. "
                "Give clear, friendly and easy-to-understand answers."
            ),
            input=conversation_history
        )

        ai_message = response.output_text.strip()

        conversation_history.append({
            "role": "assistant",
            "content": ai_message
        })
        conversation_history[:] = conversation_history[-MAX_HISTORY:]

        return ai_message

    except Exception:
        conversation_history.pop()

        return "Sorry, I couldn't process your request right now."
    
def clear_memory():
    """
    Clear NOVA's conversation history.
    """

    conversation_history.clear()

    return "Conversation memory cleared successfully."