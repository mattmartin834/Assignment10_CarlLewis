#Name: Carl Lewis (Luke Brooks, Tatianna Stryjewski, and Matthew Martin)
#email: stryjete@mail.uc.edu
#Assignment Title: Assignment 06
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: Using JSON and API
#Citations: https://fdc.nal.usda.gov/api-guide.html
#Anything else that's relevant: The API is the different types of cheese
# registered with the FDA
#main.py

import requests 
import json
from FDAPackage.FDA import *

response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?api_key=TlerFrZJS7oeM0DePkwbeLJoSvUXpaxfw62lXxNL&query=Cheddar%20Cheese')

json_string = response.content

parsed_json = json.loads(json_string) #putting results into a dictionary

#iterate_dictionary(parsed_json) #invoking the function and passing it parsed_json

#print(parsed_json)

unique_ingredients = set(food['description'] for food in parsed_json['foods'])
print("The different types of cheese descriptions under the FDAs website are as follows:" , unique_ingredients) 
# cheese is displayed at the front, followed by different types
