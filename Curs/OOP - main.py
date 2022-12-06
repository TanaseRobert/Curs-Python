from OOP import ContBancar

cont1 = ContBancar('Robert T', 'RO001')
cont2 = ContBancar('Ianis H', 'RO002')

cont1.activareCont(7777)
cont1.activareCont(1234)
cont1.activareCont(2580)

cont1.interogareSold()
cont2.interogareSold()

cont1.alimentareCont(1000)
cont2.alimentareCont(1200)

cont1.plataCard(800)
cont2.plataCard(900)