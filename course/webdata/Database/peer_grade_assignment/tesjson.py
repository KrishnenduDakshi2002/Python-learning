

import json
  
# JSON string:
# Multi-line string
x = """{
    "Name": "Jennifer Smith",
    "Contact Number": 7867567898,
    "Email": "jen123@gmail.com",
    "test" : {
    "Name": "Jennifer Smith",
    "Contact Number": 7867567898,
    "Email": "jen123@gmail.com",
    "Hobbies":["Reading", "Sketching", "Horse Riding"]
    },
    "Hobbies":["Reading", "Sketching", "Horse Riding"]
    }"""

z="""
{
   "results" : [
      {
         "address_components" : [
            {
               "long_name" : "1460",
               "short_name" : "1460",
               "types" : [ "street_number" ]
            },
            {
               "long_name" : "Broadway",
               "short_name" : "Broadway",
               "types" : [ "route" ]
            },
            {
               "long_name" : "Manhattan",
               "short_name" : "Manhattan",
               "types" : [ "political", "sublocality", "sublocality_level_1" ]
            },
            {
               "long_name" : "New York",
               "short_name" : "New York",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "New York County",
               "short_name" : "New York County",
               "types" : [ "administrative_area_level_2", "political" ]
            },
            {
               "long_name" : "New York",
               "short_name" : "NY",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "United States",
               "short_name" : "US",
               "types" : [ "country", "political" ]
            },
            {
               "long_name" : "10036",
               "short_name" : "10036",
               "types" : [ "postal_code" ]
            }
         ],
         "formatted_address" : "1460 Broadway, New York, NY 10036, USA",
         "geometry" : {
            "location" : {
               "lat" : 40.7551279,
               "lng" : -73.98617489999999
            },
            "location_type" : "ROOFTOP",
            "viewport" : {
               "northeast" : {
                  "lat" : 40.75647688029149,
                  "lng" : -73.98482591970848
               },
               "southwest" : {
                  "lat" : 40.75377891970849,
                  "lng" : -73.9875238802915
               }
            }
         },
         "place_id" : "ChIJjeMlSGNZwokRgBVdLDDLPHE",
         "types" : [ "establishment", "point_of_interest" ]
      }
   ],
   "status" : "OK"
}"""

# parse x:
y = json.loads(z)
  
# the result is a Python dictionary:
print(y)