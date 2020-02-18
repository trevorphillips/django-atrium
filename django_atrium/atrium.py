"""atrium file."""
import atrium
from django.conf import settings

from .account import Account
from .connect_widget import ConnectWidget
from .institution import Institution
from .member import Member
from .transaction import Transaction
from .user import User

settings.configure()


class AtriumClient(Account, ConnectWidget, Institution, Member, Transaction, User):
    """AtriumClient class."""

    def __init__(self):
        """Init for AtriumClient."""
        self.client = atrium.AtriumClient(
            settings.ATRIUM_API_KEY, settings.ATRIUM_CLIENT_ID, settings.ATRIUM_URL
        )

        super().__init__(self.client)
