import unittest

from django_atrium import AtriumClient


class TestAtrium(unittest.TestCase):
    def test_client(self):
        client = AtriumClient()
        self.assertIsInstance(client, AtriumClient)


if __name__ == '__main__':
    unittest.main()
