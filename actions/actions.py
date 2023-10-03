# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import List, Text, Dict, Any
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Tracker
from actions.football import *
from actions.coach import *


class ActionwinLossRecord(Action):

    def name(self) -> Text:
        return "action_winLossRecord"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("team")
        text = winLossRecord(name)

        dispatcher.utter_message(text)

        return []

class ActioncoachRecord(Action):

    def name(self) -> Text:
        return "action_coachRecord"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("team")
        text = getCoachRecord(name)

        dispatcher.utter_message(text)

        return []

