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

    # Extract the value of "id"
    msg = [alert['annotations']['msg'] for alert in data.get('alerts', [])]
    print(f"Extracted ids: {msg}")

    # Optionally, send a message to the USER_ID with the extracted ids
    if msg:
        for msg_value in msg:
            bot.send_message(USER_ID, f"Extracted id: {msg_value}")

    return jsonify({"message": "Message sent to the user!", "msg": msg}), 200

# Start the Flask web server on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
