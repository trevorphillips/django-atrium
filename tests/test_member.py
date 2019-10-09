import unittest

from atrium.models.credential_response import \
    CredentialResponse as AtriumCredentialResponse
from atrium.models.member import Member as AtriumMember

from django_atrium import AtriumClient


class TestMember(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._client = AtriumClient()

    @classmethod
    def tearDownClass(cls):
        users = cls._client.list_users()

        for user in users:
            cls._client.delete_user(user.guid)

    def test_create_member_with_defaults(self):
        user = self._client.create_user('test_identifier1')
        institution_code = 'mxbank'
        institution_creds = self._client.read_credentials_for_institution(
            institution_code)
        member = self._client.create_member(user.guid, 'test_atrium',
                                            'password', institution_creds,
                                            institution_code)
        self.assertIsInstance(member, AtriumMember)
        self.assertIsNone(member.identifier)
        self.assertIsNone(member.metadata)

    def test_create_member_with_modified_defaults(self):
        user = self._client.create_user('test_identifier2')
        institution_code = 'mxbank'
        institution_creds = self._client.read_credentials_for_institution(
            institution_code)
        member = self._client.create_member(user.guid,
                                            'test_atrium',
                                            'password',
                                            institution_creds,
                                            institution_code,
                                            identifier='test_identifier3',
                                            metadata='Hello I am metadata')
        self.assertIsInstance(member, AtriumMember)
        self.assertEqual(member.identifier, 'test_identifier3')
        self.assertEqual(member.metadata, 'Hello I am metadata')

    def test_read_member(self):
        user = self._client.create_user('test_identifier4')
        institution_code = 'mxbank'
        institution_creds = self._client.read_credentials_for_institution(
            institution_code)
        created_member = self._client.create_member(user.guid, 'test_atrium',
                                                    'password',
                                                    institution_creds,
                                                    institution_code)
        member = self._client.read_member(created_member.guid, user.guid)
        self.assertIsInstance(member, AtriumMember)

    # def test_update_member(self):
    #     user = self._client.create_user('test_identifier5')
    #     institution_code = 'mxbank'
    #     institution_creds = self._client.read_credentials_for_institution(
    #         institution_code)
    #     created_member = self._client.create_member(user.guid, 'test_atrium',
    #                                                 'password',
    #                                                 institution_creds,
    #                                                 institution_code)
    #     self.assertIsInstance(created_member, AtriumMember)
    #     self.assertIsNone(created_member.identifier)
    #     self.assertIsNone(created_member.metadata)

    #     member = self._client.update_member(created_member.guid,
    #                                         user.guid,
    #                                         identifier='test_identifier6',
    #                                         metadata='Hello I am metadata')
    #     self.assertIsInstance(member, AtriumMember)
    #     self.assertEqual(member.identifier, 'test_identifier6')
    #     self.assertEqual(member.metadata, 'Hello I am metadata')

    def test_delete_member(self):
        user = self._client.create_user('test_identifier7')
        institution_code = 'mxbank'
        institution_creds = self._client.read_credentials_for_institution(
            institution_code)
        created_member = self._client.create_member(user.guid, 'test_atrium',
                                                    'password',
                                                    institution_creds,
                                                    institution_code)

        member = self._client.delete_member(created_member.guid, user.guid)
        self.assertIsNone(member)

    # def test_list_members(self):
    #     user = self._client.create_user('test_identifier8')
    #     institution_code = 'mxbank'
    #     institution_creds = self._client.read_credentials_for_institution(
    #         institution_code)
    #     _ = self._client.create_member(user.guid, 'test_atrium', 'password',
    #                                    institution_creds, institution_code)
    #     _ = self._client.create_member(user.guid, 'test_atrium', 'challenge',
    #                                    institution_creds, institution_code)

    #     members = self._client.list_members(user.guid)
    #     self.assertIsInstance(members, list)

    def test_aggregate_member(self):
        user = self._client.create_user('test_identifier9')
        institution_code = 'mxbank'
        institution_creds = self._client.read_credentials_for_institution(
            institution_code)
        created_member = self._client.create_member(user.guid, 'test_atrium',
                                                    'password',
                                                    institution_creds,
                                                    institution_code)
        member = self._client.aggregate_member(created_member.guid, user.guid)
        self.assertIsInstance(member, AtriumMember)

    def test_list_mfa_challenges_for_member_no_challenges(self):
        user = self._client.create_user('test_identifier10')
        institution_code = 'mxbank'
        institution_creds = self._client.read_credentials_for_institution(
            institution_code)
        member = self._client.create_member(user.guid, 'test_atrium',
                                            'password', institution_creds,
                                            institution_code)
        challenges = self._client.list_mfa_challenges_for_member(
            member.guid, user.guid)
        self.assertIsNone(challenges)

    # def test_list_mfa_challenges_for_member_with_challenges(self):
    #     user = self._client.create_user('test_identifier11')
    #     institution_code = 'mxbank'
    #     institution_creds = self._client.read_credentials_for_institution(
    #         institution_code)
    #     member = self._client.create_member(user.guid, 'test_atrium',
    #                                         'challenge', institution_creds,
    #                                         institution_code)
    #     challenges = self._client.list_mfa_challenges_for_member(
    #         member.guid, user.guid)
    #     self.assertIsInstance(challenges, list)

    def test_list_credentials_for_member(self):
        user = self._client.create_user('test_identifier12')
        institution_code = 'mxbank'
        institution_creds = self._client.read_credentials_for_institution(
            institution_code)
        member = self._client.create_member(user.guid, 'test_atrium',
                                            'password', institution_creds,
                                            institution_code)
        credentials = self._client.list_credentials_for_member(
            member.guid, user.guid)
        self.assertIsInstance(credentials, list)
        self.assertIsInstance(credentials[0], AtriumCredentialResponse)
        self.assertIsInstance(credentials[1], AtriumCredentialResponse)

    def test_list_accounts_for_member(self):
        user = self._client.create_user('test_identifier13')
        institution_code = 'mxbank'
        institution_creds = self._client.read_credentials_for_institution(
            institution_code)
        member = self._client.create_member(user.guid, 'test_atrium',
                                            'password', institution_creds,
                                            institution_code)
        accounts = self._client.list_accounts_for_member(
            member.guid, user.guid)
        self.assertIsInstance(accounts, list)

    def test_list_transactions_for_member(self):
        user = self._client.create_user('test_identifier14')
        institution_code = 'mxbank'
        institution_creds = self._client.read_credentials_for_institution(
            institution_code)
        member = self._client.create_member(user.guid, 'test_atrium',
                                            'password', institution_creds,
                                            institution_code)
        transactions = self._client.list_transactions_for_member(
            member.guid, user.guid)
        self.assertIsInstance(transactions, list)
