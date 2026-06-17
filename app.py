from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from controllers.investigation_controller import handle_query

from services.analytics_service import (
get_suspicious_customers,
get_crypto_transactions,
get_high_value_transactions
)

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)




app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):

    suspicious_count = len(
        get_suspicious_customers()
    )

    crypto_count = len(
        get_crypto_transactions()
    )

    high_value_count = len(
        get_high_value_transactions()
    )

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "suspicious_count": suspicious_count,
            "crypto_count": crypto_count,
            "high_value_count": high_value_count
        }
    )

@app.post("/investigate")
async def investigate(
    request: Request,
    query: str = Form(...)
):

    result = handle_query(query)

    return templates.TemplateResponse(
        "workbench.html",
        {
            "request": request,
            "result": result,
            "query": query
        }
    )
