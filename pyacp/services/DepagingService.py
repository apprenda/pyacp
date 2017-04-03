class DepagingService(object):
    def __init__(self, getStartFunction, getNextPageFunction):
        self.getStartFunction = getStartFunction
        self.getNextPageFunction = getNextPageFunction

        self.currentPage = None

    def __next(self):
            return self.next()

    def next(self):
        if(self.currentPage is None):
            self.currentPage = self.getStartFunction()

        while self.currentPage is not None and (len(self.currentPage.items) > 0 or self.currentPage.next_page is not None):
            for item in self.currentPage.items:
                yield item

            if self.currentPage.next_page is not None \
                    and self.currentPage.next_page.href is not None \
                    and len(self.currentPage.next_page.href) > 0:
                self.currentPage = self.getNextPageFunction(self.currentPage.next_page.href)
            else:
                break
