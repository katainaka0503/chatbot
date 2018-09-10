import os
import urllib

import requests


class ChatworkSendCommentService:

    def __init__(self):
        self.__chatwork_token = os.environ.get('CHATWORK_TOKEN')
        self.__room_id = os.environ.get('CHATWORK_ROOM_ID')

    def execute(self, message):
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'x-chatworktoken': self.__chatwork_token
        }
        payload = {"body": message}

        r = requests.post(
            f"https://api.chatwork.com/v2/rooms/{self.__room_id}/messages", headers=headers, params=payload)

        r.raise_for_status()
