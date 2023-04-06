#main.py

import requests
import json
from functionsPackage.functions import *

response = requests.get('https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Fapi.nal.usda.gov%2Ffdc%2Fv1%2Ffoods%2Fsearch%3Fapi_key%3DTlerFrZJS7oeM0DePkwbeLJoSvUXpaxfw62lXxNL%26query%3DCheddar%2520Cheese&data=05%7C01%7Cmarti6mr%40mail.uc.edu%7Ceb844876b7e94aa91a8e08db35eb3367%7Cf5222e6c5fc648eb8f0373db18203b63%7C0%7C0%7C638163056509174398%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=SPkcaQD1cumenyAJdbcgQP0lGKXePI9Gfvw8NtuCeTs%3D&reserved=0')

json_string = response.content

parsed_json = json.loads(json_string)

nutrientData = iterate_dictionary(parsed_json)
print(nutrientData)

unique_ingredients = set(food['description']for food in parsed_json['foods'])
#print(unique_ingredients)
