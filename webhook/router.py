from webhook.usecases.delete_resources import DeleteResources

import logging
import os
import re

class Router():
  def __init__(self, delete_resources = DeleteResources()):
    self.__delete_resources = delete_resources
    self.__account_id = os.environ.get('CHATWORK_ACCOUNT_ID')

  def handle(self, http_body):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    message_body = http_body.get('webhook_event', {}).get('body')
    to_account_id = http_body.get('webhook_event', {}).get('to_account_id')

    #if to_account_id == self.__account_id and re.fullmatch("\[.*\]\s*delete resources", message_body) is not None:
    if message_body == "delete resources":
      logger.debug('Delete resources matched')
      self.__delete_resources.execute()
      return 'successfully executed'
    else:
      logger.debug('No route matched')