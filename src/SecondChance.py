import sys

sys.path.append('src/')
from PageReplacement import PageReplacement

class SecondChance(PageReplacement):
    def __init__(self, size=8000):
        super().__init__(size)
        self.pointer = 0
        self.reference_bit = [0] * size

    def replace_page(self, page):
        while True:
            if self.reference_bit[self.pointer] == 0:
                slot = self.pointer
                self.pointer = (self.pointer + 1) % self.memory_size
                return slot
            self.reference_bit[self.pointer] = 0
            self.pointer = (self.pointer + 1) % self.memory_size

    def access_page(self, page):
        super().access_page(page)
        if self.is_page_in_memory(page):
            self.reference_bit[self.memory.index(page)] = 1
