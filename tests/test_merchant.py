import unittest

from atrium.models.merchant import Merchant as AtriumMerchant

from django_atrium import AtriumClient


class TestMerchant(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._client = AtriumClient()

    @classmethod
    def tearDown(cls):
        users = cls._client.list_users()

        for user in users:
            cls._client.delete_user(user.guid)

    def test_read_merchant(self):
        merchant_guid = "MCH-6e551748-9adc-804f-bf1f-0aa51db42df4"
        merchant = self._client.read_merchant(merchant_guid)
        self.assertIsInstance(merchant, AtriumMerchant)
        self.assertEqual(merchant.name, "76 Fuel")
