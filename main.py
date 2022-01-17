teksts = input("Ievadiet cipari virkne: ") 

def CountNumbers(teksts):
  summa = 0
  for simbols in teksts:
   summa = summa + int(simbols)
  print(summa)
  return summa
CountNumbers(teksts) 