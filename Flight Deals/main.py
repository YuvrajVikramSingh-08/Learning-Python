#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager

datamanager = DataManager()
sheet_data = datamanager.data
flight_search = FlightSearch()

for i in sheet_data:
    i["iataCode"] = "TESTING"

datamanager.post(sheet_data)
print(sheet_data)