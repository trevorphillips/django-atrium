"""atrium file."""
import atrium

from .account import Account
from .connect_widget import ConnectWidget
from .institution import Institution
from .member import Member
from .transaction import Transaction
from .user import User

try:
    from django.conf import settings

    if not settings.configured:
        try:
            import os
            from dotenv import load_dotenv
            load_dotenv()
            settings.configure(MX_API_KEY=os.getenv('MX_API_KEY'),
                               MX_CLIENT_ID=os.getenv('MX_CLIENT_ID'),
                               MX_ATRIUM_URL=os.getenv('MX_ATRIUM_URL'))
        except Exception:
            raise ('Unable to load Django settings.')
except ImportError:
    raise ('Django must be installed to use this module.')


class AtriumClient(Account, ConnectWidget, Institution, Member, Transaction,
                   User):
    """AtriumClient class."""
    def __init__(self):
        """Init for AtriumClient."""
        self.client = atrium.AtriumClient(settings.MX_API_KEY,
                                          settings.MX_CLIENT_ID,
                                          settings.MX_ATRIUM_URL)

        super().__init__(self.client)
