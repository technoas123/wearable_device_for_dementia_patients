import serial
import time
import pynmea2
import openrouteservice
from math import radians, sin, cos, sqrt, atan2

# API Key from OpenRouteService
API_KEY = "#API_Key_Here"

# Define frequent locations (latitude, longitude)
locations = {
    "Home": (12.9716, 77.5946),  # Example coordinates
    "Hospital": (12.9352, 77.6245)
}

# Initialize OpenRouteService client
client = openrouteservice.Client(key=API_KEY)

# Function to calculate distance using Haversine formula
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth's radius in km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2) * sin(dlat/2) + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2) * sin(dlon/2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c  # Distance in km

# Function to find the closest location
def get_closest_location(lat, lon):
    min_distance = float("inf")
    closest_place = None
    
    for place, (lat2, lon2) in locations.items():
        distance = calculate_distance(lat, lon, lat2, lon2)
        if distance < min_distance:
            min_distance = distance
            closest_place = place
    
    return closest_place, locations[closest_place], min_distance

# Function to get route from OpenRouteService
def get_route(start, end):
    try:
        route = client.directions(
            coordinates=[start, end],
            profile='foot-walking',  # Change to 'driving-car' if needed
            format='geojson'
        )
        return route['features'][0]['properties']['segments'][0]['steps']
    except Exception as e:
        print(f"Error fetching route: {e}")
        return None

# Open serial port for GPS module
gps_serial = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)

# Main loop to read GPS data and navigate
while True:
    try:
        line = gps_serial.readline().decode("utf-8", errors="ignore")
        
        if line.startswith("$GPGGA") or line.startswith("$GPRMC"):
            msg = pynmea2.parse(line)
            lat = msg.latitude
            lon = msg.longitude
            
            if lat and lon:
                print(f"Current Location: {lat}, {lon}")
                
                # Find the nearest stored location
                closest_place, (dest_lat, dest_lon), distance = get_closest_location(lat, lon)
                print(f"Closest Location: {closest_place} ({distance:.2f} km away)")

                # Fetch navigation route
                steps = get_route([lon, lat], [dest_lon, dest_lat])
                if steps:
                    print(f"Navigation Steps to {closest_place}:")
                    for step in steps:
                        print(f"{step['instruction']} ({step['distance']} meters)")
        
        time.sleep(2)
    
    except Exception as e:
        print(f"Error: {e}")