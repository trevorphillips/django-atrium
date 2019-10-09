"""transaction file."""
import atrium
from atrium.models.transaction import Transaction as AtriumTransaction


class Transaction:
    """Transaction class."""
    def __init__(self, client: atrium.AtriumClient):
        """Init for Transaction."""
        self.client = client

    def read_transaction(self, transaction_guid: str,
                         user_guid: str) -> AtriumTransaction:
        """Read a transaction.

        Args:
            transaction_guid: A unique identifier for the transaction. Defined
                by MX.
            user_guid: A unique identifier for the user. Defined by MX.

        Returns:
            An Atrium transaction.

        """
        res = self.client.transactions.read_transaction(
            transaction_guid, user_guid)
        return res.transaction
