from unittest import TestCase
from unittest.mock import Mock

from webhook.exceptions import ValidationError
from webhook.deserializer import Deserializer

import json

class TestDeserializer(TestCase):
    def setUp(self):
        self.deserializer = Deserializer()

    def test_空の文字列のときは例外(self):
        self.assertRaises(ValidationError, lambda: self.deserializer.deserialize(''))

    def test_Jsonとしてパースできないときは例外(self):
        self.assertRaises(ValidationError, lambda: self.deserializer.deserialize('{{{'))

    def test_Jsonのスキーマが正しくないときは例外(self):
        self.assertRaises(ValidationError, lambda: self.deserializer.deserialize('{}'))

    def test_正しい形式のJsonのときはSerializeした結果を返す(self):
        body = \
            u'{'\
            u'  "webhook_setting_id": "12345",'\
            u'  "webhook_event_type": "mention_to_me",'\
            u'  "webhook_event_time": 1498028130,'\
            u'  "webhook_event":{'\
            u'      "account_id": 123456,'\
            u'      "from_account_id": 123456,'\
            u'      "to_account_id": 1484814,'\
            u'      "room_id": 567890123,'\
            u'      "message_id": "789012345",'\
            u'      "body": "[To:1484814]おかずはなんですか？",'\
            u'      "send_time": 1498028125,'\
            u'      "update_time": 0'\
            u'  }'\
            u'}'

        expect = json.loads(body)

        result = self.deserializer.deserialize(body)

        self.assertEqual(result, expect)