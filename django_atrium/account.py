"""account file."""
from typing import List

import atrium
from atrium.models.account import Account as AtriumAccount
from atrium.models.transaction import Transaction as AtriumTransaction


class Account:
    """Account class."""
    def __init__(self, client: atrium.AtriumClient):
        """Init for Account."""
        self.client = client

    def read_account(self, account_guid: str, user_guid: str) -> AtriumAccount:
        """Read an account.

        Args:
            account_guid: A unique identifier for the account. Defined by MX.
            user_guid: A unique identifier for the user. Defined by MX.

        Returns:
            An atrium account.

        """
        res = self.client.accounts.read_account(account_guid, user_guid)
        return res.account

    def list_accounts_for_user(self,
                               user_guid: str,
                               page: int = 1,
                               records_per_page: int = 25
                               ) -> List[AtriumAccount]:
        """List all the accounts for a user.

        Args:
            user_guid: A unique identifier for the user. Defined by MX.
            page: The page number to start the search.
            records_per_page: The number of records to retrieve with
                each request. Max is 1000.

        Returns:
            A list of atrium accounts.

        """
        accounts = []

        while True:
            res = self.client.accounts.list_user_accounts(
                user_guid, page=page, records_per_page=records_per_page)
            accounts += res.accounts

            if res.pagination.current_page == res.pagination.total_pages:
                break

            page += 1

        return accounts

    def list_transactions_for_account(self,
                                      account_guid: str,
                                      user_guid: str,
                                      page: int = 1,
                                      records_per_page: int = 25,
                                      **kwargs) -> List[AtriumTransaction]:
        """List all the transactions for an account.

        Args:
            account_guid: A unique identifier for the account. Defined by MX.
            user_guid: A unique identifier for the user. Defined by MX.
            page: The page number to start the search.
            records_per_page: The number of records to retrieve with
                each request. Max is 1000.
            **from_date: A date string that specifies the start date.
            **to_date: A date string that specifies the end date.

        Returns:
            A list of an Atrium accounts's transactions.

        """
        transactions = []

        while True:
            res = self.client.accounts.list_account_transactions(
                account_guid,
                user_guid,
                page=page,
                records_per_page=records_per_page,
                **kwargs)
            transactions += res.transactions

            if res.pagination.current_page == res.pagination.total_pages:
                break

            page += 1

        return transactions
