from unittest import TestCase
from unittest.mock import Mock
from webhook.usecases.delete_resources import DeleteResources
from webhook.helpers.amazon_sns_publish_service import AmazonSnsPublishService
from webhook.helpers.chatwork_send_comment_service import ChatworkSendCommentService

class TestDeleteResources(TestCase):

  def setUp(self):
    self.amazon_sns_publish_service_mock = Mock(spec=AmazonSnsPublishService)
    self.chatwork_send_comment_service_mock = Mock(spec=ChatworkSendCommentService)
    self.delete_resources = DeleteResources(self.amazon_sns_publish_service_mock, self.chatwork_send_comment_service_mock)

  def test_SNSに正しくイベントを発行する(self):
    self.delete_resources.execute()

    self.amazon_sns_publish_service_mock.execute.assert_any_call('delete resources by chatbot', 'delete resources by chatbot')

  def test_Chatworkにコメントを登録する(self):
    self.delete_resources.execute()

    self.chatwork_send_comment_service_mock.execute.assert_any_call(u'from bot: 削除処理が開始されました')

      
