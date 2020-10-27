# Getting Started

To get started with mymappi APIs, let's do an example.

Suppose we want to show where is our shop in a map located in our brand website. We know the 
address of our shop, but our web map only understand coordinates (latitude and longitude). 
How can we get coordinates from an address?

Simple, using mymappi Direct Geocoding API.

To do that, we are goint to follow the next steps:

1. Sign up to get our API Key.
2. Check documentation and test Direct Geocoding request.
3. Create a map.

## Sign up to get our API Key.

Firstly, we need to sign up in [mymappi Dashboard](https://dashboard.mymappi.com/signup). Complete the form 
with your email and a secure password. We will send you a confirmation email to confirm your email.

Once you have confirmed your email, log in the dashboard and go to myapi > API Token section. In this section, 
you can copy your API Key, see and change your plan and check the documentation (we will do it in the next
step).

## Check documentation and test Direct Geocoding request.

On [mymappi Documentation](https://api.mymappi.com/docs), we can check and test all the APIs. Easy, click 
in the API which you want and try it out.

In our case Direct Geocoding API, from Geocoding API section. Fill the fields with your API Key and 
the address, for example: Gran Vía, 20, Madrid; and click execute.

Check the first result in the data response array, and get the latitude and longitude.

```
{
    "licence": "https://mymappi.com/attribution",
    "osm_type": "N",
    "osm_id": 2910130620,
    "lat": 40.4199692,
    "lon": -3.7000911,
    "display_name": "Gran Vía,20,Madrid,28013,España,",
    "class": "place",
    "type": "house"
}
```

Perfect! Now we have the coordinates for our shop, let's show it in a map.

## Create a map

To create a map we are goint to use [Leaflet](https://leafletjs.com/), an open source JavaScript library 
used to build web mapping applications.

Just create the map centered in our shop coordinates.

```
var mymap = L.map('map').setView([40.4199692, -3.7000911], 15);
```

And add a marker.

```
var marker = L.marker([40.4199692, -3.7000911]).addTo(mymap);
```

This is the result.

![Getting Started Map](images/map)

All the code from map.html

```
<!DOCTYPE html>
<html>
    <head>
        
        <title>Getting Starter</title>

        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin=""/>
        <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>

        <style type="text/css">
            #map {
            height: 100%;
            }
    
            html,
            body {
            height: 100%;
            margin: 0;
            padding: 0;
            }
        </style>
    </head>
    <body>
        <div id="map"></div>
        <script>

            var mymap = L.map('map').setView([40.4199692, -3.7000911], 17);

            var marker = L.marker([40.4199692, -3.7000911]).addTo(mymap);

            marker.bindPopup("<b>Hello world!</b><br>This is my shop.").openPopup();

            L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=YOUR_API_TOKEN', {
                maxZoom: 18,
                attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
                id: 'mapbox/streets-v11',
                tileSize: 512,
                zoomOffset: -1
            }).addTo(mymap);

        </script>
    </body>
</html>
```
