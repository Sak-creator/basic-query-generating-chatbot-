#from typing import Any, Text, Dict, List
#from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher

#class GenerateSQLQueryAction(Action):
  
 #   def name(self) -> Text:
  #      return "generate_sql_query_action"

   # def run(self, dispatcher: CollectingDispatcher,
    #        tracker: Tracker,
     #       domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #print("tracker.latest_message")
        #t=next(tracker.get_latest_entity_values("table"), None)
        #print(t)
      #  dispatcher.utter_message(Text='done')
       # entity_value = tracker.get_slot("table")
        #print('entity')
        #dispatcher.utter_message(entity_value)
        #intent = tracker.latest_message.get("intent").get("name")
        #dispatcher.utter_message(intent)
        #table = tracker.get_slot("table")
        #print(tracker.latest_message)
        #if intent == "provide_table":
         #    sql_query = f"SELECT * FROM {table}"
          #   dispatcher.utter_message(template="utter_display_results", query=sql_query)
        #else:
         #    sql_query = "default"

       # return []



      #  class GenerateWHEREQueryAction(Action):
  
    #def name(self) -> Text:
       # return "generate_where_query_action"

    #def run(self, dispatcher: CollectingDispatcher,
           # tracker: Tracker,
            #domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #print("tracker.latest_message")
        #t=next(tracker.get_latest_entity_values("table"), None)
        #print(t)
       # dispatcher.utter_message(Text='done')
        #entity_value = tracker.get_slot("table")
        #print('entity')
        #dispatcher.utter_message(entity_value)
        #intent = tracker.latest_message.get("intent").get("name")
        #dispatcher.utter_message(intent)
        #table = tracker.get_slot("table")
        #operator = tracker.get_slot("operator")
        #value = tracker.get_slot("value")
        #column = tracker.get_slot("column")
        #print(tracker.latest_message)
        #if intent == "provide_table_where":
            # where_query = f"SELECT * FROM {table} WHERE {column} {operator} {value}  ;"
             #dispatcher.utter_message(template="utter_display_where", where=where_query)
        #else:
         #    sql_query = "default"

#        return []




from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class GenerateSQLQueryAction(Action):
    def name(self) -> Text:
        return "generate_sql_query_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entity_value = tracker.get_slot("tablenamenew")
        intent = tracker.latest_message.get("intent").get("name")
        tablenamenew = tracker.get_slot("tablenamenew")

        if intent == "provide_table_new":
            sql_query = f"SELECT * FROM {tablenamenew}"
            dispatcher.utter_message(template="utter_display_results", query=sql_query)
        else:
            sql_query = "default"

        return []

class GenerateWHEREQueryAction(Action):
    def name(self) -> Text:
        return "generate_where_query_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message.get("intent").get("name")
        tablenamenew = tracker.get_slot("tablenamenew")
        operator = tracker.get_slot("operator")
        value = tracker.get_slot("value")
        column = tracker.get_slot("column")
        title = tracker.get_slot("title")
        if intent == "provide_table_where":
            where_query = f"SELECT * FROM {tablenamenew} WHERE {column} {operator} {value};"
            dispatcher.utter_message(template="utter_display_where", where=where_query)
        elif intent == "provide_table_name":
            word_query = f"SELECT * FROM {tablenamenew} WHERE {column} {operator} {title};"
            dispatcher.utter_message(template="utter_display_word", word=word_query)
        else:
            print("default")

        return []

class CollectInformationAction(Action):
    def name(self) -> Text:
        return "action_collect_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Retrieve the slot values
        print("name")
        namee = tracker.get_slot("namee")
        location = tracker.get_slot("location")
        experience = tracker.get_slot("experience")
        table = tracker.get_slot("table")

        # Check if all slots have been filled
        if namee and location and experience and table:
            response = f"INSERT INTO {table} (name, experience, location) VALUES ('{namee}', '{experience}', '{location}');"
            dispatcher.utter_message(text="your query is generated")
        elif not table:
            response = "Please provide the name of the table you want to create a record in:"
        elif not namee:
            response = "Please provide your name:"
        elif not experience:
            response = "Please provide experience:"
        elif not location:
            response = "Please provide your location:"
        else:
            response = "Something went wrong. Please try again."

        dispatcher.utter_message(text=response)

        return []

class GenerateUpdateQueryAction(Action):
    def name(self) -> Text:
        return "generate_update_query_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entity_value = tracker.get_slot("rowname")
        intent = tracker.latest_message.get("intent").get("name")
        rowname = tracker.get_slot("rowname")
        quantity = tracker.get_slot("quantity")
        update = tracker.get_slot("update")
        skill = tracker.get_slot("skill")
        new_name = tracker.get_slot("new_name")
        number = tracker.get_slot("number")
        customer_id = tracker.get_slot("customer_id")
        if intent == "provide_rowname":
            update_query = f"{update} {rowname} SET Name = '{new_name}', {skill} {quantity} {number} WHERE CustomerID = {customer_id};"
            dispatcher.utter_message(template="utter_display_update", querynew=update_query)
        else:
            sql_query = "default"

        return []



