import time
import unittest

from atrium.models.account import Account as AtriumAccount

from django_atrium import AtriumClient


class TestAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._client = AtriumClient()

    @classmethod
    def tearDown(cls):
        users = cls._client.list_users()

        for user in users:
            cls._client.delete_user(user.guid)

    def test_read_account(self):
        user = self._client.create_user("test_identifier")
        institution_code = "mxbank"
        institution_creds = self._client.read_credentials_for_institution(
            institution_code
        )
        member = self._client.create_member(
            user.guid, "test_atrium", "password", institution_creds, institution_code
        )
        time.sleep(15)
        accounts = self._client.list_accounts_for_member(member.guid, user.guid)
        account = self._client.read_account(accounts[0].guid, user.guid)
        self.assertIsInstance(account, AtriumAccount)

    def test_list_accounts_for_user(self):
        user = self._client.create_user("test_identifier")
        institution_code = "mxbank"
        institution_creds = self._client.read_credentials_for_institution(
            institution_code
        )
        member = self._client.create_member(
            user.guid, "test_atrium", "password", institution_creds, institution_code
        )
        accounts = self._client.list_accounts_for_member(member.guid, user.guid)
        self.assertIsInstance(accounts, list)

    def test_list_accounts_for_member(self):
        user = self._client.create_user("test_identifier")
        institution_code = "mxbank"
        institution_creds = self._client.read_credentials_for_institution(
            institution_code
        )
        member = self._client.create_member(
            user.guid, "test_atrium", "password", institution_creds, institution_code
        )
        accounts = self._client.list_accounts_for_member(member.guid, user.guid)
        self.assertIsInstance(accounts, list)
