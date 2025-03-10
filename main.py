### this code will be heavily commented on to help me learn and remember the syntax ###
from fastapi import FastAPI     # Import FastAPI to create the API
from fastapi.middleware.cors import CORSMiddleware      #Import CORS to allow frontend requests
from fastapi import Request

# Create an instance of the FastAPI app
app = FastAPI()

# Handle CORS (Cross-Origin Resource Sharing) so the frontend can talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],    # Allows requests from any origin (localhost, other servers, etc.)
    allow_credentials=True,
    allow_methods=["*"],    # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],    # Allows all HTTP headers
)

@app.get("/")
def home():
    return {"message": "Welcome to my API. Use /send-data to post data."}

# This is the API endpoint the fontend will call
@app.post("/send-data")
async def send_data(request: Request):
    body = await request.json()
    text = body.get("text", "")
    print(f"Recieved from frontend: {text}")     # This will appear in the terminal when someone sends data from the frontend
    return {"message": f"You said: {text}"}    # Return a JSON response to the frontend



# To run the backend of the server "uvicorn main:app --reload" in environment & directory terminal
