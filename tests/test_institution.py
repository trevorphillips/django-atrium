import unittest

from atrium.models.credential_response import (
    CredentialResponse as AtriumCredentialResponse,
)
from atrium.models.institution import Institution as AtriumInstitution

from django_atrium import AtriumClient


class TestInstitution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._client = AtriumClient()

    @classmethod
    def tearDownClass(cls):
        users = cls._client.list_users()

        for user in users:
            cls._client.delete_user(user.guid)

    def test_read_institution(self):
        institution = self._client.read_institution("mxbank")
        self.assertIsInstance(institution, AtriumInstitution)
        self.assertEqual(institution.code, "mxbank")

    def test_list_institutions_with_name(self):
        institutions = self._client.list_institutions(name="MX Bank")
        self.assertIsInstance(institutions, list)
        self.assertEqual(len(institutions), 1)

    def test_list_institutions_with_acc_id(self):
        institutions = self._client.list_institutions(
            supports_account_identification=True
        )
        self.assertIsInstance(institutions, list)
        self.assertEqual(len(institutions), 5)

    def test_list_institutions_with_acc_statements(self):
        institutions = self._client.list_institutions(supports_account_statement=True)
        self.assertIsInstance(institutions, list)
        self.assertEqual(len(institutions), 4)

    def test_list_institutions_with_acc_verification(self):
        institutions = self._client.list_institutions(
            supports_account_verification=True
        )
        self.assertIsInstance(institutions, list)
        self.assertEqual(len(institutions), 11)

    def test_list_institutions_with_transaction_history(self):
        institutions = self._client.list_institutions(supports_transaction_history=True)
        self.assertIsInstance(institutions, list)
        self.assertEqual(len(institutions), 5)

    def test_read_credentials_for_institution(self):
        institution = self._client.read_credentials_for_institution("mxbank")
        self.assertIsInstance(institution, list)
        self.assertIsInstance(institution[0], AtriumCredentialResponse)
        self.assertIsInstance(institution[1], AtriumCredentialResponse)
