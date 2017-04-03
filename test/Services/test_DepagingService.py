import unittest
import pyacp

from pyacp import models
from pyacp import services

class TestDepagingService(unittest.TestCase):
    """ AddOn unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDepagingService(self):
        under_test = services.DepagingService(self.fakeStartGet, self.fakeStartNext)

        #act
        res = under_test.next()

        #assert
        self.assertIsNotNone(res)

        max = 0
        for item in res:
            if(item > max):
                max = item

        self.assertEqual(179, max)

    def fakeStartGet(self):
        return self.makePage(0)

    def fakeStartNext(self, url):
        if url is None:
            return None

        pageString = url.split("page=")
        parsed = int(pageString[-1])

        if parsed < 9:
            return self.makePage(parsed)
        else:
            fakePaging = models.PagedResourceBaseRegistrySetting()
            fakePaging.items = range(91, 100)
            fakePaging.page_size = 10
            fakePaging.next_page = None
            return fakePaging

    def makePage(self, page):
        fakePaging = models.PagedResourceBaseRegistrySetting()
        fakePaging.items = range(page * 10, (page + 10) * 10)
        fakePaging.page_size = 10
        fakePaging.next_page = models.ApprendaRestAPICommonResourcesResourceBase("http://test.com/endpoint?pageSize=10&page=" + str((page + 1)))
        return fakePaging


if __name__ == '__main__':
    unittest.main()