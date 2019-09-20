import atrium
from atrium.rest import ApiException


class User:
    """User class."""
    def __init__(self, client):
        self.client = client

    def create_user(self, identifier, **kwargs):
        """Create a user.

        Parameters
        ----------
        identifier : str
            A unique, enforced identifier for the user, defined by you.
        is_disabled : bool, optional
            True if you want the user disabled, false otherwise.
        metadata : str, optional
            Additional information you can store about this user.
            MX recommends using JSON-structured data.

        Returns
        -------
        user : atrium.models.user.User
            An Atrium user.

        Raises
        -----
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        body = atrium.UserCreateRequestBody(user={
            'identifier': identifier,
            **kwargs
        })

        try:
            response = self.client.users.create_user(body)
            return response.user
        except ApiException as e:
            print(e)

    def read_user(self, user_guid):
        """Read a user.

        Parameters
        ----------
        user_guid : str
            A unique identifier for the user. Defined by MX.

        Returns
        -------
        user : atrium.models.user.User
            An Atrium user.

        Raises
        -----
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        try:
            response = self.client.users.read_user(user_guid)
            return response.user
        except ApiException as e:
            print(e)

    def update_user(self, user_guid, **kwargs):
        """Update a user.

        Parameters
        ----------
        user_guid : str
            A unique identifier for the user. Defined by MX.
        identifier : str, optional
            A unique, enforced identifier for the user, defined by you.
        is_disabled : bool, optional
            True if you want the user disabled, false otherwise.
        metadata : str, optional
            Additional information you can store about this user.
            MX recommends using JSON-structured data.

        Returns
        -------
        user : atrium.models.user.User
            An Atrium user.

        Raises
        -----
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        body = atrium.UserCreateRequestBody(user={**kwargs})

        try:
            response = self.client.users.update_user(user_guid, body=body)
            return response.user
        except ApiException as e:
            print(e)

    def delete_user(self, user_guid):
        """Delete a user.

        Parameters
        ----------
        user_guid : str
            A unique identifier for the user. Defined by MX.

        Returns
        -------
            _ : None

        Raises
        -----
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        try:
            self.client.users.delete_user(user_guid)
        except ApiException as e:
            print(e)

    def list_users(self):
        """List all the users.

        Returns
        -------
            _ : None

        Raises
        -----
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        users = []
        page = 1
        records_per_page = 100

        try:
            while True:
                response = self.client.users.list_users(
                    page=page, records_per_page=records_per_page)
                users += response.users

                if response.pagination.current_page <= response.pagination.total_pages:
                    break

                page += 1

            return users
        except ApiException as e:
            print(e)
