import base64
import hmac
import hashlib
from webhook.exceptions import ValidationError
import os


class SignatureValidator:
    def __init__(self):
        self.__chatwork_webhook_token = os.environ.get(
            'CHATWORK_WEBHOOK_TOKEN')

    def validate_signature(self, signature, body):
        secret = base64.b64decode(self.__chatwork_webhook_token)
        body_bytes = bytes(body, 'ascii')
        digest = base64.b64encode(
            hmac.new(secret, body_bytes, hashlib.sha256).digest()).decode('ascii')

        if not signature == digest:
            raise ValidationError('signature is not valid')
