import requests
from datetime import datetime

APP_KEY= "YOURKEY"
APP_ID= "YOURID"
NUTRIX_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT="https://api.sheety.co/bd25026a50c3be1b214ec5fca5c3edd7/workoutTracking/workouts"

yourinput=input("What kind of excersise did you do today?")
headers={
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

bearer_headers={
    "Authorization": "Bearer HEADERS"
}

nutrix_parameters={
    "query": yourinput,
    "gender": "female",
    "weight_kg":  70,
    "height_cm":  170,
    "age": 25
}
response=requests.post(NUTRIX_ENDPOINT, json=nutrix_parameters, headers=headers)
result=response.json()



####### Posting the data + log time in GoogleSheets

today_date=datetime.now().strftime("%d/%m/%Y")
now_time= datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs={
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response=requests.post(SHEETY_ENDPOINT, json=sheet_inputs, headers=bearer_headers)

print(sheet_response.text)