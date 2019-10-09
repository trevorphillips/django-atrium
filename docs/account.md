# django_atrium

# django_atrium.account
account file.
## Account
```python
Account(self, client: atrium.api.atrium_client.AtriumClient)
```
Account class.
### read_account
```python
Account.read_account(self, account_guid: str, user_guid: str) -> atrium.models.account.Account
```
Read an account.

Args:
    account_guid: A unique identifier for the account. Defined by MX.
    user_guid: A unique identifier for the user. Defined by MX.

Returns:
    An atrium account.


### list_accounts_for_user
```python
Account.list_accounts_for_user(self, user_guid: str, page: int = 1, records_per_page: int = 25) -> List[atrium.models.account.Account]
```
List all the accounts for a user.

Args:
    user_guid: A unique identifier for the user. Defined by MX.
    page: The page number to start the search.
    records_per_page: The number of records to retrieve with
        each request. Max is 1000.

Returns:
    A list of atrium accounts.


### list_transactions_for_account
```python
Account.list_transactions_for_account(self, account_guid: str, user_guid: str, page: int = 1, records_per_page: int = 25, **kwargs) -> List[atrium.models.transaction.Transaction]
```
List all the transactions for an account.

Args:
    account_guid: A unique identifier for the account. Defined by MX.
    user_guid: A unique identifier for the user. Defined by MX.
    page: The page number to start the search.
    records_per_page: The number of records to retrieve with
        each request. Max is 1000.
    **from_date: A date string that specifies the start date.
    **to_date: A date string that specifies the end date.

Returns:
    A list of an Atrium accounts's transactions.


