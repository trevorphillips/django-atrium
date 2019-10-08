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
            **current_member_guid: A string that is a unique identifier for
                the member. Defined by MX.
            **disable_institution_search: A boolean to indicate if the
                institution search feature will be disabled and end users will
                not be able to navigate to it.
            **update_credentials: A boolean to be used in conjunction with
                current_member_guid to load into a state to update the
                provided members credentials.

        Returns:
            An Atrium user's connect widget.

        """
        body = atrium.ConnectWidgetRequestBody(**kwargs)

        res = self.client.connect_widget.get_connect_widget(user_guid, body)
        return res.user
