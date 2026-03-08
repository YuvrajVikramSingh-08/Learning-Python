from dotenv import load_dotenv
import os
import requests
import datetime as dt

load_dotenv()

calorie_api = "https://api.api-ninjas.com/v1/caloriesburned"
headers = {
    "X-Api-Key": os.getenv("API_NINJA_KEY"),
}
params = {
    "activity": "",
    "duration": "",
}

post_sheety = "https://api.sheety.co/b0c798dac0fad5f0c8af9f040762901c/myWorkouts/workouts"

more = True

while more:

    date = dt.date.today()
    time = dt.datetime.now().time().strftime("%H:%M:%S")

    activity = input("Enter activity: ")
    duration = input("Enter duration(in minutes): ")

    params["activity"] = activity
    params["duration"] = int(duration)

    response = requests.get(url=calorie_api, headers=headers, params=params)
    # print(response.json()[0])

    exercise = {
        "workout": {
            "date": date.strftime("%Y-%m-%d"),
            "time": time,
            "exercise": activity,
            "duration": duration,
            "calories": response.json()[0]["total_calories"]
        }
    }
    head_sheet = {
        "Authorization": os.getenv("BEARER"),
    }

    sheet_response = requests.post(url=post_sheety, json=exercise, headers=head_sheet)
    print(sheet_response.json())

    cont = input("Continue? (y/n): ")
    if cont == "n":
        more = False