# load db url from the env variable. you can use python-dotenv package

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return {"Status": "Success"}, 200 


# Run the app in port 5000 and in debug mode
if __name__ == '__main__':
    app.run(port=5000, debug=True)