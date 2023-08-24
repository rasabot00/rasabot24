# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import webbrowser

class ActionOpenWebsite(Action):

   
    def name(self) -> Text:
        return "action_open_website"

    async def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        website = tracker.latest_message.get("text")

        if "google" in website.lower():
            url = "https://www.google.com"
            dispatcher.utter_message("Opening Google")
        elif "myntra" in website.lower():
            url = "https://www.myntra.com"
            dispatcher.utter_message("Opening Myntra")
        elif "nyka" in website.lower():
            url = "https://www.nykaa.com"
            dispatcher.utter_message("Opening Nykaa")
        else:
            url = "https://www.amazon.com"
            dispatcher.utter_message("Opening Amazon")

        webbrowser.open(url)
        return []
    
    
import requests
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGetWeather(Action):
    def name(self) -> Text:
        return "action_get_weather"
    
    def kelvin_to_celsius(self, kelvin_temp: float) -> float:
        celsius_temp = kelvin_temp - 273.15
        return celsius_temp

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message.get("entities")
        print("Extracted entities:", entities)

        city = tracker.get_slot('city')
        print("Extracted City:", city)  # Add this line for debugging
        
        api_key = "4d5df4d5dbd81c9da080c40a865e313d"
        complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        response = requests.get(complete_url)
        weather_data = response.json()

        conditions = ""
        temperature = None

        if "weather" in weather_data and weather_data["weather"]:
            conditions = weather_data["weather"][0].get("description", "")

        if "main" in weather_data and "temp" in weather_data["main"]:
            temperature_kelvin = weather_data["main"]["temp"]
            temperature_celsius = self.kelvin_to_celsius(temperature_kelvin)
            temperature = f"{int(temperature_celsius)}°C"  # Convert to integer and format as °C

        if temperature and conditions:
            message = f"The weather in {city} is {conditions} with a temperature of {temperature}."
        elif conditions:
            message = f"The weather in {city} is {conditions}."
        else:
            message = f"Sorry, I couldn't fetch the weather information for {city}."

        dispatcher.utter_message(text=message)
        return []
    