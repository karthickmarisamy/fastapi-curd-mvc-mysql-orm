from fastapi import FastAPI
from .utils.response_wrapper import api_response
app = FastAPI()

@app.get('/')
def index():
    return {"success": True}