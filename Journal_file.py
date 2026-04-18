class Journal:
    def __init__(self):
        self._journal = {}



    def add_student(self, name, mark: list):
        self._journal[name] = mark


    def update_mark(self, name, mark: list):
        if name in self._journal:
            self._journal[name] = mark



    def get_mark(self, name):
        if name in self._journal:
            return self._journal[name]


    def get_all(self):
        for key, value in self._journal.items():
            print(f"{key}: {' '.join(str(i) for i in value)}")






