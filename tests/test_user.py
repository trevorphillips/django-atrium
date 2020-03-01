import time
import unittest

from atrium.models.user import User as AtriumUser

from django_atrium import AtriumClient


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._client = AtriumClient()

    @classmethod
    def tearDown(cls):
        users = cls._client.list_users()

        for user in users:
            cls._client.delete_user(user.guid)

    def test_create_user_with_defaults(self):
        user = self._client.create_user("test_identifier")
        self.assertIsInstance(user, AtriumUser)
        self.assertEqual(user.identifier, "test_identifier")
        self.assertFalse(user.is_disabled)
        self.assertIsNone(user.metadata)

    def test_create_user_with_modified_defaults(self):
        user = self._client.create_user(
            "test_identifier", is_disabled=True, metadata="Hello I am metadata"
        )
        self.assertIsInstance(user, AtriumUser)
        self.assertEqual(user.identifier, "test_identifier")
        self.assertTrue(user.is_disabled)
        self.assertEqual(user.metadata, "Hello I am metadata")

    def test_read_user(self):
        created_user = self._client.create_user("test_identifier")
        user = self._client.read_user(created_user.guid)
        self.assertIsInstance(user, AtriumUser)
        self.assertEqual(user.identifier, "test_identifier")
        self.assertFalse(user.is_disabled)
        self.assertIsNone(user.metadata)

    def test_update_user(self):
        created_user = self._client.create_user("test_identifier")
        self.assertIsInstance(created_user, AtriumUser)
        self.assertEqual(created_user.identifier, "test_identifier")
        self.assertFalse(created_user.is_disabled)
        self.assertIsNone(created_user.metadata)

        user = self._client.update_user(
            created_user.guid, is_disabled=True, metadata="Hello I am metadata"
        )
        self.assertIsInstance(user, AtriumUser)
        self.assertEqual(user.identifier, "test_identifier")
        self.assertTrue(user.is_disabled)
        self.assertEqual(user.metadata, "Hello I am metadata")

    def test_delete_user(self):
        created_user = self._client.create_user("test_identifier")
        self.assertIsInstance(created_user, AtriumUser)
        self.assertEqual(created_user.identifier, "test_identifier")
        self.assertFalse(created_user.is_disabled)
        self.assertIsNone(created_user.metadata)

        user = self._client.delete_user(created_user.guid)
        self.assertIsNone(user)

    def test_list_users(self):
        _ = self._client.create_user("test_identifier")

        users = self._client.list_users()
        self.assertIsInstance(users, list)
