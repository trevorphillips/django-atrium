import time
import unittest

from atrium.models.credential_response import (
    CredentialResponse as AtriumCredentialResponse,
)
from atrium.models.member import Member as AtriumMember
from atrium.models.member_connection_status import (
    MemberConnectionStatus as AtriumMemberConnectionStatus,
)

from django_atrium import AtriumClient


class TestMember(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._client = AtriumClient()

    @classmethod
    def tearDown(cls):
        users = cls._client.list_users()

        for user in users:
            cls._client.delete_user(user.guid)

    def test_create_member_with_defaults(self):
        user = self._client.create_user("test_identifier")
        institution_code = "mxbank"
        institution_creds = self._client.read_credentials_for_institution(
            institution_code
        )
        member = self._client.create_member(
            user.guid, "test_atrium", "password", institution_creds, institution_code
        )
        self.assertIsInstance(member, AtriumMember)
        self.assertIsNone(member.identifier)
        self.assertIsNone(member.metadata)

    def test_create_member_with_modified_defaults(self):
        user = self._client.create_user("test_identifier")
        institution_code = "mxbank"
        institution_creds = self._client.read_credentials_for_institution(
            institution_code
        )
        member = self._client.create_member(
            user.guid,
            "test_atrium",
            "password",
            institution_creds,
            institution_code,
            identifier="test_identifier",
            metadata="Hello I am metadata",
        )
        self.assertIsInstance(member, AtriumMember)
        self.assertEqual(member.identifier, "test_identifier")
        self.assertEqual(member.metadata, "Hello I am metadata")

    def test_read_member(self):
        user = self._client.create_user("test_identifier")
        institution_code = "mxbank"
        institution_creds = self._client.read_credentials_for_institution(
            institution_code
        )
        created_member = self._client.create_member(
            user.guid, "test_atrium", "password", institution_creds, institution_code
        )
        member = self._client.read_member(created_member.guid, user.guid)
        self.assertIsInstance(member, AtriumMember)

    # def test_update_member(self):
    #     user = self._client.create_user("test_identifier")
    #     institution_code = "mxbank"
    #     institution_creds = self._client.read_credentials_for_institution(
    #         institution_code
    #     )
    #     created_member = self._client.create_member(
    #         user.guid, "test_atrium", "password", institution_creds, institution_code
    #     )
    #     self.assertIsInstance(created_member, AtriumMember)
    #     self.assertIsNone(created_member.identifier)
    #     self.assertIsNone(created_member.metadata)
    #     print(vars(created_member))

    #     member = self._client.update_member(
    #         created_member.guid,
    #         user.guid,
    #         identifier="test_identifier",
    #         metadata="Hello I am metadata",
    #     )
    #     self.assertIsInstance(member, AtriumMember)
    #     self.assertEqual(member.identifier, "test_identifier")
    #     self.assertEqual(member.metadata, "Hello I am metadata")

    def test_delete_member(self):
        user = self._client.create_user("test_identifier")
        institution_code = "mxbank"
        institution_creds = self._client.read_credentials_for_institution(
            institution_code
        )
        created_member = self._client.create_member(
            user.guid, "test_atrium", "password", institution_creds, institution_code
        )

        member = self._client.delete_member(created_member.guid, user.guid)
        self.assertIsNone(member)

    def test_list_members_for_user(self):
        user = self._client.create_user("test_identifier")
        institution_code = "mxbank"
        institution_creds = self._client.read_credentials_for_institution(
            institution_code
        )
        _ = self._client.create_member(
            user.guid, "test_atrium", "password", institution_creds, institution_code
        )

        members = self._client.list_members_for_user(user.guid)
        self.assertIsInstance(members, list)

    def test_aggregate_member(self):
        user = self._client.create_user("test_identifier")
        institution_code = "mxbank"
        institution_creds = self._client.read_credentials_for_institution(
            institution_code
        )
        created_member = self._client.create_member(
            user.guid, "test_atrium", "password", institution_creds, institution_code
        )
        member = self._client.aggregate_member(created_member.guid, user.guid)
        self.assertIsInstance(member, AtriumMember)

    def test_read_connection_status_for_member(self):
        user = self._client.create_user("test_identifier")
        institution_code = "mxbank"
        institution_creds = self._client.read_credentials_for_institution(
            institution_code
        )
        created_member = self._client.create_member(
            user.guid, "test_atrium", "password", institution_creds, institution_code
        )
        status = self._client.read_connection_status_for_member(
            created_member.guid, user.guid
        )
        self.assertIsInstance(status, AtriumMemberConnectionStatus)

    def test_list_mfa_challenges_for_member_no_challenges(self):
        user = self._client.create_user("test_identifier")
        institution_code = "mxbank"
        institution_creds = self._client.read_credentials_for_institution(
            institution_code
        )
        member = self._client.create_member(
            user.guid, "test_atrium", "password", institution_creds, institution_code
        )
        challenges = self._client.list_mfa_challenges_for_member(member.guid, user.guid)
        self.assertIsNone(challenges)

    def test_list_mfa_challenges_for_member_with_text_challenges(self):
        user = self._client.create_user("test_identifier")
        institution_code = "mxbank"
        institution_creds = self._client.read_credentials_for_institution(
            institution_code
        )
        member = self._client.create_member(
            user.guid, "test_atrium", "challenge", institution_creds, institution_code
        )
        time.sleep(15)
        challenges = self._client.list_mfa_challenges_for_member(member.guid, user.guid)
        self.assertIsInstance(challenges, list)

    def test_list_mfa_challenges_for_member_with_options_challenges(self):
        user = self._client.create_user("test_identifier")
        institution_code = "mxbank"
        institution_creds = self._client.read_credentials_for_institution(
            institution_code
        )
        member = self._client.create_member(
            user.guid, "test_atrium", "options", institution_creds, institution_code
        )
        time.sleep(15)
        challenges = self._client.list_mfa_challenges_for_member(member.guid, user.guid)
        self.assertIsInstance(challenges, list)

    def test_list_mfa_challenges_for_member_with_image_challenges(self):
        user = self._client.create_user("test_identifier")
        institution_code = "mxbank"
        institution_creds = self._client.read_credentials_for_institution(
            institution_code
        )
        member = self._client.create_member(
            user.guid, "test_atrium", "image", institution_creds, institution_code
        )
        time.sleep(15)
        challenges = self._client.list_mfa_challenges_for_member(member.guid, user.guid)
        self.assertIsInstance(challenges, list)

    def test_list_credentials_for_member(self):
        user = self._client.create_user("test_identifier")
        institution_code = "mxbank"
        institution_creds = self._client.read_credentials_for_institution(
            institution_code
        )
        member = self._client.create_member(
            user.guid, "test_atrium", "password", institution_creds, institution_code
        )
        credentials = self._client.list_credentials_for_member(member.guid, user.guid)
        self.assertIsInstance(credentials, list)
        self.assertIsInstance(credentials[0], AtriumCredentialResponse)
        self.assertIsInstance(credentials[1], AtriumCredentialResponse)
