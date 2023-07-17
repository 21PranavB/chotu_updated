# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class LinkFind(Action):

    def name(self) -> Text:
        return "link_find"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        var2 = tracker.get_slot("user_text")
        str2 = "I want "
        product = var2.replace(str2, "")
        str1 = "https://www.mystore.in/en/search/" + product
        Search = str1.replace(" ", "%20")
        dispatcher.utter_message(response="utter_search", search=Search)
        # dispatcher.utter_template("utter_dbz",tracker,link=tink)
        return []


class FindRet(Action):

    def name(self) -> Text:
        return "find_ret"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        var2 = tracker.get_slot("ret_name")
        str2 = "Tell me about "
        product = var2.replace(str2, "")
        str1 = "https://www.mystore.in/en/search/" + product
        Search = str1.replace(" ", "%20")
        dispatcher.utter_message(response="utter_search", search=Search)
        return []



