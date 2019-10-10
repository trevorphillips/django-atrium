"""member file."""
from typing import List

import atrium
from atrium.models.account import Account as AtriumAccount
from atrium.models.challenge import Challenge as AtriumChallenge
from atrium.models.credential_response import \
    CredentialResponse as AtriumCredentialResponse
from atrium.models.member import Member as AtriumMember
from atrium.models.member_connection_status import \
    MemberConnectionStatus as AtriumMemberConnectionStatus
from atrium.models.transaction import Transaction as AtriumTransaction


class Member:
    """Member class."""
    def __init__(self, client: atrium.AtriumClient):
        """Init for Member."""
        self.client = client

    def create_member(self, user_guid: str, username: str, password: str,
                      institution_creds: List[AtriumCredentialResponse],
                      institution_code: str, **kwargs) -> AtriumMember:
        """Create a member.

        Args:
            user_guid: A unique identifier for the user. Defined by MX.
            username: The username/email of the bank.
            password: The password of the bank.
            institution_code: A unique identifier for each institution,
                defined by MX.
            **identifier: A unique, enforced identifier for the user, defined
                by you.
            **metadata: Additional information you can store about this user.

        Returns:
            An Atrium member.

        """
        body = atrium.MemberCreateRequestBody(
            member={
                'credentials': [{
                    "guid": institution_creds[0].guid,
                    "value": username
                }, {
                    "guid": institution_creds[1].guid,
                    "value": password
                }],
                'institution_code':
                institution_code,
                **kwargs
            })

        res = self.client.members.create_member(user_guid, body)
        return res.member

    def read_member(self, member_guid: str, user_guid: str) -> AtriumMember:
        """Read a member.

        Args:
            member_guid: A unique identifier for the member. Defined by MX.
            user_guid: A unique identifier for the user. Defined by MX.

        Returns:
            An Atrium member.

        """
        res = self.client.members.read_member(member_guid, user_guid)
        return res.member

    def update_member(self, member_guid: str, user_guid: str,
                      **kwargs) -> AtriumMember:
        """Update a member.

        Args:
            member_guid: A unique identifier for the member. Defined by MX.
            user_guid: A unique identifier for the user. Defined by MX.
            **identifier: A unique, enforced identifier for the user, defined
                by you.
            **metadata: Additional information you can store about this user.

        Returns:
            An Atrium member.

        """
        body = atrium.MemberUpdateRequestBody(member={**kwargs})

        res = self.client.members.update_member(member_guid,
                                                user_guid,
                                                body=body)
        return res.member

    def delete_member(self, member_guid: str, user_guid: str):
        """Delete a member.

        Args:
            member_guid: A unique identifier for the member. Defined by MX.
            user_guid: A unique identifier for the user. Defined by MX.

        """
        self.client.members.delete_member(member_guid, user_guid)

    def list_members(self,
                     user_guid: str,
                     page: int = 1,
                     records_per_page: int = 25) -> List[AtriumMember]:
        """List all the members for a user.

        Args:
            user_guid: A unique identifier for the user. Defined by MX.
            page: The page number to start the search.
            records_per_page: The number of records to retrieve with
                each request. Max is 1000.

        Returns:
            A list of an Atrium user's members.

        """
        members = []

        while True:
            res = self.client.members.list_members(
                user_guid, page=page, records_per_page=records_per_page)
            members += res.members

            if res.pagination.current_page == res.pagination.total_pages:
                break

            page += 1

        return members

    def aggregate_member(self, member_guid: str,
                         user_guid: str) -> AtriumMember:
        """Aggregate a member.

        Args:
            member_guid: A unique identifier for the member. Defined by MX.
            user_guid: A unique identifier for the user. Defined by MX.

        Returns:
            An Atrium member.

        """
        res = self.client.members.aggregate_member(member_guid, user_guid)
        return res.member

    def read_connection_status_for_member(self, member_guid: str,
                                          user_guid: str
                                          ) -> AtriumMemberConnectionStatus:
        """Read a member's connection status.

        Args:
            member_guid: A unique identifier for the member. Defined by MX.
            user_guid: A unique identifier for the user. Defined by MX.

        Returns:
            An Atrium member's connection status.

        """
        res = self.client.members.read_member_status(member_guid, user_guid)
        return res.member

    def list_mfa_challenges_for_member(self, member_guid: str,
                                       user_guid: str) -> AtriumChallenge:
        """List all the MFA challenges for a member.

        Args:
            member_guid: A unique identifier for the member. Defined by MX.
            user_guid: A unique identifier for the user. Defined by MX.

        Returns:
            An Atrium member's challenges.

        """
        res = self.client.members.list_member_mfa_challenges(
            member_guid, user_guid)
        return res.challenges

    def list_credentials_for_member(self, member_guid: str, user_guid: str
                                    ) -> List[AtriumCredentialResponse]:
        """List the member's credentials.

        Args:
            member_guid: A unique identifier for the member. Defined by MX.
            user_guid: A unique identifier for the user. Defined by MX.

        Returns:
            A list of an Atrium member's credentials.

        """
        res = self.client.members.list_member_credentials(
            member_guid, user_guid)
        return res.credentials

    def list_accounts_for_member(self,
                                 member_guid: str,
                                 user_guid: str,
                                 page: int = 1,
                                 records_per_page: int = 25
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
                member_guid,
                user_guid,
                page=page,
                records_per_page=records_per_page)
            accounts += res.accounts

            if res.pagination.current_page == res.pagination.total_pages:
                break

            page += 1

        return accounts

    def list_transactions_for_member(self,
                                     member_guid: str,
                                     user_guid: str,
                                     page: int = 1,
                                     records_per_page: int = 25,
                                     **kwargs) -> List[AtriumTransaction]:
        """List all of a member's transactions.

        Args:
            member_guid: A unique identifier for the member. Defined by MX.
            user_guid: A unique identifier for the user. Defined by MX.
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
                **kwargs)
            transactions += res.transactions

            if res.pagination.current_page == res.pagination.total_pages:
                break

            page += 1

        return transactions
