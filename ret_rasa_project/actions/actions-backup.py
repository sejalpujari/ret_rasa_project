from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGetInformation(Action):
    def name(self) -> Text:
        return "action_get_information"
        
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        topic = tracker.get_slot('topic')
        print(f"DEBUG: Received topic: {topic}")  # Add this for debugging
        
        if topic:
            topic = topic.lower()  # Convert to lowercase to match dictionary keys
        
        # Simple lookup table for responses
        topic_responses = {
            "programming": "utter_info_programming",
            "machine learning": "utter_info_machine_learning",
            "rasa": "utter_info_rasa",
            "artificial intelligence": "utter_info_artificial_intelligence",
            "chatbots": "utter_info_chatbots"
        }
        
        if topic and topic in topic_responses:
            dispatcher.utter_message(response=topic_responses[topic])
        else:
            dispatcher.utter_message(response="utter_default")
            
        return []