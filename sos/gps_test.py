import serial
import pynmea2

# Set up serial connection
ser = serial.Serial('/dev/serial0', baudrate=9600, timeout=1)

try:
    while True:
        # Read a line of data from the GPS module
        data = ser.readline().decode('utf-8', errors='ignore')
        
        # Check if the data is a valid NMEA sentence
        if data.startswith('$GPGGA'):
            # Parse the NMEA sentence
            msg = pynmea2.parse(data)
            
            # Extract and print GPS data
            print(f"Time: {msg.timestamp}")
            print(f"Latitude: {msg.latitude} {msg.lat_dir}")
            print(f"Longitude: {msg.longitude} {msg.lon_dir}")
            print(f"Altitude: {msg.altitude} {msg.altitude_units}")
            print(f"Satellites: {msg.num_sats}")
            print("-----------------------------")

except KeyboardInterrupt:
    print("Exiting...")
finally:
    ser.close()