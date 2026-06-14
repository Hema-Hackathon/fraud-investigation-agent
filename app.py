from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

from controllers.investigation_controller import (
    handle_query
)

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def home():

    return """
    <html>
        <body>
            <h1>
                Financial Crime Investigation Agent
            </h1>

            <form action="investigate" method="post">

                <input
                    type="text"
                    name="query"
                    placeholder="Ask a question"
                    style="width:400px"
                >

                <button type="submit">
                    Investigate
                </button>

            </form>

        </body>
    </html>
    """


@app.post("/investigate")
async def investigate_query(
    query: str = Form(...)
):

    result = handle_query(query)

    return result