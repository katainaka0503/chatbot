from unittest import TestCase
from unittest.mock import Mock
from webhook.webhook_handler import WebhookHandler
from webhook.router import Router
from webhook.helpers.signature_validator import SignatureValidator
from webhook.deserializer import Deserializer
from webhook.exceptions import ValidationError
import json

class TestWebhookHandler(TestCase):

    def setUp(self):
        self.signature_validator_mock =Mock(spec=SignatureValidator)
        self.deserializer_mock = Mock(spec=Deserializer)
        self.router_mock = Mock(spec=Router)
        self.webhook_handler = WebhookHandler(self.signature_validator_mock, self.deserializer_mock, self.router_mock)

    def json_schemaが誤っているときは400(self):
        self.deserializer_mock.deserialize.side_effect = ValidationError('fail')

        result = self.webhook_handler.handle({}, '')

        self.assertEqual(result['statusCode'], 400)

    def test_signatureが誤っているときは403(self):
        self.signature_validator_mock.validate_signature.side_effect = ValidationError('fail')

        result = self.webhook_handler.handle({}, '')

        self.assertEqual(result['statusCode'], 403)

    def test_validation等で例外が出ないときはrouterに処理が渡される(self):
        deserialize_result = { "deserialize": "result" }
        router_result = { "router": "result" }
        self.deserializer_mock.deserialize.return_value = deserialize_result
        self.router_mock.handle.return_value = router_result

        self.webhook_handler.handle({}, '')

        self.router_mock.handle.assert_any_call(deserialize_result)

    def test_validation等で例外が出ずrouterでも例外が出ないときは200(self):
        deserialize_result = { "deserialize": "result" }
        router_result = { "router": "result" }
        self.deserializer_mock.deserialize.return_value = deserialize_result
        self.router_mock.handle.return_value = router_result

        result = self.webhook_handler.handle({}, '')

        self.assertEqual(result['statusCode'], 200)


