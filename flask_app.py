
# import streamlit as st
# import subprocess
# import atexit
# import requests

# # Import the Flask app from another file
# from flask_app import app

# # Run the Flask app as a background process
# flask_process = subprocess.Popen(["flask", "run", "--port=8888"])

# # Register a function to terminate the Flask process when Streamlit exits
# def kill_flask():
#     flask_process.terminate()

# atexit.register(kill_flask)

# # Your normal Streamlit app goes here
# st.title("Streamlit and Flask Integration")

# # Fetch the content of the /foo route and display it
# response = requests.get("http://localhost:8888/foo")
# st.write(response.text)
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    # Save the file to a directory
    file.save(os.path.join('uploads', file.filename))
    return 'File uploaded successfully'
