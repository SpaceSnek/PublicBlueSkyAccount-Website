from flask import Flask, render_template, request
from atproto import Client
from dotenv import load_dotenv
import os

app = Flask(__name__)

def CreatePost(user_input):
    load_dotenv()
    username = os.environ.get("BSky-username")
    password = os.environ.get("BSky-password")
    client = Client()
    client.login(username, password)
    client.send_post(user_input)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def process_text():
    if request.method == 'POST':
        user_input = request.form['user_text'] # Access the input using its name attribute
        CreatePost(user_input)
        success_message = f"Your message: {user_input} has been posted successfully!"
        return render_template('submit.html', message=success_message)

if __name__ == '__main__':
    app.run(debug=True)