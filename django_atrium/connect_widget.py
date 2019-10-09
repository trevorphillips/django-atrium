"""connect widget file."""
import atrium
from atrium.models.connect_widget import ConnectWidget as AtriumConnectWidget


class ConnectWidget:
    """Connect Widget class."""
    def __init__(self, client: atrium.AtriumClient):
        """Init for ConnectWidget."""
        self.client = client

    def get_connect_widget(self, user_guid: str,
                           **kwargs) -> AtriumConnectWidget:
        """Get Atrium connect widget.

        Args:
            user_guid: A unique identifier for the user. Defined by MX.
            **is_mobile_webview: A boolean to indicate if you'd like to
                execute URL updates in place of the JavaScript event messages.
            **current_institution_code: A string to load the widget with
                desired institution credential view by the institutions code.
            **current_member_guid: Load to a specific member that contains an
                error or requires MFA from the most recent job. Members with
                no errors will return to search. `current_member_guid` takes
                precedence over `current_institution_code`.
            **update_credentials: A boolean to be used in conjunction with
                current_member_guid to load into a state to update the
                provided members credentials.

        Returns:
            An Atrium user's connect widget.

        """
        body = atrium.ConnectWidgetRequestBody(**kwargs)

        res = self.client.connect_widget.get_connect_widget(user_guid, body)
        return res.user
