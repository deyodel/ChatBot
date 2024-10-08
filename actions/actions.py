# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ExtractProductEntity(Action):

    def name(self) -> Text:
        return "action_extract_product_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product_entity = next(tracker.get_latest_entity_values('product'), None)

        if product_entity:
            dispatcher.utter_message(text = f"Thank you for confirming your choice of {product_entity}. "
                     "If you have any additional questions or need further assistance, please don't hesitate to ask.")
        else:
            dispatcher.utter_message(text = "I apologize, but it seems I couldn't identify the service you are interested in. "
                     "Could you kindly specify your choice, and I'll be happy to assist you further?")

        return []

class OrderProductAction(Action):
    def name(self) -> Text:
        return "action_order_product"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text = "Thank you for your interest in our services. We currently offer a variety of solutions, including Email Marketing, "
            "SEO Optimization, Product Management, and CRM Software. Could you please let us know which service you're "
            "interested in?")

        return []

class ConfirmOrderAction(Action):
    def name(self) -> Text:
        return "action_confirm_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product_entity = next(tracker.get_latest_entity_values('product'), None)

        if product_entity:
            dispatcher.utter_message(text=f"Thank you for confirming your choice of {product_entity}. "
                     "If you have any additional questions or need further assistance, please don't hesitate to ask.")
        else:
            dispatcher.utter_message(text="I apologize, but it seems I couldn't identify the service you are interested in. "
                     "Could you kindly specify your choice, and I'll be happy to assist you further?")
        return []

class PricingPlanAction(Action):
    def name(self) -> Text:
        return "action_pricing_plan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text = "We have a range of pricing plans tailored to your needs: Basic, Pro, and Enterprise. "
            "Could you please let us know which plan you're interested in, or if you'd like more details to help with your decision?")

        return []

class ProvidePricingInfoAction(Action):
    def name(self) -> Text:
        return "action_provide_pricing_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        pricing_tier = next(tracker.get_latest_entity_values("pricing_tier"), None)

        if pricing_tier:
            if pricing_tier.lower() == "basic":
                response = (
                    "The **Basic** plan is perfect for those beginning their journey. "
                    "It includes fundamental features designed to give your business a solid start. "
                    "Would you like to schedule a demo to explore how it can assist your growth?"
                )
            elif pricing_tier.lower() == "pro":
                response = (
                    "The **Pro** plan is ideal for businesses looking to scale. "
                    "It offers advanced tools for growing your business efficiently and strategically. "
                    "How about scheduling a personalized demo to see how Elevate can boost your progress?"
                )
            elif pricing_tier.lower() == "Enterprise":
                response = (
                    "The **Prestige** plan is designed for established businesses. "
                    "It provides premium features and insights to refine your operations. "
                    "Would you like to schedule a demo and discover how Prestige can enhance your business?"
                )
            else:
                response = (
                    f"The {pricing_tier} plan is available, offering a robust set of features to meet your needs. "
                    "Would you like to schedule a demo to explore its benefits?"
                )
            dispatcher.utter_message(text=response)
        else:
            dispatcher.utter_message(
                text="We offer several thoughtfully crafted pricing tiers, each tailored to distinct business needs. "
                     "Could you please specify which plan you'd like to explore further, and I’ll provide more information?"
            )
        return []


class OfferDemoAction(Action):
    def name(self) -> Text:
        return "action_offer_demo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_response = tracker.latest_message['text'].lower()

        if tracker.latest_message['intent'].get('name') == 'affirmative_demo':
            # Proceed with lead capture logic
            dispatcher.utter_message(
                text="I'm pleased to inform you that your demo has been successfully arranged! Please check your email for all the necessary details.")
        elif tracker.latest_message['intent'].get('name') == 'negative_demo':
            # Alternative action if the user doesn't want the demo
            dispatcher.utter_message(
                text="No problem! If you have any other questions or need assistance, feel free to ask.")

        return []