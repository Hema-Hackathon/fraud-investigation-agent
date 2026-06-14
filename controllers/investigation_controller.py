from services.query_processor import (
    process_query
)


def handle_query(query: str):

    intent_data = process_query(query)

    return intent_data

    