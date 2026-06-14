import os

def is_llm_available():
    return (
        os.getenv("OPENAI_API_KEY")
        is not None
    )