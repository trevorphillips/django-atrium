import atrium
from atrium.rest import ApiException


class ConnectWidget:

    def __init__(self, client):
        self.client = client

    def get_connect_widget(self, user_guid, **kwargs):
        """
        Get MX connect widget.

        Parameters
        ----------
        user_guid : str
            A unique identifier for the user. Defined by MX.
        is_mobile_webview : bool, optional
            Executes URL updates in place of the JavaScript event messages.
        current_institution_code : str, optional
            Load the widget with desired institution credential view by the
            institutions code.
        current_member_guid : str, optional
            Load to a specific member that contains an error or requires MFA
            from the most recent job.
            Members with no errors will return to search.
            current_member_guid takes precedence over current_institution_code.
        update_credentials : bool, optional
            Used in conjuction with current_member_guid to load into a state
            to update the provided members credentials.

        Raises
        -----
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        body = atrium.ConnectWidgetRequestBody(**kwargs)

        try:
            response = self.client.connect_widget.get_connect_widget(
                user_guid, body
            )
            return response.user
        except ApiException as e:
            print("ApiException")
