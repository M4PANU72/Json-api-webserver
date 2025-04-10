from flask import Flask



app = Flask(__name__)

@app.get("/")
def root():
    return {"message": "Welkom bij de API!"}


@app.get("/tools")
def get_tools():
    return 