svar = int(input("skriv ett tal"))

while svar != 42:
  if svar > 42:
    print("för stort tal testa igen")
  elif svar < 42:
    print("för litet testa igen")
    
  svar = int(input("skriv ett tal"))

print("rätt svar")

      