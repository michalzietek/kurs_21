class KontoBankowe:
    def __init__(self, numer_konta, saldo):
        self.__saldo  = saldo
        self.__numer_konta = numer_konta
        self.__dowod_osobisty = None # pobierzemy dane z bazy ale nie udostepniamy do dalszej analizy

    def _get_saldo(self):
        return self.__saldo

    def get_saldo(self):
        self._get_saldo()

    def set_saldo(self, saldo):
        if self.__saldo < 0:
            print("Nie mozesz zmienic salda bo masz ujemne")
        self.__saldo = saldo



konto_michala = KontoBankowe(numer_konta="123456", saldo=1000)
print(konto_michala.get_saldo())