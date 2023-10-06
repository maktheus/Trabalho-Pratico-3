import sys

sys.path.append('src/')
from PageReplacement import PageReplacement

class LRU(PageReplacement):
    def __init__(self, size=8000):
        super().__init__(size)
        self.recent_access = []

    def replace_page(self, page):
        least_recently_used = self.recent_access.pop(0)
        slot = self.memory.index(least_recently_used)
        return slot

    def access_page(self, page):
        super().access_page(page)
        if page in self.recent_access:
            self.recent_access.remove(page)
        self.recent_access.append(page)
