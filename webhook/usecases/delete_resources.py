import boto3

from webhook.helpers.amazon_sns_publish_service import AmazonSnsPublishService
from webhook.helpers.chatwork_send_comment_service import ChatworkSendCommentService


class DeleteResources:

  def __init__(
    self,
    amazon_sns_publish_service=AmazonSnsPublishService(),
    chatwork_send_comment_service = ChatworkSendCommentService()):

    self.__amazon_sns_publish_service=amazon_sns_publish_service
    self.__chatwork_send_comment_service=chatwork_send_comment_service

  def execute(self):

    self.__amazon_sns_publish_service.execute(
        'delete resources by chatbot', 'delete resources by chatbot')
    self.__chatwork_send_comment_service.execute(u'from bot: 削除処理が開始されました')
