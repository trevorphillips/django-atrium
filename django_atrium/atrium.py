"""atrium file."""
import atrium
from django.conf import settings

from .account import Account
from .connect_widget import ConnectWidget
from .institution import Institution
from .member import Member
from .transaction import Transaction
from .user import User

if not settings.configured:
    import os

    ATRIUM_API_KEY = os.environ.get("ATRIUM_API_KEY")
    ATRIUM_CLIENT_ID = os.environ.get("ATRIUM_CLIENT_ID")
    ATRIUM_URL = os.environ.get("ATRIUM_URL")

    if ATRIUM_API_KEY is None:
        raise Exception(
            "ATRIUM_API_KEY was not set in Django settings or environment variables."
        )
    elif ATRIUM_CLIENT_ID is None:
        raise Exception(
            "ATRIUM_CLIENT_ID was not set in Django settings or environment variables."
        )
    elif ATRIUM_URL is None:
        raise Exception(
            "ATRIUM_URL was not set in Django settings or environment variables."
        )

else:
    ATRIUM_API_KEY = settings.ATRIUM_API_KEY
    ATRIUM_CLIENT_ID = settings.ATRIUM_CLIENT_ID
    ATRIUM_URL = settings.ATRIUM_URL


class AtriumClient(Account, ConnectWidget, Institution, Member, Transaction, User):
    """AtriumClient class."""

    def __init__(self):
        """Init for AtriumClient."""
        self.client = atrium.AtriumClient(ATRIUM_API_KEY, ATRIUM_CLIENT_ID, ATRIUM_URL)
        super().__init__(self.client)
