import atrium
from atrium.rest import ApiException


class Account:

    def __init__(self, client):
        self.client = client

    def read_account(self, account_guid, user_guid):
        """
        Read an account.

        Parameters
        ----------
        account_guid : str
            Unique identifier for the account. Defined by MX.
        user_guid : str
            A unique identifier for the user. Defined by MX.

        Raises
        -----
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        try:
            response = self.client.accounts.read_account(
                account_guid, user_guid
            )
            return response.account
        except ApiException as e:
            print("ApiException")

    def list_accounts_for_user(self, user_guid):
        """
        List all the accounts for a user.

        Parameters
        ----------
        user_guid : str
            A unique identifier for the user. Defined by MX.

        Raises
        -----
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        accounts = []
        page = 1
        records_per_page = 100

        try:
            while True:
                response = self.client.accounts.list_user_accounts(
                    user_guid, page=page, records_per_page=records_per_page
                )
                accounts += response.accounts

                if response.pagination.current_page <= response.pagination.total_pages:
                    break

                page += 1

            return accounts
        except ApiException as e:
            print("ApiException")

    def list_account_transactions(self, account_guid, user_guid, **kwargs):
        """
        List all of an account's transactions.

        Parameters
        ----------
        account_guid : str
            Unique identifier for the account. Defined by MX.
        user_guid : str
            A unique identifier for the user. Defined by MX.
        from_date : str, optional
            Filter transactions from this date.
        to_date : str, optional
            Filter transactions to this date.

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
                response = self.client.accounts.list_account_transactions(
                    account_guid, user_guid, page=page, records_per_page=records_per_page, **kwargs
                )
                transactions += response.transactions

                if response.pagination.current_page <= response.pagination.total_pages:
                    break

                page += 1

            return transactions
        except ApiException as e:
            print("ApiException")
