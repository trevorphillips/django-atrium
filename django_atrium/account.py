"""account file."""
from typing import List

import atrium
from atrium.models.account import Account as AtriumAccount


class Account:
    """Account class."""

    def __init__(self, client: atrium.AtriumClient):
        """Init for Account."""
        self.client = client

    def read_account(self, account_guid: str, user_guid: str) -> AtriumAccount:
        """Read an account.

        Args:
            account_guid: A unique identifier for an account. Defined by MX.
            user_guid: A unique identifier for the user. Defined by MX.

        Returns:
            An atrium account.

        """
        res = self.client.accounts.read_account(account_guid, user_guid)
        return res.account

    def list_accounts_for_user(
        self, user_guid: str, page: int = 1, records_per_page: int = 25
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
                user_guid, page=page, records_per_page=records_per_page
            )
            accounts += res.accounts

            if res.pagination.current_page == res.pagination.total_pages:
                break

            page += 1

        return accounts

    def list_accounts_for_member(
        self,
        member_guid: str,
        user_guid: str,
        page: int = 1,
        records_per_page: int = 25,
    ) -> List[AtriumAccount]:
        """List a member's accounts.

        Args:
            member_guid: A unique identifier for the member. Defined by MX.
            user_guid: A unique identifier for the user. Defined by MX.
            page: The page number to start the search.
            records_per_page: The number of records to retrieve with
                each request. Max is 1000.

        Returns:
            A list of an Atrium member's accounts.

        """
        accounts = []

        while True:
            res = self.client.members.list_member_accounts(
                member_guid, user_guid, page=page, records_per_page=records_per_page
            )
            accounts += res.accounts

            if res.pagination.current_page == res.pagination.total_pages:
                break

            page += 1

        return accounts
