import random
import requests

# SCRIPT PARAMETERS
BASE_URL = "https://api.mymappi.com/v1/directions/matrix/"
PROFILE = "car/"
APIKEY = "2300bc7b-1ba0-4c7b-8336-c9a2cff48a99"
ANNOTATIONS = "duration"
N = random.randint(3,8)
BOUNDING_BOX = [40.4179, 40.4389, -3.7242, -3.6768]

# SCRIPT VARIABLES
passengers = []
drivers = []

# SCRIPT FUNCIONS
def generate_location():
    return [random.uniform(BOUNDING_BOX[0], BOUNDING_BOX[1]), random.uniform(BOUNDING_BOX[2], BOUNDING_BOX[3])]

def generate_url():
    # Auxiliar variables
    coordinates = ""
    sources = ""
    destinations = ""
    # Generate strings
    for passenger in passengers:
        coordinates += str(passenger["coordinates"][0]) + "," + str(passenger["coordinates"][1]) + ";"
    for driver in drivers:
        coordinates += str(driver["coordinates"][0]) + "," + str(driver["coordinates"][1]) + ";"
    for i in range(N):
        # Sources = Drivers
        sources += str(i+N) + ";"
        # Destinations = Passengers
        destinations += str(i) + ";"
    return BASE_URL + PROFILE + coordinates[:len(coordinates)-1] + "?apikey=" + APIKEY + "&sources=" + sources[:len(sources)-1] + "&destinations=" + destinations[:len(destinations)-1] + "&annotations=" + ANNOTATIONS

# DATA GENERATION
print(f'# START EXECUTION #')
# Generate passengers and drivers
for i in range(N):
    passengers.append({
        "id": "passenger-" + str(i),
        "coordinates": generate_location()
    })
    drivers.append({
        "id": "driver-" + str(i),
        "coordinates": generate_location()
    })
print(f'Generated {N} drivers and {N} passengers. One of them: {passengers[0]}')



# Create and perform request
print(generate_url())
# r = requests.get('https://api.mymappi.com/v1/directions/matrix/car/40.427772%2C-3.714630%3B40.407348%2C-3.710520%3B40.461178%2C-3.676533%3B40.441933%2C-3.650275%3B40.434914%2C-3.697337%3B40.451737%2C-3.683682?apikey=2300bc7b-1ba0-4c7b-8336-c9a2cff48a99&annotations=duration%2Cdistance')
# print(r.status_code)
# print(r.json())

