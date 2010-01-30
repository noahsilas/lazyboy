# -*- coding: utf-8 -*-
#
# Author: Noah Silas <noah@mahalo.com>
#

""" Simple Cassandra Query Operations """

from cassandra import ttypes as cas_types

from lazyboy.connection import get_pool


def get_count(key, consistency=None):
    consistency = consistency or cas_types.ConsistencyLevel.ONE
    return get_pool(key.keyspace).get_count(
        key.keyspace, key.key, key.get_path(), consistency
    )