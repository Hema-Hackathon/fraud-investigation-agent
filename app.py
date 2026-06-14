from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def home():

    return """
    <html>
        <body>
            <h1>
                Financial Crime Investigation Agent
            </h1>

            <input
                type='text'
                placeholder='Ask a question'
            >

            <button>
                Investigate
            </button>

        </body>
    </html>
    """