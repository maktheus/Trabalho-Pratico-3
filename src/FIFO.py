import sys

sys.path.append('src/')
from PageReplacement import PageReplacement

class FIFO(PageReplacement):
    def __init__(self, size=8000):
        super().__init__(size)
        self.pointer = 0

    def replace_page(self, page):
        slot = self.pointer
        self.pointer = (self.pointer + 1) % self.memory_size
        return slot
