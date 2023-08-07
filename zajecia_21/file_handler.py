import json
from abc import abstractmethod, ABC

class FileHandlerInterface(ABC):

    @abstractmethod
    def load_saldo_and_magazyn(self):
        pass

    @abstractmethod
    def save_saldo_and_magazyn_to_file(self):
        pass



class FileHandler(FileHandlerInterface):
    def load_saldo_and_magazyn(self, file):
        with open(file) as opened_file:
            our_data = json.loads(opened_file.read())
            saldo = our_data.get("saldo")
            magazyn = our_data.get("magazyn")
            return saldo, magazyn

    def save_saldo_and_magazyn_to_file(self, file, saldo, magazyn):
        with open(file, mode="w") as opened_file:
            structure_to_be_saved = {
                "saldo": saldo,
                "magazyn": magazyn
            }
            opened_file.write(json.dumps(structure_to_be_saved))

    def load_history(self, file):
        with open(file) as opened_file:
            our_data = opened_file.read().split(",")
            return our_data

    def save_history(self, file, history):
        with open(file, mode="w") as opened_file:
            text = ""
            for history_line in history:
                text += f"{history_line},"
            opened_file.write(text)