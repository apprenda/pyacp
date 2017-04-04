import unittest
import pyacp
import integrationtestsetttings


class TestGetCustomProperties(unittest.TestCase):
    def setUp(self):
        pass;

    def tearDown(self):
        pass;

    def test_paged_retrieves_at_least_one_custom_property(self):
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

    def test_get_custom_property_by_name(self):
        settings = integrationtestsetttings.IntegrationTestSetttings()

        client = pyacp.ApprendaOpsClient(settings.baseurl, settings.adminEmail, settings.adminPassword)

        #set paging low so we test it
        client.custom_properties_page_size = 1

        results = client.get_custom_properties()

        self.assertIsNotNone(results)

        my_prop = None
        for prop in results:
            self.assertIsNotNone(prop)
            my_prop = prop

        single_res = client.get_custom_properties(my_prop.name)

        self.assertIsNotNone(single_res)
        self.assertEqual(my_prop.name, single_res.name)

    def test_get_custom_property_by_name_returns_key_error_for_unfound(self):
        settings = integrationtestsetttings.IntegrationTestSetttings()

        client = pyacp.ApprendaOpsClient(settings.baseurl, settings.adminEmail, settings.adminPassword)

        threw = False
        try:
            client.get_custom_properties("thisisneitheralovesongoracustomprop")
        except KeyError:
            threw = True

        self.assertTrue(threw)