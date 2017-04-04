import unittest
import pyacp
import integrationtestsetttings

class TestGetCustomProperties(unittest.TestCase):
    def setUp(self):
        pass;

    def tearDown(self):
        pass;

    def getPagedRetrievesAtLeastOneCustomProperty(self):
        settings = integrationtestsetttings.IntegrationTestSetttings()

        client = pyacp.ApprendaOpsClient(settings.baseurl, settings.adminEmail, settings.adminPassword)