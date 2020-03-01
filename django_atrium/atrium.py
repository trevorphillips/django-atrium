"""atrium file."""
import os

import atrium
from django.conf import settings

from .account import Account
from .connect_widget import ConnectWidget
from .institution import Institution
from .member import Member
from .merchant import Merchant
from .transaction import Transaction
from .user import User

ATRIUM_API_KEY = os.environ.get("ATRIUM_API_KEY")
ATRIUM_CLIENT_ID = os.environ.get("ATRIUM_CLIENT_ID")
ATRIUM_URL = os.environ.get("ATRIUM_URL")

if ATRIUM_API_KEY is None and settings.configured:
    ATRIUM_API_KEY = settings.ATRIUM_API_KEY

if ATRIUM_CLIENT_ID is None and settings.configured:
    ATRIUM_CLIENT_ID = settings.ATRIUM_CLIENT_ID

if ATRIUM_URL is None and settings.configured:
    ATRIUM_URL = settings.ATRIUM_URL

if ATRIUM_API_KEY is None:
    raise Exception("Unable to determine ATRIUM_API_KEY variable.")
if ATRIUM_CLIENT_ID is None:
    raise Exception("Unable to determine ATRIUM_CLIENT_ID variable.")
if ATRIUM_URL is None:
    raise Exception("Unable to determine ATRIUM_URL variable.")


class AtriumClient(
    Account, ConnectWidget, Institution, Member, Merchant, Transaction, User
):
    """AtriumClient class."""

    def __init__(self):
        """Init for AtriumClient."""
        self.client = atrium.AtriumClient(ATRIUM_API_KEY, ATRIUM_CLIENT_ID, ATRIUM_URL)
        super().__init__(self.client)
