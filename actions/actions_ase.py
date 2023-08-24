from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class ActionID(Action):
    def name(self):
        return "action_id"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        response = (
            "Sure! To apply for an ID card, you can visit the [Support Portal](https://support.accenture.com)."
        )

        dispatcher.utter_message(response)
        return [SlotSet("asked_how_to_apply_id_card", True)]

class ActionBookingRoom(Action):
    def name(self):
        return "action_booking_room"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        response = (
            "Sure! You can make room reservations using the [Reservation Portal](https://reservations.accenture.com/reserve-space/Default.aspx) link."
        )

        dispatcher.utter_message(response)
        return [SlotSet("asked_how_to_book_room", True)]

class ActionRelocateLocation(Action):
    def name(self):
        return "action_relocate_location"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        response = "To relocate your work location, please click on the following link: [Relocation Link](https://ast.accenture.com/atlas/Home/wfrmHomePage.aspx). "
        dispatcher.utter_message(response)
        return []

class ActionBookSeat(Action):
    def name(self):
        return "action_book_seat"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        message = "To book a seat, please click on the following link: [Seat Booking Link](https://acpindia-mobile.accenture.com/home)."
        dispatcher.utter_message(text=message)
        return []

