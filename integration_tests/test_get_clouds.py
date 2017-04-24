import unittest
import pyacp
import integrationtestsetttings

class TestGetClouds(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_clouds_returns(self):
        settings = integrationtestsetttings.IntegrationTestSetttings()

        client = pyacp.ApprendaOpsClient(settings.baseurl, settings.adminEmail, settings.adminPassword)

        results = client.get_public_clouds()

        found_one = False

        # enumerate the generator and we'll start firing
        for cloud in results:
            self.assertIsNotNone(cloud)
            found_one = True

        self.assertTrue(found_one)

    def test_get_cloud_by_id(self):
        settings = integrationtestsetttings.IntegrationTestSetttings()

        client = pyacp.ApprendaOpsClient(settings.baseurl, settings.adminEmail, settings.adminPassword)

        results = client.get_public_clouds()

        cloud = None
        for ret in results:
            cloud = ret
            break

        self.assertIsNotNone(cloud, "No cloud was found - ensure your platform has at least one add on installed to run this test")

        single_res = client.get_public_clouds(cloud.id)

        self.assertIsNotNone(single_res)
        self.assertEqual(cloud.id, single_res.id)