from unittest import TestCase
from unittest.mock import Mock

from webhook.router import Router
from webhook.usecases.delete_resources import DeleteResources


class TestRouter(TestCase):
    def setUp(self):
        self.delete_resources_mock = Mock(spec=DeleteResources)
        self.router = Router(self.delete_resources_mock)
        self.account_id = 999999
        self.other_account_id = 1
        self.router._Router__account_id = self.account_id


    def test_正しく削除リソーススクリプトにルーティングされる(self):

        self.delete_resources_mock.execute.return_value = None
        
        self.router.handle({
            "webhook_event": {
                "to_account_id": self.account_id,
                "body": f"[To ${self.account_id}] delete resources"
            }
        })

        self.delete_resources_mock.execute.assert_any_call()

    def test_アカウントが違うなら削除スクリプトは実行されない(self):
        self.delete_resources_mock.execute.return_value = None
        
        self.router.handle({
            "webhook_event": {
                "to_account_id": self.other_account_id,
                "body": f"[To ${self.other_account_id}] delete resources"
            }
        })

        self.delete_resources_mock.execute.assert_not_called()
