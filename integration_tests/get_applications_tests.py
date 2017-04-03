import unittest
import integrationtestsetttings
import pyacp

class test_get_applications(unittest.TestCase):
    def setUp(self):
        pass;

    def tearDown(self):
        pass;



    def testGetAtLeastOneApp(self):
        settings = integrationtestsetttings.IntegrationTestSetttings()

        client = pyacp.ApprendaOpsClient(settings.baseurl, settings.adminEmail, settings.adminPassword)
        client.apps_page_size = 2

        results = client.getApplications()

        foundOne = False

        for application in results:
            foundOne = True

        self.assertTrue(foundOne)