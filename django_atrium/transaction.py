"""transaction file."""
from typing import List

import atrium
from atrium.models.transaction import Transaction as AtriumTransaction


class Transaction:
    """Transaction class."""

    def __init__(self, client: atrium.AtriumClient):
        """Init for Transaction."""
        self.client = client

    def read_transaction(
        self, transaction_guid: str, user_guid: str
    ) -> AtriumTransaction:
        """Read a transaction.

        Args:
            transaction_guid: A unique identifier for the transaction. Defined
                by MX.
            user_guid: A unique identifier for a user. Defined by MX.

        Returns:
            An Atrium transaction.

        """
        res = self.client.transactions.read_transaction(transaction_guid, user_guid)
        return res.transaction

    def list_transactions_for_account(
        self,
        account_guid: str,
        user_guid: str,
        page: int = 1,
        records_per_page: int = 25,
        **kwargs
    ) -> List[AtriumTransaction]:
        """List all the transactions for an account.

        Args:
            account_guid: A unique identifier for an account. Defined by MX.
            user_guid: A unique identifier for a user. Defined by MX.
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
                **kwargs
            )
            transactions += res.transactions

            if res.pagination.current_page == res.pagination.total_pages:
                break

            page += 1

        return transactions

    def list_transactions_for_member(
        self,
        member_guid: str,
        user_guid: str,
        page: int = 1,
        records_per_page: int = 25,
        **kwargs
    ) -> List[AtriumTransaction]:
        """List all of a member's transactions.

        Args:
            member_guid: A unique identifier for a member. Defined by MX.
            user_guid: A unique identifier for a user. Defined by MX.
            page: The page number to start the search.
            records_per_page: The number of records to retrieve with
                each request. Max is 1000.
            **from_date: A date string that specifies the start date.
            **to_date: A date string that specifies the end date.

        Returns:
            A list of an Atrium member's transaction.

        """
        transactions = []

        while True:
            res = self.client.members.list_member_transactions(
                member_guid,
                user_guid,
                page=page,
                records_per_page=records_per_page,
                **kwargs
            )
            transactions += res.transactions

            if res.pagination.current_page == res.pagination.total_pages:
                break

            page += 1

        return transactions

    def list_transactions_for_user(
        self, user_guid, page: int = 1, records_per_page: int = 25, **kwargs
    ) -> List[AtriumTransaction]:
        """
        List all of the transactions for a user.

        Args:
            user_guid: A unique identifier for a user. Defined by MX.
            page: The page number to start the search.
            records_per_page: The number of records to retrieve with
                each request. Max is 1000.
            **from_date: A date string that specifies the start date.
            **to_date: A date string that specifies the end date.

        Returns:
            A list of an Atrium user's transactions.

        """
        transactions = []

        while True:
            res = self.client.transactions.list_user_transactions(
                user_guid, page=page, records_per_page=records_per_page, **kwargs
            )
            transactions += res.transactions

            if res.pagination.current_page == res.pagination.total_pages:
                break

            page += 1

        return transactions
