# Google Maps Clone

A simple Google Maps clone built with Flask, HTML, and CSS.

## Features

- Interactive map interface
- Search locations
- Get current location
- Draggable marker
- Clean and modern UI

## Setup

1. Clone this repository
2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your Google Maps API key:

   ```
   GOOGLE_MAPS_API_KEY=your_api_key_here
   ```

4. Run the application:

   ```
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:5000`

## Getting a Google Maps API Key

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Maps JavaScript API
4. Create credentials (API key)
5. Add the API key to your `.env` file

## Note

Make sure to keep your API key secure and never commit it to version control.
