import atrium
from atrium.rest import ApiException


class Institution:

    def __init__(self, client):
        self.client = client

    def read_institution(self, institution_code):
        """
        Read an institution.

        Parameters
        ----------
        institution_code : str
            A unique identifier for each institution, defined by MX.

        Raises
        -----
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        try:
            response = self.client.institutions.read_institution(
                institution_code
            )
            return response.institution
        except ApiException as e:
            print("ApiException")

    def list_institutions(self, **kwargs):
        """
        List all the institutions.

        Parameters
        ----------
        name : str, optional
            Only institutions whose name contains the appended string will
            be returned.
        supports_account_identification : bool, optional
            Only institutions which support identity will be returned.
        supports_account_statement : bool, optional
            Only institutions which offer access to account statements will
            be returned.
        supports_account_verification : bool, optional
            Only institutions which support account verification will
            be returned.
        supports_transaction_history : bool, optional
            Only institutions which offer an extended transaction history will
            be returned.

        Raises
        -----
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        try:
            response = self.client.institutions.list_institutions(**kwargs)
            return response.institutions
        except ApiException as e:
            print("ApiException")

    def read_institution_credentials(self, institution_code):
        """
        Read an institution's credentials.

        Parameters
        ----------
        institution_code : str
            A unique identifier for each institution, defined by MX.

        Raises
        -----
        ApiException
            If there is an error when calling the MX Atrium API.
        """

        try:
            response = self.client.institutions.read_institution_credentials(
                institution_code
            )
            return response.credentials
        except ApiException as e:
            print("ApiException")
