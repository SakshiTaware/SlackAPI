from http import client
from urllib import response
import requests
import os
from slack_sdk import WebClient

SLACK_API_TOKEN = ""
CHANNEL_NAME = ""

def get_channels(
    client = WebClient(token=os.environ["SLACK_API_TOKEN"])
    response = client.conversations_list()
    conversations = response["channels"]
    return conversations
)

print(get_channels)
