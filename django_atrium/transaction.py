import atrium
from atrium.rest import ApiException


class Transaction:
    def __init__(self, client):
        self.client = client

    def read_transaction(self, transaction_guid, user_guid):
        """Read a transaction.

        Parameters
        ----------
        transaction_guid : str
            A unique identifier for the transaction. Defined by MX.
        user_guid : str
            A unique identifier for the user. Defined by MX.

        Returns
        -------
        transaction:
            An Atrium transaction.

        Raises
        -----
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        try:
            response = self.client.transactions.read_transaction(
                transaction_guid, user_guid)
            return response.transaction
        except ApiException as e:
            print(e)

    def list_transactions_for_user(self, user_guid, **kwargs):
        """
        List all of the transactions for a user.

        Parameters
        ----------
        user_guid : str
            A unique identifier for the user. Defined by MX.
        from_date : str, optional
            Filter transactions from this date.
        to_date : str, optional
            Filter transactions to this date.

        Returns
        -------
        transactions : list
            A list of an Atrium user's transactions.


        Raises
        -----
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        transactions = []
        page = 1
        records_per_page = 100

        try:
            while True:
                response = self.client.transactions.list_user_transactions(
                    user_guid,
                    page=page,
                    records_per_page=records_per_page,
                    **kwargs)
                transactions += response.transactions

                if response.pagination.current_page <= response.pagination.total_pages:
                    break

                page += 1

            return transactions
        except ApiException as e:
            print(e)
