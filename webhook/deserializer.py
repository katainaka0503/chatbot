
import json
import jsonschema
from webhook.exceptions import ValidationError

class Deserializer:
    def deserialize(self, body):
        if body is None:
            raise ValidationError('Request body was empty')

        try:
            json_body = json.loads(body)
        except json.JSONDecodeError as err:
            raise ValidationError(err.msg)

        schema = {
            "type": "object",
            "properties": {
                "webhook_setting_id": {"type": "string"},
                "webhook_event_type": {"type": "string"},
                "webhook_event_time": {"type": "integer"},
                "webhook_event": {
                    "type": "object",
                    "properties": {
                        "from_account_id": {"type": "integer"},
                        "to_account_id": {"type": "integer"},
                        "account_id": {"type": "integer"},
                        "room_id": {"type": "integer"},
                        "message_id": {"type": "string"},
                        "body": {"type": "string"},
                        "send_time": {"type": "integer"},
                        "update_time": {"type": "integer"}
                    },
                    "required": [
                        "room_id",
                        "message_id",
                        "account_id",
                        "body",
                        "send_time",
                        "update_time"
                    ]
                }
            },
            "required": [
                "webhook_setting_id",
                "webhook_event_type",
                "webhook_event_time",
                "webhook_event"
            ]
        }

        try:
            jsonschema.validate(json_body, schema)
        except jsonschema.ValidationError as err:
            raise ValidationError(err.message)

        return json_body
