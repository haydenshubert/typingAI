from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (can restrict it later)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Defining a data model to send data from frontend to backend
class UserInput(BaseModel):
    text: str

@app.post("/send-data")
def send_data(user_input : UserInput):
    print(f"Recieved from frontend: {user_input.text}")
    response = f"You said: {user_input.text}"
    return {"message": response}

# Purpose of this code 
#         V
# 1. It creates and API endpoint (/sent-data) that the frontend can call
# 2. It listens for POST requests from frontend
# 3. It recieves the text input from the frontend and prints it in the terminal
# 4. It sends a resonse back to the frontend

# To run the backend of the server "uvicorn main:app --reload" in environment & directory terminal
