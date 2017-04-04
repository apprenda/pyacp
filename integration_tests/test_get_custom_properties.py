import unittest
import pyacp
import integrationtestsetttings


class TestGetCustomProperties(unittest.TestCase):
    def setUp(self):
        pass;

    def tearDown(self):
        pass;

    def testPagedRetrievesAtLeastOneCustomProperty(self):
        settings = integrationtestsetttings.IntegrationTestSetttings()

        client = pyacp.ApprendaOpsClient(settings.baseurl, settings.adminEmail, settings.adminPassword)

        #set paging low so we test it
        client.custom_properties_page_size = 1

        results = client.get_custom_properties()

        self.assertIsNotNone(results)

        found_one = False
        for prop in results:
            self.assertIsNotNone(prop)
            found_one = True

        self.assertTrue(found_one)