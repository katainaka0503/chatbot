import boto3
import os


class AmazonSnsPublishService:
  def __init__(self):
    self.__topic_arn = os.environ.get('DELETE_RESOURCES_TOPIC_ARN')
    self.__client = boto3.client('sns')

  def execute(self, subject, message):
    self.__client.publish(
        TopicArn = self.__topic_arn,
        Subject = subject,
        Message = message
    )