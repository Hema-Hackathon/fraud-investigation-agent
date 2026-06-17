from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from controllers.investigation_controller import handle_query
import pandas as pd

from services.analytics_service import (
get_suspicious_customers,
get_crypto_transactions,
get_high_value_transactions
)
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

    top_customers = get_suspicious_customers()[:5]

    crypto_transactions = get_crypto_transactions()

    high_value_transactions = (
        get_high_value_transactions()
    )

    transactions = pd.read_csv(
    "data/transactions.csv"
    )

    dashboard_rows = []
    
    for customer in top_customers:
    
        customer_txns = transactions[
            transactions["customer_id"]
            == customer["customer_id"]
        ]
    
        latest_date = "N/A"
    
        if not customer_txns.empty:
    
            latest_date = (
                customer_txns
                .sort_values(
                    by="timestamp",
                    ascending=False
                )
                .iloc[0]["timestamp"]
            )
    
        dashboard_rows.append({
            "customer": customer,
            "last_activity": latest_date
        })

    suspicious_count = len(
        top_customers
    )

    crypto_count = len(
        crypto_transactions
    )

    high_value_count = len(
        high_value_transactions
    )

    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "suspicious_count": suspicious_count,
            "crypto_count": crypto_count,
            "high_value_count": high_value_count,

            "top_customers": top_customers,

            "top_crypto_transactions":
                crypto_transactions[:3],

            "top_high_value_transactions":
                high_value_transactions[:3],
            "dashboard_rows": dashboard_rows
        }
    )

@app.post("/investigate")
async def investigate(
    request: Request,
    query: str = Form(...)
):

    result = handle_query(query)

    print(result)
    
    return templates.TemplateResponse(
        "workbench.html",
        {
            "request": request,
            "result": result,
            "query": query
        }
    )
