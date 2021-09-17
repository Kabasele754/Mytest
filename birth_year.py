
birth_year : int = int(input("Bonjour vous pouvez donner votre annee de naissance : "))

age : int = 2021 - birth_year

if age > 18:
    print("Merci pour votre age tu es Mageur avec ", age, "ans")

elif age < 18:
    print("Merci pour votre age tu es Mineur avec ", age, "ans")
    
else:
   print("Merci pour votre age tu es Adolescent avec ", age, "ans")
