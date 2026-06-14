from services.llm_service import (
    is_llm_available
)

from services.query_interpreter import (
    interpret_query
)


def process_query(query):

    if is_llm_available():

        print(
            "Using LLM Orchestrator"
        )

        return llm_interpret_query(
            query
        )

    else:

        print(
            "Using Query Interpreter"
        )

        return interpret_query(
            query
        )