"""institution file."""
from typing import List

import atrium
from atrium.models.credential_response import \
    CredentialResponse as AtriumCredentialResponse
from atrium.models.institution import Institution as AtriumInstitution


class Institution:
    """Institution class."""
    def __init__(self, client: atrium.AtriumClient):
        """Init for Institution."""
        self.client = client

    def read_institution(self, institution_code: str) -> AtriumInstitution:
        """Read an institution.

        Args:
            institution_code: A unique identifier for each institution,
                defined by MX.

        Returns:
            An Atrium institution.

        """
        res = self.client.institutions.read_institution(institution_code)
        return res.institution

    def list_institutions(self, **kwargs) -> List[AtriumInstitution]:
        """List all the institutions.

        Args:
            **name: Only institutions whose name contains the appended string
                will be returned.
            **supports_account_identification: A boolean to only show
                institutions which support identity will be returned.
            **supports_account_statement: A boolean to only show institutions
                which offer access to account statements will be returned.
            supports_account_verification: A boolean to only show institutions
                which support account verification will be returned.
            supports_transaction_history: A boolean to only show institutions
                which offer an extended transaction history will be returned.

        Returns:
            A list of Atrium institutions.

        """
        res = self.client.institutions.list_institutions(**kwargs)
        return res.institutions

    def read_credentials_for_institution(self, institution_code: str
                                         ) -> List[AtriumCredentialResponse]:
        """Read an institution's credentials.

        Args:
            institution_code: A unique identifier for each institution,
                defined by MX.

        Returns:
            A list of an Atrium Institutions's credentials.

        """
        res = self.client.institutions.read_institution_credentials(
            institution_code)
        return res.credentials
