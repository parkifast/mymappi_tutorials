import random
import requests
import os, json

# SCRIPT PARAMETERS
BASE_URL = "https://api.mymappi.com/v1/directions/matrix/"
PROFILE = "car/"
APIKEY = "2300bc7b-1ba0-4c7b-8336-c9a2cff48a99"
ANNOTATIONS = "duration,distance"
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
    return BASE_URL + PROFILE + coordinates[:len(coordinates)-1] + "?apikey=" + APIKEY + "&destinations=" + destinations[:len(destinations)-1] + "&sources=" + sources[:len(sources)-1] + "&annotations=" + ANNOTATIONS

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
r = requests.get(generate_url())
response = r.json()

matrix = {
    "timestamp": response["timestamp"],
    "data": {
        "sources": drivers,
        "destinations": passengers,
        "durations": response["data"]["durations"],
        "distances": response["data"]["distances"],
    }
}

data = {"timestamp": 1605007439,"data": {"sources":[[40.43871056191201,-3.7108465168370945],[40.438851825209454,-3.6818973265756565],[40.43727428465753,-3.700126460783412],[40.42698788151344,-3.7061092312349646],[40.418527110759335,-3.6824172388098635],[40.437761962690395,-3.683206076649443],[40.436074690982885,-3.7027540001252537],[40.43677273078681,-3.6822265498141418]], "destinations":[[40.41826332937495,-3.711152885700495],[40.41878541533847,-3.7006849874443493],[40.4275920055038,-3.7050225902626486],[40.42075366840505,-3.6873847037798066],[40.4181750475997,-3.688452843710744],[40.437988176503424,-3.6960201188475494],[40.43503311090895,-3.69718215521498],[40.43701483928551,-3.69523147561721]], "data":[[542.3,451.8,236.9,410.3,472.8,126.5,154.3,187.1],[725.5,407.3,395.1,309.8,368.5,226.1,210.3,181.1],[590.6,404,260.2,362.5,425,56.9,93.4,117.5],[374,275.4,24.9,299.9,362.4,227.7,159.8,233.8],[684.3,366.1,353.9,268.6,327.3,184.8,169.1,139.8],[702.3,318.6,428.7,166.1,252.1,424.3,365.6,380.7],[499.5,384,169.1,342.5,405,167.3,99.4,183],[673.8,354.8,343.4,216.5,322.2,255,174.6,190.8]]}}
with open(os.path.join('..','database','allocations.json'), "w") as outfile:
    json.dump(data, outfile)


# print(min(min(durations)))
# print(durations.index(min(durations)))
# print(durations.index(min(min(durations))))
# Allocate drivers and passengers

# Populate allocations txt: Timestamp, driver_id, driver_latitude, driver_longitude, passenger_id, passenger_latitude, passenger_longitude, duration, distance

# Populate matrix txt: Timestamp, sources, destinations, durations, distances
# {
#   timestamp: 1605007438,
#   sources: [],
#   destinations: [],
#   durations: [],
#   distances: []
# } 

def perform_allocate():
    print("Hello")