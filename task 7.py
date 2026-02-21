from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace this with your actual API key
API_KEY = "e078cd3385a0da779198392b1ce381a2"

@app.route('/weather')
def get_weather():
    # Get latitude and longitude from URL parameters
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    
    if not lat or not lon:
        return jsonify({"error": "Please provide lat and lon parameters"}), 400
    
    # API URL using lat/lon
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Check for errors from OpenWeatherMap
        if response.status_code != 200:
            return jsonify({"error": data.get("message", "Invalid request")}), response.status_code
        
        # Return only the relevant info
        return jsonify({
            "Latitude": lat,
            "Longitude": lon,
            "Temperature": data["main"]["temp"],
            "Description": data["weather"][0]["description"]
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)