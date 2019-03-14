l=input("Podaj ciag!\n")
print(l)
for wart in l:
   pisemnie=('0','1','2','3','4','5','6','7','8','9')
   if wart in pisemnie:
       slownie={0:'Zero',1:'Jeden',2:'Dwa',3:'Trzy',4:'Cztery',5:'Piec',6:'Szesc',7:'Siedem',8:'Osiem',9:'Dziewiec'}
       print(slownie[int(wart)])