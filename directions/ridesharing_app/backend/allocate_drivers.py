# SCRIPT IMPORTS
import random
import requests
import os, json
import numpy as np

# SCRIPT PARAMETERS
# url: more info in https://api.mymappi.com/docs
BASE_URL = "https://api.mymappi.com/v1/directions/matrix/"
PROFILE = "car/"
APIKEY = <YOUR_API_KEY>
ANNOTATIONS = "duration,distance"
# Number of passengers and drivers
N = random.randint(3,8)
# Area where passengers and drivers will be generated
BOUNDING_BOX = [40.4179, 40.4389, -3.7242, -3.6768]

# SCRIPT VARIABLES
passengers = []
drivers = []
allocations = []

# SCRIPT FUNCTIONS
# Generate random location (latitude and longitude) from bounding box defined.
def generate_locations():
    return [random.uniform(BOUNDING_BOX[0], BOUNDING_BOX[1]), random.uniform(BOUNDING_BOX[2], BOUNDING_BOX[3])]

# Compose mymappi matrix api url to request duration and distance
# for every combination of passengers and drivers
def compose_matrix_url():
    # Auxiliar variables to concatenate strings
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

# Return the position (row and column) in a matrix of the minimum travel duration found
def minimum_travel_position(m, value):
    return np.argwhere(m==value)

# Return the position (row) of the driver in a matrix
def matrix_driver_position(m):
    return np.argmin(np.transpose(m.min(axis=1)), axis=1)[0,0]

# Return the position (column) of the passenger in a matrix
def matrix_passenger_position(m):
    return np.argmin(np.transpose(m.min(axis=0)), axis=0)[0,0]




# -- MAIN SCRIPT EXECUTION -- #
# DATA GENERATION
# Generate passengers and drivers
for i in range(N):
    passengers.append({
        "id": "passenger-" + str(i),
        "coordinates": generate_locations() 
    })
    drivers.append({
        "id": "driver-" + str(i),
        "coordinates": generate_locations()
    })
print(f"Generated {N} drivers and passengers.")
print(f"One of them: {passengers[0]}")

# Once drivers and passengers are generated, request distance and duration matrix 
# Compose and perform request
r = requests.get(compose_matrix_url())
response = r.json()

# Sample request
#
# response = {
#   "status":"OK",
#   "version":"1.0",
#   "provider":"mymappi API 1.0",
#   "timestamp":1605781265,
#   "copyright":"The data included in this document is from www.mymappi.com. The data is strictly forbidden to be cached, read our terms and conditions in https:\/\/mymappi.com\/myapi\/legal.",
#   "next":"",
#   "data":{"code":"Ok",
#       "distances":[[2449.7,1118.5,2599.4,2499,146.9,3183,2650.1,2718.4], ...],
#       "durations":[[344.6,148.9,356.7,284.6,30.5,362.7,322.7,379.7], ... ],
#       "sources":[{"hint":"c_1ggHX9YIAMAAAAXwAAAAkAAAAIAAAA_5OgQBl9HkKR-mlAmLdZQAwAAABfAAAACQAAAAgAAADfFQAAJ2HH_7f7aAI2Ycf_cvxoAgEAHxFHO5za", ... ],
#       "destinations":[{"hint":"NvZggP___3_TAAAAAQEAAAAAAAAUAAAA3tC8QjVToUEAAAAAqmYQQdMAAAABAQAAAAAAABQAAADfFQAAN27H_3nMaAJHbsf_lMxoAgAAbxJHO5za", ... ]
#   }
# }

# Get response duration information. We could use distance or both to our calculations.
durations = response["data"]["durations"]

# Using numpy library to transform a bidimensional array to a matrix
# to use specific library matrix-friendly functions
durations_matrix = np.asmatrix(durations)           # It will be updated when an allocation is found
const_durations_matrix = np.asmatrix(durations)     # To get driver and passenger when an allocation is found

# Loop to allocate drivers and passengers. 
# In every iteration, we will search the minimum travel duration.
for iteration in const_durations_matrix:
    # Find minimum duration time
    m = minimum_travel_position(const_durations_matrix, durations_matrix.min(axis=0).min(axis=1))
    # Find driver and passenger
    d = matrix_driver_position(durations_matrix)
    p = matrix_passenger_position(durations_matrix)
    # Allocate driver and passenger and populate json file
    allocations.append({
        "driver": drivers[m[0,0]],
        "passenger": passengers[m[0,1]],
        "duration": durations_matrix[d,p]
    })
    # Delete driver and passenger from duration_matrix
    durations_matrix = np.delete(durations_matrix, d, 0)
    durations_matrix = np.delete(durations_matrix, p, 1)


# SAVE DATA
# We use json file, but it could be a database.

# Save allocations generated in json files.
# Populate matrix json file: Timestamp, allocation (driver, passenger, duration).
dict_allocations = {
    "timestamp": response["timestamp"],
    "data": allocations
}
with open(os.path.join("..","database","allocations.json"), "w") as outfile:
    json.dump(dict_allocations, outfile)

# Save matrix api response, for example to analyse average travels time.
# Populate matrix json file: Timestamp, sources, destinations, durations, distances.
dict_matrix = {
    "timestamp": response["timestamp"],
    "data": {
        "sources": drivers,
        "destinations": passengers,
        "durations": response["data"]["durations"],
        "distances": response["data"]["distances"],
    }
}
with open(os.path.join("..","database","matrix.json"), "w") as outfile:
    json.dump(dict_matrix, outfile)