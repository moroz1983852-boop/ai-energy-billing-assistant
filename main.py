from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from contextlib import asynccontextmanager

from database import init_db, get_customer_debts, add_new_customer
from ai_assistent import generate_billing_response

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="AI Energy Assistant Server", lifespan=lifespan)


@app.get("/debts/{email}")
def check_debts(email: str):
    data = get_customer_debts(email)
    if data is None:
        return {"error": f"Customer with email {email} not found."}
    return data

@app.get("/ask-ai/{email}")
def ask_ai_assitstant(email: str):
    data = get_customer_debts(email)
    if data is None:
        return {"error": f"Customer with email {email} not found."}
    ai_text = generate_billing_response(data["name"], data["total_debt"])
    return {"assistant_response": ai_text}

class CustomerCreate(BaseModel):
    name: str
    email: str

@app.post("/add-customer")
def create_customer(customer: CustomerCreate):
    result = add_new_customer(customer.name, customer.email)
    return result

app.mount("/", StaticFiles(directory="static", html=True), name="static")