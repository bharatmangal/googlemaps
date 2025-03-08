from flask import Flask, render_template
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    # Get the Google Maps API key from environment variable
    maps_api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    return render_template('index.html', maps_api_key=maps_api_key)

if __name__ == '__main__':
    app.run(debug=True) 