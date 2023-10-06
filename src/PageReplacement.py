class PageReplacement:
    def __init__(self, size=8000):
        self.memory_size = size
        self.memory = [-1] * size
        self.page_faults = 0

    def is_page_in_memory(self, page):
        return page in self.memory

    def get_free_slot(self):
        for index, page in enumerate(self.memory):
            if page == -1:
                return index
        return None

    def replace_page(self, page):
        raise NotImplementedError

    def access_page(self, page):
        if not self.is_page_in_memory(page):
            self.page_faults += 1
            slot = self.get_free_slot()
            if slot is None:
                slot = self.replace_page(page)
            self.memory[slot] = page

    def get_page_faults(self):
        return self.page_faults
