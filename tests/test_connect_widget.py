import unittest

from atrium.models.connect_widget import ConnectWidget as AtriumConnectWidget

from django_atrium import AtriumClient


class TestConnectWidget(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._client = AtriumClient()

    @classmethod
    def tearDownClass(cls):
        users = cls._client.list_users()

        for user in users:
            cls._client.delete_user(user.guid)

    def test_connect_widget_with_defaults(self):
        user = self._client.create_user("test_identifier1")
        connect_widget = self._client.get_connect_widget(user.guid)
        self.assertIsInstance(connect_widget, AtriumConnectWidget)

    def test_connect_widget_with_institution(self):
        user = self._client.create_user("test_identifier2")
        connect_widget = self._client.get_connect_widget(
            user.guid, current_institution_code="mxbank"
        )
        self.assertIsInstance(connect_widget, AtriumConnectWidget)

    def test_connect_widget_with_member(self):
        user = self._client.create_user("test_identifier3")
        institution_code = "mxbank"
        institution_creds = self._client.read_credentials_for_institution(
            institution_code
        )
        member = self._client.create_member(
            user.guid, "test_atrium", "password", institution_creds, institution_code
        )
        connect_widget = self._client.get_connect_widget(
            user.guid, current_member_guid=member.guid
        )
        self.assertIsInstance(connect_widget, AtriumConnectWidget)

    def test_connect_widget_update_credentials(self):
        user = self._client.create_user("test_identifier4")
        institution_code = "mxbank"
        institution_creds = self._client.read_credentials_for_institution(
            institution_code
        )
        member = self._client.create_member(
            user.guid, "test_atrium", "password", institution_creds, institution_code
        )
        connect_widget = self._client.get_connect_widget(
            user.guid, current_member_guid=member.guid, update_credentials=True
        )
        self.assertIsInstance(connect_widget, AtriumConnectWidget)
