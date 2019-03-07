slownik = {'Damian':'728751517', 'Jarek':'679637970', 'Piotr':'661903621'}
print(slownik['Damian'])
slownik['Jarek'] = '666123789'
slownik['Rafal'] = '598142745'
del slownik['Piotr']
print(slownik)
slownik.clear()
print(slownik)
