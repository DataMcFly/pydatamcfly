# -*- coding: utf-8 *-*
"""PyMongo_-flavored package for accessing to Data McFly apps via
`datamcflyClient`.

.. _PyMongo: http://api.datamcfly.com/"""


ASCENDING = 1
"""Ascending sort order."""
DESCENDING = -1
"""Descending sort order."""


OFF = 0
"""No database profiling."""
SLOW_ONLY = 1
"""Only profile slow operations."""
ALL = 2
"""Profile all operations."""


from pydatamcfly.connection import Connection
from pydatamcfly.datamcfly_client import DataMcFlyClient
