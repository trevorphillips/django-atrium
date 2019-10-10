"""user file."""
from typing import List

import atrium
from atrium.models.transaction import Transaction as AtriumTransaction
from atrium.models.user import User as AtriumUser


class User:
    """User class."""
    def __init__(self, client: atrium.AtriumClient):
        """Init for User."""
        self.client = client

    def create_user(self, identifier: str, **kwargs) -> AtriumUser:
        """Create a user.

        Args:
            identifier: A unique, enforced identifier for the user, defined by
                you.
            **is_disabled: A boolean indicating if a user is active. True if
                you want the user disabled, false otherwise.
            **metadata: Additional information you can store about this user.

        Returns:
            An Atrium user.

        """
        body = atrium.UserCreateRequestBody(user={
            'identifier': identifier,
            **kwargs
        })

        res = self.client.users.create_user(body)
        return res.user

    def read_user(self, user_guid: str) -> AtriumUser:
        """Read a user.

        Args:
            user_guid: A unique identifier for the user. Defined by MX.

        Returns:
            An Atrium user.

        """
        res = self.client.users.read_user(user_guid)
        return res.user

    def update_user(self, user_guid: str, **kwargs) -> AtriumUser:
        """Update a user.

        Args:
            user_guid: A unique identifier for the user. Defined by MX.
            **identifier: A unique, enforced identifier for the user, defined
                by you.
            **is_disabled: A boolean indicating if a user is active. True if
                    you want the user disabled, false otherwise.
            **metadata: Additional information you can store about this user.

        Returns:
            An Atrium user.

        """
        body = atrium.UserCreateRequestBody(user={**kwargs})

        res = self.client.users.update_user(user_guid, body=body)
        return res.user

    def delete_user(self, user_guid: str):
        """Delete a user.

        Args:
            user_guid: A unique identifier for the user. Defined by MX.

        """
        self.client.users.delete_user(user_guid)

    def list_users(self, page: int = 1,
                   records_per_page: int = 25) -> List[AtriumUser]:
        """List all the users.

        Args:
            page: The page number to start the search.
            records_per_page: The number of records to retrieve with
                each request. Max is 1000.

        Returns:
            A list of Atrium users.

        """
        users = []

        while True:
            res = self.client.users.list_users(
                page=page, records_per_page=records_per_page)
            users += res.users

            if res.pagination.current_page == res.pagination.total_pages:
                break

            page += 1

        return users

    def list_transactions_for_user(self,
                                   user_guid,
                                   page: int = 1,
                                   records_per_page: int = 25,
                                   **kwargs) -> List[AtriumTransaction]:
        """
        List all of the transactions for a user.

        Args:
            user_guid: A unique identifier for the user. Defined by MX.
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
                user_guid,
                page=page,
                records_per_page=records_per_page,
                **kwargs)
            transactions += res.transactions

            if res.pagination.current_page == res.pagination.total_pages:
                break

            page += 1

        return transactions
