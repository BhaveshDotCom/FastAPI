from fastapi import FastAPI, Depends, Header, HTTPException, status

app = FastAPI()

# Dependency
def get_db():
    return "Database Connection"

@app.get("/")
def home(db = Depends(get_db)):
    return {
        "db" : db
    }

# Dependency Injection promotes reusable logic

def verify_token(token:str=Header(None)):
    if token != "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9":
        raise HTTPException (
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="UNAUTHORIZED ACCESS",
        )
    return {
        "is_access_granted" : True
    } 

@app.get("/dashboard")
def get_dashboard(verify = Depends(verify_token)):
    return {
        "message" : "Welcome",
        "is_verified" : verify
    }

@app.get("/profile")
def get_dashboard(name:str, verify = Depends(verify_token)):
    return {
        "name" : name,
        "is_verified" : verify
    }