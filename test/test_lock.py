# coding: utf-8

"""
    CERN Unified Storage API

    A unified storage API for all data-storage back-ends.

    OpenAPI spec version: 2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.lock import Lock


class TestLock(unittest.TestCase):
    """ Lock unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLock(self):
        """
        Test Lock
        """
        model = swagger_client.models.lock.Lock()


if __name__ == '__main__':
    unittest.main()
