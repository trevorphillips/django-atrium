import unittest

from atrium.models.user import User as AtriumUser

from django_atrium import AtriumClient


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._client = AtriumClient()

    @classmethod
    def tearDownClass(cls):
        users = cls._client.list_users()

        for user in users:
            cls._client.delete_user(user.guid)

    def test_create_user_with_defaults(self):
        user = self._client.create_user("test_identifier1")
        self.assertIsInstance(user, AtriumUser)
        self.assertEqual(user.identifier, "test_identifier1")
        self.assertFalse(user.is_disabled)
        self.assertIsNone(user.metadata)

    def test_create_user_with_modified_defaults(self):
        user = self._client.create_user(
            "test_identifier2", is_disabled=True, metadata="Hello I am metadata"
        )
        self.assertIsInstance(user, AtriumUser)
        self.assertEqual(user.identifier, "test_identifier2")
        self.assertTrue(user.is_disabled)
        self.assertEqual(user.metadata, "Hello I am metadata")

    def test_read_user(self):
        created_user = self._client.create_user("test_identifier3")
        user = self._client.read_user(created_user.guid)
        self.assertIsInstance(user, AtriumUser)
        self.assertEqual(user.identifier, "test_identifier3")
        self.assertFalse(user.is_disabled)
        self.assertIsNone(user.metadata)

    def test_update_user(self):
        created_user = self._client.create_user("test_identifier4")
        self.assertIsInstance(created_user, AtriumUser)
        self.assertEqual(created_user.identifier, "test_identifier4")
        self.assertFalse(created_user.is_disabled)
        self.assertIsNone(created_user.metadata)

        user = self._client.update_user(
            created_user.guid, is_disabled=True, metadata="Hello I am metadata"
        )
        self.assertIsInstance(user, AtriumUser)
        self.assertEqual(user.identifier, "test_identifier4")
        self.assertTrue(user.is_disabled)
        self.assertEqual(user.metadata, "Hello I am metadata")

    def test_delete_user(self):
        created_user = self._client.create_user("test_identifier5")
        self.assertIsInstance(created_user, AtriumUser)
        self.assertEqual(created_user.identifier, "test_identifier5")
        self.assertFalse(created_user.is_disabled)
        self.assertIsNone(created_user.metadata)

        user = self._client.delete_user(created_user.guid)
        self.assertIsNone(user)

    def test_list_users(self):
        _ = self._client.create_user("test_identifier6")
        _ = self._client.create_user("test_identifier7")
        _ = self._client.create_user("test_identifier8")

        users = self._client.list_users()
        self.assertIsInstance(users, list)
