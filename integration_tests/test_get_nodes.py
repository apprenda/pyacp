import unittest
import pyacp
import integrationtestsetttings


class TestGetNodes(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_node_by_name(self):
        settings = integrationtestsetttings.IntegrationTestSetttings()

        client = pyacp.ApprendaOpsClient(settings.baseurl, settings.adminEmail, settings.adminPassword)

        res = client.get_nodes(settings.testNodeName)

        self.assertIsNotNone(res)

        self.assertEqual(settings.testNodeName, res.name)

    def test_get_all_nodes_returns_at_least_one(self):
        settings = integrationtestsetttings.IntegrationTestSetttings()

        client = pyacp.ApprendaOpsClient(settings.baseurl, settings.adminEmail, settings.adminPassword)

        res = client.get_nodes()

        self.assertIsNotNone(res)

        found_one = False

        for node in res:
            self.assertIsNotNone(node)
            found_one = True

        self.assertTrue(found_one)

    def test_get_node_by_name_throws_with_unfound_node(self):
        settings = integrationtestsetttings.IntegrationTestSetttings()

        client = pyacp.ApprendaOpsClient(settings.baseurl, settings.adminEmail, settings.adminPassword)

        threw = False
        try:
            client.get_nodes("iamnotanodeimbadtestdata")
        except pyacp.ApiException:
            threw = True

        self.assertTrue(threw)