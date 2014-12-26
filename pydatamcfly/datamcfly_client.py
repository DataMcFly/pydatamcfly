# -*- coding: utf-8 *-*
from pydatamcfly import database
from datamcflyclient import DataMcFlyClient


class DataMcFlyClient(object):
    """Instance class with the API key located at
    https://app.datamcfly.com/

    Example usage:

    .. code-block:: python

       >>> from pydatamcfly import DataMcFlyClient
       >>> DataMcFlyClient("DataMcFlyAPIKey")
       DataMcFlyClient('DataMcFlyAPIKey', 'v1')

    .. note::
       The ``version`` parameter is optional, because it is planed for using in
       future versions of REST API.

    When your connection needs to set a proxy, you can to set an `str` with the
    Proxy url to ``proxy_url`` parameter. If you don't set a ``proxy_url``,
    then :class:`datamcflyclient.client.DataMcFlyClient` gets system proxy
    settings.

    .. code-block:: python

       >>> from pydatamcfly import DataMcFlyClient
       >>> DataMcFlyClient("DataMcFlyAPIKey", proxy_url="https://127.0.0.1:8000")
       DataMcFlyClient('DataMcFlyAPIKey', 'v1')
    """

    def __init__(self, api_key, version="v1", proxy_url=None):
        self.api_key = api_key
        self.version = version
        self.__request = DataMcFlyClient(api_key, version, proxy_url)

    @property
    def request(self):
        """An instance of :class:`datamcflyclient.client.DataMcFlyClient` used
        for internal calls to DataMcFly REST API via :mod:`datamcflyclient`.
        """
        return self.__request

    def __eq__(self, other):
        if isinstance(other, DataMcFlyClient):
            us = (self.api_key, self.version)
            them = (other.api_key, other.version)
            return us == them
        return NotImplemented

    def __repr__(self):
        return "DataMcFlyClient(%r, %r)" % (self.api_key, self.version)

    def __getattr__(self, name):
        """Get a database using a attribute-style access.

        Example usage:

        .. code-block:: python

           >>> from pydatamcfly import DataMcFlyClient
           >>> con = DataMcFlyClient("DataMcFlyAPIKey")
           >>> con.database
           Database(DataMcFlyClient('DataMcFlyAPIKey', 'v1'), 'database')
        """
        return database.Database(self, name)

    def __getitem__(self, name):
        """Get a database using a dictionary-style access.

        Example usage:

        .. code-block:: python

           >>> from pydatamcfly import DataMcFlyClient
           >>> con = DataMcFlyClient("DataMcFlyAPIKey")
           >>> db = con["database"]
           Database(DataMcFlyClient('DataMcFlyAPIKey', 'v1'), 'database')
        """
        return self.__getattr__(name)

    def database_names(self):
        """Returns a list with your database names.

        Example usage:

        .. code-block:: python

           >>> from pydatamcfly import DataMcFlyClient
           >>> con = DataMcFlyClient("DataMcFlyAPIKey")
           >>> con.database_names()
           [u'database', u'otherdatabase']
        """
        return self.request.list_databases()
