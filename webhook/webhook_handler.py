import logging
import os
import json

from webhook.router import Router
from webhook.exceptions import ValidationError
from webhook.helpers.signature_validator import SignatureValidator
from webhook.deserializer import Deserializer

class WebhookHandler():
    def __init__(self, signature_validator=SignatureValidator(), deserializer=Deserializer(), router=Router()):
        self.__signature_validator = signature_validator
        self.__deserializer = deserializer
        self.__router = router

    def handle(self, headers, body):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        logger.debug(headers)

        try: 
            self.__signature_validator.validate_signature(headers.get('X-ChatWorkWebhookSignature'), body)
        except ValidationError as err:
            logger.debug(err.message)
            logger.debug(body)
            return self.__response_body(403, {"message": err.message})

        try:
            json_body = self.__deserializer.deserialize(body)
        except ValidationError as err:
            logger.debug(err.message)
            logger.debug(body)
            return self.__response_body(400, {"message": err.message})

        logger.debug('valid json schema')
        result = self.__router.handle(json_body)

        return self.__response_body(200, {"message": result})

    def __response_body(self, statusCode, bodydic):
        return {
            "statusCode": statusCode,
            "body": json.dumps(bodydic)
        }
