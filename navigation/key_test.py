import requests
import json

# Replace with your OpenRouteService API key
API_KEY = "#API_Key_Here"

# OpenRouteService API endpoint for directions
API_URL = "https://api.openrouteservice.org/v2/directions/driving-car"

# Coordinates for the start and end points
start_coords = [76.712615, 9.939092]  # Start location (longitude, latitude)
end_coords = [76.332486, 9.956297]    # End location (longitude, latitude)

# Request body (JSON format)
data = {
    "coordinates": [start_coords, end_coords]
}

# Headers for the API request
headers = {
    "Authorization": API_KEY,
    "Content-Type": "application/json; charset=utf-8"
}

# Make the API request
try:
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the JSON response
    data = response.json()

    # Display the navigation data
    print("Navigation Data:")
    print("Distance:", data["routes"][0]["summary"]["distance"], "meters")
    print("Duration:", data["routes"][0]["summary"]["duration"], "seconds")
    print("Steps:")
    for step in data["routes"][0]["segments"][0]["steps"]:
        print(f"- {step['instruction']} ({step['distance']} meters)")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")
except KeyError:
    print("Invalid API key or coordinates. Please check your input.")