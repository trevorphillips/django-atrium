import atrium
from atrium.rest import ApiException


class Member:
    def __init__(self, client):
        self.client = client

    def read_member(self, member_guid, user_guid):
        """Read a member.

        Parameters
        ----------
        member_guid : str
            A unique identifier for the member. Defined by MX.
        user_guid : str
            A unique identifier for the user. Defined by MX.

        Returns
        -------
            member : atrium.models.member.Member
                An Atrium member.

        Raises
        ------
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        try:
            response = self.client.members.read_member(member_guid, user_guid)
            return response.member
        except ApiException as e:
            print(e)

    def update_member(self, member_guid, user_guid, **kwargs):
        """Update a member.

        Parameters
        ----------
        member_guid : str
            A unique identifier for the member. Defined by MX.
        user_guid : str
            A unique identifier for the user. Defined by MX.
        identifier : str, optional
            A unique, enforced identifier for the user, defined by you.
        metadata : str, optional
            Additional information you can store about this user.
            MX recommends using JSON-structured data.

        Returns
        -------
            member : atrium.models.member.Member
                An Atrium member.

        Raises
        ------
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        body = atrium.MemberUpdateRequestBody(member={**kwargs})

        try:
            response = self.client.members.update_member(member_guid,
                                                         user_guid,
                                                         body=body)
            return response.member
        except ApiException as e:
            print(e)

    def delete_member(self, member_guid, user_guid):
        """Delete a member.

        Parameters
        ----------
        member_guid : str
            A unique identifier for the member. Defined by MX.
        user_guid : str
            A unique identifier for the user. Defined by MX.

        Returns
        -------
            _ : None

        Raises
        ------
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        try:
            self.client.members.delete_member(member_guid, user_guid)
        except ApiException as e:
            print(e)

    def list_members(self, user_guid):
        """List all the members for a user.

        Parameters
        ----------
        user_guid : str
            A unique identifier for the user. Defined by MX.

        Returns
        -------
            members : list
                A list of an Atrium user's members.

        Raises
        ------
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        members = []
        page = 1
        records_per_page = 100

        try:
            while True:
                response = self.client.members.list_members(
                    user_guid, page=page, records_per_page=records_per_page)
                members += response.members

                if response.pagination.current_page <= response.pagination.total_pages:
                    break

                page += 1

            return members
        except ApiException as e:
            print(e)

    def aggregate_member(self, member_guid, user_guid):
        """Aggregate a member.

        Parameters
        ----------
        member_guid : str
            A unique identifier for the member. Defined by MX.
        user_guid : str
            A unique identifier for the user. Defined by MX.

        Returns
        -------
            member : atrium.models.member.Member
                An Atrium member.

        Raises
        ------
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        try:
            response = self.client.members.aggregate_member(
                member_guid, user_guid)
            return response.member
        except ApiException as e:
            print(e)

    def read_member_connection_status(self, member_guid, user_guid):
        """Read a member's connection status.

        Parameters
        ----------
        member_guid : str
            A unique identifier for the member. Defined by MX.
        user_guid : str
            A unique identifier for the user. Defined by MX.

        Returns
        -------
            member_status : atrium.models.member_connection_status.MemberConnectionStatus
                An Atrium member's connection status.

        Raises
        ------
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        try:
            response = self.client.members.read_member_status(
                member_guid, user_guid)
            return response.member
        except ApiException as e:
            print(e)

    def list_member_mfa_challenges(self, member_guid, user_guid):
        """List all the MFA challenges for a member.

        Parameters
        ----------
        member_guid : str
            A unique identifier for the member. Defined by MX.
        user_guid : str
            A unique identifier for the user. Defined by MX.

        Returns
        -------
            challenges : list
                A list of an Atrium member's challenges.

        Raises
        ------
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        try:
            response = self.client.members.list_member_mfa_challenges(
                member_guid, user_guid)
            return response.challenges
        except ApiException as e:
            print(e)

    def list_member_credentials(self, member_guid, user_guid):
        """List the member's credentials.

        Parameters
        ----------
        member_guid : str
            A unique identifier for the member. Defined by MX.
        user_guid : str
            A unique identifier for the user. Defined by MX.

        Returns
        -------
        credentials : list
            A list of an Atrium member's credentials.

        Raises
        ------
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        try:
            response = self.client.members.list_member_credentials(
                member_guid, user_guid)
            return response.credentials
        except ApiException as e:
            print(e)

    def list_member_accounts(self, member_guid, user_guid):
        """List a member's accounts.

        Parameters
        ----------
        member_guid : str
            A unique identifier for the member. Defined by MX.
        user_guid : str
            A unique identifier for the user. Defined by MX.

        Returns
        -------
        accounts : list
            A list of an Atrium member's accounts.

        Raises
        ------
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        accounts = []
        page = 1
        records_per_page = 100

        try:
            while True:
                response = self.client.members.list_member_accounts(
                    member_guid,
                    user_guid,
                    page=page,
                    records_per_page=records_per_page)
                accounts += response.accounts

                if response.pagination.current_page <= response.pagination.total_pages:
                    break

                page += 1

            return accounts
        except ApiException as e:
            print(e)

    def list_member_transactions(self, member_guid, user_guid, **kwargs):
        """List all of a member's transactions.

        Parameters
        ----------
        member_guid : str
            A unique identifier for the member. Defined by MX.
        user_guid : str
            A unique identifier for the user. Defined by MX.
        from_date : str, optional
            Filter transactions from this date.
        to_date : str, optional
            Filter transactions to this date.

        Returns
        -------
        transactions : list
            A list of an Atrium member's transaction.

        Raises
        ------
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        transactions = []
        page = 1
        records_per_page = 100

        try:
            while True:
                response = self.client.members.list_member_transactions(
                    member_guid,
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
