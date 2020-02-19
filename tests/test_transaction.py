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

    # def test_list_transactions_for_account(self):
    #     user = self._client.create_user('test_identifier3')
    #     institution_code = 'mxbank'
    #     institution_creds = self._client.read_credentials_for_institution(
    #         institution_code)
    #     member = self._client.create_member(user.guid, 'test_atrium',
    #                                         'password', institution_creds,
    #                                         institution_code)
    #     accounts = self._client.list_accounts_for_member(
    #         member.guid, user.guid)
    #     transactions = self._client.list_transactions_for_account(
    #         accounts[0].guid, user.guid)
    #     self.assertIsInstance(transactions, list)

    def test_list_transactions_for_member(self):
        user = self._client.create_user("test_identifier14")
        institution_code = "mxbank"
        institution_creds = self._client.read_credentials_for_institution(
            institution_code
        )
        member = self._client.create_member(
            user.guid, "test_atrium", "password", institution_creds, institution_code
        )
        transactions = self._client.list_transactions_for_member(member.guid, user.guid)
        self.assertIsInstance(transactions, list)

    def test_list_transactions_for_user(self):
        user = self._client.create_user("test_identifier9")
        transactions = self._client.list_transactions_for_user(user.guid)
        self.assertIsInstance(transactions, list)
