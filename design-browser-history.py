class BrowserHistory:

    class NewPageNode:
        def __init__(self, url: str) -> None:
            self.back: BrowserHistory.NewPageNode | None = None
            self.url: str = url
            self.forward: BrowserHistory.NewPageNode | None = None

    def __init__(self, homepage: str) -> None:
        self.currentPage: BrowserHistory.NewPageNode = self.NewPageNode(homepage)
        self.pageNumber: int = 1
        self.totalPages: int = 1

    def visit(self, url: str) -> None:
        newPage = self.NewPageNode(url)

        if self.currentPage:
            self.currentPage.forward = newPage
            newPage.back = self.currentPage
            self.currentPage = newPage

        self.pageNumber += 1
        self.totalPages = self.pageNumber
        

    def back(self, steps: int) -> str:
        if steps >= self.pageNumber:
            self.pageNumber = 1
            while self.currentPage.back:
                self.currentPage = self.currentPage.back
        else:
            self.pageNumber -= steps
            for _ in range(steps):
                if self.currentPage.back:
                    self.currentPage = self.currentPage.back
            
        return self.currentPage.url
            
        

    def forward(self, steps: int) -> str:
        if steps >= self.totalPages - self.pageNumber:
            self.pageNumber = self.totalPages
            while self.currentPage.forward:
                self.currentPage = self.currentPage.forward
        else:
            self.pageNumber += steps
            for _ in range(steps):
                if self.currentPage.forward:
                    self.currentPage = self.currentPage.forward
            
        return self.currentPage.url