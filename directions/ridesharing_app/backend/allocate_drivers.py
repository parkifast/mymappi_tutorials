import random
import requests
import os, json
import numpy as np

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
allocations = []

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

def find_minimum(m, value):
    return np.argwhere(m==value)

def find_driver(m):
    return np.argmin(np.transpose(m.min(axis=1)), axis=1)[0,0]

def find_passenger(m):
    return np.argmin(np.transpose(m.min(axis=0)), axis=0)[0,0]

# DATA GENERATION
print(f"# START EXECUTION #")
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
print(f"Generated {N} drivers and {N} passengers. One of them: {passengers[0]}")



# Create and perform request
r = requests.get(generate_url())
response = r.json()

# response = {"statxus":"OK","version":"1.0","provider":"mymappi API 1.0","timestamp":1605781265,"copyright":"The data included in this document is from www.mymappi.com. The data is strictly forbidden to be cached, read our terms and conditions in https:\/\/mymappi.com\/myapi\/legal.","next":"","data":{"code":"Ok","distances":[[2449.7,1118.5,2599.4,2499,146.9,3183,2650.1,2718.4],[1025.3,1469.4,2252.6,3450.4,1842.8,1193.3,1079.6,2291.5],[2660.8,2256.4,2032.5,721.4,1878.1,3852.2,2861.1,2151.5],[2387,724.7,2795.8,2638.4,793.5,2789.2,2587.3,2914.8],[2714.9,2074.3,3666.9,3873,2447.7,1852.1,2782.6,3785.8],[4046.3,3616.7,2779.7,1636.5,3221.6,5237.7,4246.6,2898.7],[970.2,1564.4,2090.4,3230.5,1937.8,1316.6,635.7,2129.4],[3871.5,3442,2604.9,1468.1,3053.2,5062.9,4071.9,2723.9]],"durations":[[344.6,148.9,356.7,284.6,30.5,362.7,322.7,379.7],[179.5,175.7,319.4,390.7,195.2,131.6,137.2,331.5],[345.9,266.7,237.3,113,255.4,442.2,324,260.3],[295.4,83.1,332.1,271.5,106.6,296.9,273.5,355.1],[362.5,257.7,426.7,437.3,277.2,186.5,309.8,449.7],[476.8,391.5,326.8,193.4,401.5,573.1,454.9,349.8],[173.8,193.4,312.7,394.6,212.9,163.2,141.9,324.8],[458.5,373.2,308.5,167.8,375.8,554.8,436.6,331.5]],"sources":[{"hint":"c_1ggHX9YIAMAAAAXwAAAAkAAAAIAAAA_5OgQBl9HkKR-mlAmLdZQAwAAABfAAAACQAAAAgAAADfFQAAJ2HH_7f7aAI2Ycf_cvxoAgEAHxFHO5za","distance":20.803638,"location":[-3.710681,40.434615],"name":"Calle Pontevedra"},{"hint":"xMMIgP___39MAAAAYAAAAC4AAABbAAAAnUupQlKgsEGPM-NBrXTJQkwAAABgAAAALgAAAFsAAADfFQAAZlLH_4nGaAKIU8f_m8VoAgIA_wJHO5za","distance":36.112467,"location":[-3.714458,40.421001],"name":"Cuesta de San Vicente"},{"hint":"vhxhgP___397AAAAgwAAAAAAAAAUAAAAzS6rQiNnq0AAAAAAv1ZiQXsAAACDAAAAAAAAABQAAADfFQAA8ozH_5T7aAI-jMf_aPtoAgAAbxVHO5za","distance":16.037908,"location":[-3.69947,40.43458],"name":"Calle del Castillo"},{"hint":"sMQIgP___39hAAAAdQAAAAwAAAAPAAAAuI6CQidPTUGTiwJBPh0fQWEAAAB1AAAADAAAAA8AAADfFQAA1FHH_7X-aALgUcf_V_9oAgEA3wVHO5za","distance":18.017435,"location":[-3.714604,40.435381],"name":"Calle de Fernández de los Ríos"},{"hint":"fvdggP___38DAAAACQAAABsBAAAQAQAA10Z_QKsmxkAfWJ1D59CXQwMAAAAJAAAAGwEAABABAADfFQAATjfH_6DWaAIyOMf_N9doAgoA7xNHO5za","distance":25.603221,"location":[-3.721394,40.42512],"name":"Calle de la Rosaleda"},{"hint":"UK5ggP___3-vAAAA2QAAAAAAAAATAAAAXkLzQoZV6EEAAAAAOHROQa8AAADZAAAAAAAAABMAAADfFQAA69bH_2sFaQKw18f_YQVpAgAAPwBHO5za","distance":16.755112,"location":[-3.680533,40.437099],"name":"Calle de Castelló"},{"hint":"N_tggP___38FAAAADgAAAAAAAAArAAAAs5d-QEtHq0AAAAAA7ubmQQUAAAAOAAAAAAAAACsAAADfFQAA4lfH_93BaAK9Vcf_gMFoAgAAfwpHO5za","distance":47.721276,"location":[-3.713054,40.419805],"name":"Calle de Bailén"},{"hint":"Y6tggP___38AAAAAFwAAAEMAAAAAAAAAbmnjPTpcx0HssFBCAAAAAAAAAAAXAAAAQwAAAAAAAADfFQAAUs3H_yAMaQJQzcf_IAxpAgMAPwBHO5za","distance":0.169729,"location":[-3.68299,40.438816],"name":"Calle de Velázquez"}],"destinations":[{"hint":"NvZggP___3_TAAAAAQEAAAAAAAAUAAAA3tC8QjVToUEAAAAAqmYQQdMAAAABAQAAAAAAABQAAADfFQAAN27H_3nMaAJHbsf_lMxoAgAAbxJHO5za","distance":3.291252,"location":[-3.707337,40.422521],"name":"Calle de la Estrella"},{"hint":"7PxggP___38BAAAAJwAAAEQAAAAAAAAAxRrbPxuQJUJxgFZCAAAAAAEAAAAnAAAARAAAAAAAAADfFQAAhVPH_4zraAKIU8f_oetoAgIAXxFHO5za","distance":2.345717,"location":[-3.714171,40.430476],"name":"Calle del Marqués de Urquijo"},{"hint":"7R5hgP___38sAAAAswAAAAAAAAAAAAAAhJz4QZhzukIAAAAAAAAAACwAAACzAAAAAAAAAAAAAADfFQAAdp3H_33MaAJ5ncf_xMxoAgAAvwVHO5za","distance":7.888016,"location":[-3.695242,40.422525],"name":"Calle del Almirante"},{"hint":"1cgIgP___3-MAAAA6AAAAAAAAAASAAAAWWTDQpbse0IAAAAAUtBDQYwAAADoAAAAAAAAABIAAADfFQAA6J_H_w0HaQKOn8f_EQdpAgAAPwBHO5za","distance":7.650695,"location":[-3.694616,40.437517],"name":"Calle de Fernández de la Hoz"},{"hint":"Hv1ggCT9YIB1AAAAKQAAAAkAAAAAAAAAykKDQtuMs0E_-KhAAAAAADoAAAAVAAAABQAAAAAAAADfFQAA1lrH_1T8aALZWsf_e_xoAgEAHxFHO5za","distance":4.338074,"location":[-3.712298,40.434772],"name":"Calle de Abdón Terradas"},{"hint":"qvdggP___38TAAAAPgAAAAMAAAAAAAAA_wWvQdHkPEICOj1AAAAAABMAAAA-AAAAAwAAAAAAAADfFQAAiDTH_zLMaALyNMf_4MtoAgEA3wJHO5za","distance":12.799559,"location":[-3.722104,40.42245],"name":"Calle del Maestro Sorozábal"},{"hint":"QvZggP___39IAAAAZAAAAAAAAAAGAAAAqPmfQqyR9kEAAAAA4XHiQEgAAABkAAAAAAAAAAYAAADfFQAAhGPH_-i-aAJ2ZMf_Xr5oAgAAjw1HO5za","distance":25.624006,"location":[-3.710076,40.419048],"name":"Cuesta de Santo Domingo"},{"hint":"7h5hgP___3-DAAAAuwAAAAAAAAAAAAAA8kNqQkM5xUEAAAAAAAAAAIMAAAC7AAAAAAAAAAAAAADfFQAAMJvH_wvRaAIkm8f_cdBoAgAA3wVHO5za","distance":17.130601,"location":[-3.695824,40.423691],"name":"Calle de San Lucas"}]}}

# print(min(min(durations)))
# print(durations.index(min(durations)))
# print(durations.index(min(min(durations))))

durations = response["data"]["durations"]
durations_matrix = np.asmatrix(durations)
const_durations_matrix = np.asmatrix(durations)

print(const_durations_matrix)

for row in durations_matrix:
    # Find minimum duration time
    m = find_minimum(const_durations_matrix, durations_matrix.min(axis=0).min(axis=1))
    print(m)
    # Find driver and passenger
    d = find_driver(durations_matrix)
    print(d)
    p = find_passenger(durations_matrix)
    print(p)
    # Allocate driver and passenger and populate json file
    allocations.append({
        "driver": drivers[m[0,0]],
        "passenger": passengers[m[0,1]],
        "duration": durations_matrix[d,p]
    })
    # Delete driver and passenger from matrix
    durations_matrix = np.delete(durations_matrix, d, 0)
    durations_matrix = np.delete(durations_matrix, p, 1)
    print(const_durations_matrix)
    print(durations_matrix)

dict_allocations = {
    "timestamp": response["timestamp"],
    "data": allocations
}

with open(os.path.join("..","database","allocations.json"), "w") as outfile:
    json.dump(dict_allocations, outfile)

# Populate matrix json file: Timestamp, sources, destinations, durations, distances
# {
#   timestamp: 1605007438,
#   data: {
#       sources: [],
#       destinations: [],
#       durations: [],
#       distances: []
#   }
# }

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