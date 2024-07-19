import os
import telebot
from flask import Flask, request, jsonify
from dotenv import load_dotenv
TOKEN = os.getenv('TOKEN', 'token')
USER_ID = os.getenv('USER_ID', 'uid')

load_dotenv()
bot = telebot.TeleBot(TOKEN)

# Create a Flask web server
app = Flask(__name__)

# Define a route for the web server that accepts POST requests
@app.route('/', methods=['POST'])
def send_message():
    data = request.json
    print(f"Received POST data: {data}")

    # Optionally, send a message to the USER_ID with the received data
    bot.send_message(USER_ID, f"Received data: {data}")

    return jsonify({"message": "Message sent to the user!", "data_received": data}), 200

# Start the Flask web server on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
