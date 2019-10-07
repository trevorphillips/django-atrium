import atrium

from .account import Account
from .connect_widget import ConnectWidget
from .institution import Institution
from .member import Member
from .transaction import Transaction
from .user import User

try:
    from django.conf import settings
except ImportError:
    raise Exception('Django has to be installed to use this module.')

settings.configure()


class AtriumClient(Account, ConnectWidget, Institution, Member, Transaction,
                   User):
    def __init__(self):
        self.client = atrium.AtriumClient(settings.MX_API_KEY,
                                          settings.MX_CLIENT_ID,
                                          settings.MX_ATRIUM_URL)

        super().__init__(self.client)
