# Import libraries
from flask import Flask, request

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data

#set home
@app.route('/')
def home():
    return "Homepage"
# Read operation

# Create operation

# Update operation

# Delete operation

# Run the Flask app
if __name__ == "__main__":
    app.run()
    