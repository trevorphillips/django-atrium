import unittest

from atrium.models.transaction import Transaction as AtriumTransaction

from django_atrium import AtriumClient


class TestTransaction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._client = AtriumClient()

    @classmethod
    def tearDownClass(cls):
        users = cls._client.list_users()

        for user in users:
            cls._client.delete_user(user.guid)

    # def test_read_transaction(self):
    #     user = self._client.create_user('test_identifier1')
    #     transactions = self._client.list_transactions_for_user(user.guid)
    #     transaction = self._client.read_transaction(transactions[0].guid,
    #                                                 user.guid)
    #     self.assertIsInstance(transaction, AtriumTransaction)
