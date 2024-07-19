import os
import telebot
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN', 'token')
USER_ID = os.getenv('USER_ID', 'user_id')

bot = telebot.TeleBot(TOKEN)

# Create a Flask web server
app = Flask(__name__)

# Define a route for the web server that accepts POST requests
@app.route('/', methods=['POST'])
def send_message():
    data = request.json
    print(f"Received POST data: {data}")

    # Extract the value of "msg"
    messages = [alert['annotations']['msg'] for alert in data.get('alerts', []) if 'msg' in alert['annotations']]
    print(f"Extracted messages: {messages}")

    # Optionally, send a message to the USER_ID with the extracted messages
    if messages:
        for msg in messages:
            bot.send_message(USER_ID, f"{msg}")

    return jsonify({"message": "Messages sent to the user!", "msgs": messages}), 200

# Start the Flask web server on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
