"""Install the following requirements:
    google-api-core   1.4.1
"""
import os
import google.cloud.dialogflow_v2 as dialogflow
from google.api_core.exceptions import InvalidArgument
from datetime import datetime

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private-key.json' # To update

DIALOGFLOW_PROJECT_ID = '[PROJECT_ID]' # To update
DIALOGFLOW_LANGUAGE_CODE = 'English — en'
SESSION_ID = f'{os.environ.get("USERNAME")}#{os.uname()[1]}@{datetime.now()}'

text_to_be_analyzed = "come here fast"

session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
query_input = dialogflow.types.QueryInput(text=text_input)
try:
    response = session_client.detect_intent(session=session, query_input=query_input)
except InvalidArgument:
    raise

print("Query text:", response.query_result.query_text)
print("Detected intent:", response.query_result.intent.display_name)
# print("Detected intent confidence:", response.query_result.intent_detection_confidence)
print("Fulfillment text:", response.query_result.fulfillment_text)
# print("Detected parameters:", response.query_result)
print("speed:", response.query_result.parameters["speed"])
print("direction:", response.query_result.parameters["direction"])
# for v in response.query_result.parameters:
#     print(v)
