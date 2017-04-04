import unittest
import pyacp
import integrationtestsetttings


class TestGetAddOns(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_addons_returns(self):
        settings = integrationtestsetttings.IntegrationTestSetttings()

        client = pyacp.ApprendaOpsClient(settings.baseurl, settings.adminEmail, settings.adminPassword)

        results = client.get_add_ons()

        found_one = False

        # enumerate the generator and we'll start firing
        for add_on in results:
            self.assertIsNotNone(add_on)
            found_one = True

        self.assertTrue(found_one, "No add on was found - ensure your platform has at least one add on installed to run this test")

    def test_get_add_on_by_alias(self):
        settings = integrationtestsetttings.IntegrationTestSetttings()

        client = pyacp.ApprendaOpsClient(settings.baseurl, settings.adminEmail, settings.adminPassword)

        results = client.get_add_ons()

        add_on = None
        for ret in results:
            add_on = ret
            break

        self.assertIsNotNone(add_on, "No add on was found - ensure your platform has at least one add on installed to run this test")

        single_res = client.get_add_ons(add_on.alias)

        self.assertIsNotNone(single_res)
        self.assertEqual(add_on.alias, single_res.alias)