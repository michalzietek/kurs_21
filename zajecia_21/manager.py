from zajecia_21.file_handler import  FileHandler


class Manager(FileHandler):

    def __init__(self, history_file, magazyn_and_saldo_file):
        self.history_file = history_file
        self.magazyn_and_saldo_file = magazyn_and_saldo_file
        print("zainicjalizowalem obiekt")
        self.history = self.load_history(history_file)
        self.saldo, self.magazyn = self.load_saldo_and_magazyn(magazyn_and_saldo_file)
        self.actions = {}

    def assign(self, name):
        def wrapper(function):
            self.actions[name] = function
        return wrapper

    def execute(self, name):
        if not name in self.actions:
            print("Niestety nie ma takiej akcji")
        else:
            self.actions[name](self)
