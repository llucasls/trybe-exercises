class MainMemory:
    def __init__(self):
        self.clean()

    def load(self, value):
        self.loaded_memory.append(value)

    def get(self, index):
        try:
            value = self.loaded_memory[index]
        except IndexError:
            value = 0
        return value

    def clean(self):
        self.loaded_memory = []
