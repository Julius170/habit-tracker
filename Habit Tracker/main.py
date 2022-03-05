# The Habit Tracker 
from django.test import modify_settings
import requests
from datetime import datetime


# CREATING A PIXELA ACCOUNT
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "sunshine"


user_params = {
    "token":"nsixduh293484noushcisyvgt",
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)

# CREATING A PIXELA GRAPH

TOKEN = "nsixduh293484noushcisyvgt"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = "graph1"

graph_config= {
    'id': GRAPH_ID,
    "name": "Coding",
    "unit": "hours",
    "type": "int",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response2 = requests.post(url= GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response2.text)



# # POSTING A PIXLE 
POSTING_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()   #(year=2022, month=3, day=3)
print(today)


pixle_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity":input("How many hours did you code today?" ),
}

# response3 = requests.post(POSTING_ENDPOINT, json=pixle_data, headers=headers)
# print(response3.text)


# # PUTTING AND DELETING REQUESTS

MODIFYING_ENDPOINT = "{PIXELA_ENDPOINT}/{USERNAME}/graph/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

modifying_data = {
    "quantity": "7",

}

# response4 = requests.put(MODIFYING_ENDPOINT, json=modifying_data,headers=headers)
# print(response4.text)


# DELETING_ENDPOINT = "{PIXELA_ENDPOINT}/{USERNAME}/graph/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


# # response5 = requests.delete(DELETING_ENDPOINT, headers=headers)
# # print(response5.text)



# LINK_TO_TRACKER = "pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html"