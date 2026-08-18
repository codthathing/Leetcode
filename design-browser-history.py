class BrowserHistory(object):

    class NewPageNode():
        def __init__(self, url):
            self.back = None
            self.url = url
            self.forward = None

    def __init__(self, homepage):
        self.currentPage = self.NewPageNode(homepage)
        self.pageNumber = 1
        self.totalPages = 1

    def visit(self, url):
        newPage = self.NewPageNode(url)

        self.currentPage.forward = newPage
        newPage.back = self.currentPage
        self.currentPage = newPage

        self.pageNumber += 1
        self.totalPages = self.pageNumber
        

    def back(self, steps):
        if steps >= self.pageNumber:
            self.pageNumber = 1
            while self.currentPage.back:
                self.currentPage = self.currentPage.back
        else:
            self.pageNumber -= steps
            for i in range(steps):
                self.currentPage = self.currentPage.back
            
        return self.currentPage.url
            
        

    def forward(self, steps):
        if steps >= self.totalPages - self.pageNumber:
            self.pageNumber = self.totalPages
            while self.currentPage.forward:
                self.currentPage = self.currentPage.forward
        else:
            self.pageNumber += steps
            for i in range(steps):
                self.currentPage = self.currentPage.forward
            
        return self.currentPage.url