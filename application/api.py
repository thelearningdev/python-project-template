from application.app import app

@app.route("/")
def home():
    return {"Status": "Success"}, 200 

