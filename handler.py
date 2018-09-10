from webhook.webhook_handler import WebhookHandler

def handle(event, context):
    body = event.get('body')  # Todo ErrorHandle

    headers = event.get('headers')

    return WebhookHandler().handle(headers, body)
