class ContBancar:

    # constructor
    def __init__(self, titularCont, iban):

        # atribute / proprietati / fields
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.pin = 2580
        self.numar_incercari = 0

    def salut(self):
        print(f'Buna {self.titularCont}')

    def interogareSold(self):
        print(f'Titular {self.titularCont}')
        print(f'IBAN {self.iban}')
        print(f'Sold {self.sold}')
        print(f'Activ {self.activ}')
        print(f'Numar de incercari {self.numar_incercari}')
        print('------------------------------------------')

    def activareCont(self, pin_utilizator):
        self.salut()
        if pin_utilizator == self.pin:
            print("Card activat")
            self.activ = True
        else:
            print("Pin gresit")
            self.numar_incercari += 1

    def alimentareCont(self, suma):
        self.salut()
        self.sold += suma
        print(f'Ati alimentat suma {suma}')
        print(f'Acum aveti suma de {self.sold}')

    def plataCard(self, suma):

        # variable scope (suma din plata e diferita de cea din alimentare)
        self.salut()
        if suma <= self.sold:
            self.sold -= suma
            print(f'Ati cheltuit suma {suma}')
            print(f'Acum aveti suma de {self.sold}')
        else:
            print("Fonduri insuficiente")