"""merchant file."""
import atrium
from atrium.models.merchant import Merchant as AtriumMerchant


class Merchant:
    """Merchant class."""

    def __init__(self, client: atrium.AtriumClient):
        """Init for Merchant."""
        self.client = client

    def read_merchant(self, merchant_guid: str) -> AtriumMerchant:
        """Read a merchant.

        Args:
            merchant_guid: The unique identifier for the merchant. Defined by MX.

        Returns:
            An Atrium merchant.

        """
        res = self.client.merchants.read_merchant(merchant_guid)
        return res.merchant
