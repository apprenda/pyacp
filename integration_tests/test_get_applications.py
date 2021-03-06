import unittest
import integrationtestsetttings
import pyacp


class TestGetApplications(unittest.TestCase):
    def setUp(self):
        pass;

    def tearDown(self):
        pass;

    def testGetAtLeastOneApp(self):
        settings = integrationtestsetttings.IntegrationTestSetttings()

        client = pyacp.ApprendaOpsClient(settings.baseurl, settings.adminEmail, settings.adminPassword)
        # set our page size low so we page
        client.apps_page_size = 2

        results = client.get_applications()

        found_one = False

        # enumerate the generator and we'll start firing
        for application in results:
            self.assertIsNotNone(application)
            found_one = True

        self.assertTrue(found_one)

    def testGetAppsByName(self):
        settings = integrationtestsetttings.IntegrationTestSetttings()

        client = pyacp.ApprendaOpsClient(settings.baseurl, settings.adminEmail, settings.adminPassword)
        # set our page size low so we page
        client.apps_page_size = 2

        results = client.get_applications()

        app = None
        for a in results:
            app = a
            break

        self.assertIsNotNone(app)
        self.assertTrue(app.name)

        res = client.get_applications(app.alias)

        self.assertIsNotNone(res)
        self.assertEqual(app.name, res.name)

    def testGetAppsByNameReturns404WhenNotFound(self):
        settings = integrationtestsetttings.IntegrationTestSetttings()

        client = pyacp.ApprendaOpsClient(settings.baseurl, settings.adminEmail, settings.adminPassword)

        bad_alias = "notAThingHereISwear"

        threw = False
        try:
            client.get_applications(bad_alias)
        except KeyError:
            threw = True

        self.assertTrue(threw)
