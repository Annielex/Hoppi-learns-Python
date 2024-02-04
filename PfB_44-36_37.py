# Calling an API

# API:
# Applicable Programming Interfaces - Programmierschnittstellen

# Webservice:
# developer shares functionality of a function, but not the code via placing the function on a web server
# programmer with address of that function on the web server and the required permissions can call the function

# documentation needed to be able to call required function

# You can't call a function unless you know the function name and required parameters
# When you create a webservice you create an Application Programming Interface (API)
#The API defines the function names and parameters so others know how to call your function

# Computer Vision API - v2.0
# Example for function "Analyze Image" (POST)
#analyze(visualfeatures, details, language)

#visualfeatures is a string... and other parameters from documentation

# This code will show you how to call the Computer Vision API from Python
# You can find documentation on the Computer Vision Analyze Image method here
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa

# Use the requests library to simplify making a REST API call from Python 
import requests

# We will need the json library to read the data passed back 
# by the web service
import json

# You need to update the SUBSCRIPTION_KEY to 
# they key for your Computer Vision Service
SUBSCRIPTION_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"

# You need to update the vision_service_address to the address of
# your Computer Vision Service
vision_service_address = "https://canadacentral.api.cognitive.microsoft.com/vision/v2.0/"

# Add the name of the function you want to call to the address
address = vision_service_address + "analyze"

# According to the documentation for the analyze image function 
# There are three optional parameters: language, details & visualFeatures
parameters  = {'visualFeatures':'Description,Color',
               'language':'en'}

# Open the image file to get a file object containing the image to analyze
image_path = "./TestImages/PolarBear.jpg"
image_data = open(image_path, "rb").read()

# According to the documentation for the analyze image function
# we need to specify the subscription key and the content type
# in the HTTP header. Content-Type is application/octet-stream when you pass in a image directly
headers    = {'Content-Type': 'application/octet-stream',
              'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

# According to the documentation for the analyze image function
# we use HTTP POST to call this function
response = requests.post(address, headers=headers, params=parameters, data=image_data)

# Raise an exception if the call returns an error code
response.raise_for_status()

# Display the JSON results returned
results = response.json()
print(json.dumps(results))
