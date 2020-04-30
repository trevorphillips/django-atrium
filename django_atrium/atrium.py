"""atrium file."""
import os
import atrium
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from .account import Account
from .connect_widget import ConnectWidget
from .institution import Institution
from .member import Member
from .merchant import Merchant
from .transaction import Transaction
from .user import User

try:
    ATRIUM_API_KEY = settings.ATRIUM_API_KEY
    ATRIUM_CLIENT_ID = settings.ATRIUM_CLIENT_ID
    ATRIUM_URL = settings.ATRIUM_URL
except ImproperlyConfigured:
    ATRIUM_API_KEY = os.environ["ATRIUM_API_KEY"]
    ATRIUM_CLIENT_ID = os.environ["ATRIUM_CLIENT_ID"]
    ATRIUM_URL = os.environ["ATRIUM_URL"]


class AtriumClient(
    Account, ConnectWidget, Institution, Member, Merchant, Transaction, User
):
    """AtriumClient class."""

    def __init__(self):
        """Init for AtriumClient."""
        self.client = atrium.AtriumClient(ATRIUM_API_KEY, ATRIUM_CLIENT_ID, ATRIUM_URL)
        super().__init__(self.client)
