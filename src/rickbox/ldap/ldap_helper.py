"""
LDAP wrapper for generic LDAP servers

Usage:

The constructor for the ldap helper takes in a host. If a host is not provided
the helper will use the values stored in the config file.
"""

from ldap3 import Server, Connection
from ldap3.core.exceptions import LDAPException, LDAPInvalidCredentialsResult

from app_config import LDAP_HOST


class LdapHelper:

    def __init__(self, host=LDAP_HOST):
        """
        Create a connection to the ldap server at the given host

        :param host: address of the ldap server to connect to
        """
        self._server = Server(host=host)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def authenticate(self, username, password):
        """
        Authenticate a username and password against the ldap server

        :param username: username to authenticate with
        :param password: password to authenticate with

        :return status code and message associated with authentication results
        """
        user_query = 'uid={username},ou=People,ou=fcs,o=unb'
        try:
            connection = Connection(
                self._server,
                user=user_query.format(username=username),
                password=password,
                raise_exceptions=True
            )
            connection.open()
            connection.start_tls()
            connection.bind()
            return 200, 'successfully authenticated user'
        except LDAPInvalidCredentialsResult:
            return 401, 'invalid username or password provided'
        except LDAPException:
            return 500, 'an unexpected error occurred'
        finally:
            connection.unbind()


if __name__ == '__main__':
    with LdapHelper() as ldap:
        u = input('Please enter your username: ')
        p = input('Please enter your password: ')
        print('starting authentication')
        print(ldap.authenticate(u, p))
        print('finished authentication')
