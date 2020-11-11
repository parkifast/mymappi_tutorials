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
print(generate_url())
r = requests.get(generate_url())
print(r.status_code)
print(r.json())
response = r.json()
# response = {"status":"OK","version":"1.0","provider":"mymappi API 1.0","timestamp":1605007438,"copyright":"The data included in this document is from www.mymappi.com. The data is strictly forbidden to be cached, read our terms and conditions in https:\/\/mymappi.com\/myapi\/legal.","next":"","data":{"code":"Ok","durations":[[542.3,451.8,236.9,410.3,472.8,126.5,154.3,187.1],[725.5,407.3,395.1,309.8,368.5,226.1,210.3,181.1],[590.6,404,260.2,362.5,425,56.9,93.4,117.5],[374,275.4,24.9,299.9,362.4,227.7,159.8,233.8],[684.3,366.1,353.9,268.6,327.3,184.8,169.1,139.8],[702.3,318.6,428.7,166.1,252.1,424.3,365.6,380.7],[499.5,384,169.1,342.5,405,167.3,99.4,183],[673.8,354.8,343.4,216.5,322.2,255,174.6,190.8]],"sources":[{"hint":"sPZggP___38TAAAAFAAAAAAAAAAdAAAAJQ6yQbNA2T4AAAAAS-4AQhMAAAAUAAAAAAAAAB0AAADfFQAAeGDH_1gMaQKBYMf_twtpAgAAfwVHO5za","distance":17.893899,"location":[-3.710856,40.438872],"name":"Calle de Cea Bermúdez"},{"hint":"vatggMCrYIAVAAAAGAAAAKUAAADgAAAAtwWRQNDxnkBbwghCFUY7QgoAAAANAAAAUgAAAHAAAADfFQAAodHH_38MaQKX0cf_RAxpAgYAXxFHO5za","distance":6.606152,"location":[-3.681887,40.438911],"name":""},{"hint":"A8kIgP___389AAAAQwAAAAAAAAAAAAAA666JQkmuv0AAAAAAAAAAAD0AAABDAAAAAAAAAAAAAADfFQAAsYvH_3AGaQJiisf_GgZpAgAAXxVHO5za","distance":29.990549,"location":[-3.699791,40.43736],"name":"Calle de Santa Engracia"},{"hint":"SPpggFL6YIBsAAAALgAAAAAAAAAAAAAAkcCWQlzn_EEAAAAAAAAAAGwAAAAuAAAAAAAAAAAAAADfFQAAHXPH_33eaAIDc8f_7N1oAgAAXxFHO5za","distance":16.25142,"location":[-3.706083,40.427133],"name":"Calle de Daoíz"},{"hint":"k7kIgP___38KAAAAFQAAAAAAAAA_AAAA2uc0QcolPUEAAAAA4PGMQgoAAAAVAAAAAAAAAD8AAADfFQAAd8zH_94HaQJ6zMf_AghpAgAAHxFHO5za","distance":4.005573,"location":[-3.683209,40.437726],"name":"Calle de María de Molina"},{"hint":"57gIgP___38lAAAASwAAAD8AAADWAAAAgvclQpsQJkIfiotCYMVtQyUAAABLAAAAPwAAANYAAADfFQAArMzH_4zGaAKPz8f_37xoAgEA3wRHO5za","distance":282.107717,"location":[-3.683156,40.421004],"name":"Calle de O\u0027Donnell"},{"hint":"b_tggP___38ZAAAAQwAAAAAAAAAAAAAAE1LjQQ8dOUIAAAAAAAAAABkAAABDAAAAAAAAAAAAAADfFQAAE4DH__YAaQIegMf_awFpAgAALxFHO5za","distance":13.025285,"location":[-3.702765,40.435958],"name":"Calle de Viriato"},{"hint":"M7oIgP___39HAAAAjAAAAAgAAAAAAAAAZ3CeQrTdmEJ5CwlBAAAAAEcAAACMAAAACAAAAAAAAADfFQAA4dHH_xIEaQJN0Mf_JQRpAgEAfwtHO5za","distance":34.350049,"location":[-3.681823,40.436754],"name":"Calle de Núñez de Balboa"}],"destinations":[{"hint":"WjxXgP___38DAAAAMgAAAAAAAAAAAAAA2HwbQOgjAEIAAAAAAAAAAAMAAAAyAAAAAAAAAAAAAADfFQAAb2HH_9S5aAJPX8f_17toAgAAfw5HO5za","distance":73.495351,"location":[-3.710609,40.417748],"name":"Calle de Vergara"},{"hint":"zisBgP___3_IAAAAOwEAAAAAAAASAQAA-K-yQppsTEIAAAAA8YbzQsgAAAA7AQAAAAAAABIBAADfFQAAgYjH_2a8aAIziMf_4b1oAgAAXxBHO5za","distance":42.601915,"location":[-3.700607,40.418406],"name":"Calle de la Aduana"},{"hint":"R_pggP___3-NAAAAzQAAAAAAAAAAAAAAeS57QoGk4UEAAAAAAAAAAI0AAADNAAAAAAAAAAAAAADfFQAA_XbH_1DgaAJBd8f_SOBoAgAAjwBHO5za","distance":5.838748,"location":[-3.705091,40.4276],"name":"Calle de Monteleón"},{"hint":"daZggP___38nAAAAXgAAABcAAAALAAAAtKDcQZQiFULpsIBB44T6QCcAAABeAAAAFwAAAAsAAADfFQAAv7zH_4bFaAInvMf_ksVoAgIAXwBHO5za","distance":12.968021,"location":[-3.687233,40.420742],"name":"Calle de Claudio Coello"},{"hint":"cRxhgP___39GAAAAUAAAAAAAAAAAAAAATwGdQls5KUEAAAAAAAAAAEYAAABQAAAAAAAAAAAAAADfFQAAt7bH_5G7aAL7t8f_f7toAgAATwBHO5za","distance":27.568599,"location":[-3.688777,40.418193],"name":"Calle de Alfonso XII"},{"hint":"9MgIgP___38QAAAAjQAAAAwAAAAJAAAA-meOQcQOCkNujFVBX2geQRAAAACNAAAADAAAAAkAAADfFQAAaZnH__AIaQJsmsf_5AhpAgEAfwtHO5za","distance":22.020219,"location":[-3.696279,40.438],"name":"Calle de Modesto Lafuente"},{"hint":"pRxhgKkcYYAyAAAAJwAAAAAAAAAfAAAAtpdhQsuJKUIAAAAA7aILQjIAAAAnAAAAAAAAAB8AAADfFQAA5JXH_zj9aALilcf_Wf1oAgAAvxBHO5za","distance":3.66828,"location":[-3.69718,40.435],"name":"Paseo del General Martínez Campos"},{"hint":"pBxhgP___38qAAAAegAAAAAAAAAHAAAAlMg7Qs4ZskIAAAAAaY78QCoAAAB6AAAAAAAAAAcAAADfFQAAdZ3H_6oDaQKBncf_FwVpAgAA_xBHO5za","distance":40.542734,"location":[-3.695243,40.43665],"name":"Calle de García de Paredes"}]}}
durations = response["data"]["durations"]
print(min(min(durations)))
print(durations.index(min(durations)))
print(durations.index(min(min(durations))))
# Allocate drivers and passengers

# Populate allocations txt: Timestamp, driver_id, driver_latitude, driver_longitude, passenger_id, passenger_latitude, passenger_longitude, duration

# Populate matrix txt: Timestamp, sources, destinations, data
# {
#   timestamp: 1605007438,
#   sources: [
#       [40.43871056191201,-3.7108465168370945],
#       [40.438851825209454,-3.6818973265756565],
#       [40.43727428465753,-3.700126460783412],
#       [40.42698788151344,-3.7061092312349646],
#       [40.418527110759335,-3.6824172388098635],
#       [40.437761962690395,-3.683206076649443],
#       [40.436074690982885,-3.7027540001252537,
#       [40.43677273078681,-3.6822265498141418],
#   ],
#   destinations: [
#       [40.41826332937495,-3.711152885700495],
#       [40.41878541533847,-3.7006849874443493],
#       [40.4275920055038,-3.7050225902626486],
#       [40.42075366840505,-3.6873847037798066],
#       [40.4181750475997,-3.688452843710744],
#       [40.437988176503424,-3.6960201188475494],
#       [40.43503311090895,-3.69718215521498],
#       [40.43701483928551,-3.69523147561721],
#   ],
#   data: [
#       [542.3,451.8,236.9,410.3,472.8,126.5,154.3,187.1],
#       [725.5,407.3,395.1,309.8,368.5,226.1,210.3,181.1],
#       [590.6,404,260.2,362.5,425,56.9,93.4,117.5],
#       [374,275.4,24.9,299.9,362.4,227.7,159.8,233.8],
#       [684.3,366.1,353.9,268.6,327.3,184.8,169.1,139.8],
#       [702.3,318.6,428.7,166.1,252.1,424.3,365.6,380.7],
#       [499.5,384,169.1,342.5,405,167.3,99.4,183],
#       [673.8,354.8,343.4,216.5,322.2,255,174.6,190.8]]
# } 

