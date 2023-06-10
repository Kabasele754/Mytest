

class ClasseA:
    def __init__(self):
        self.classe_b = None

class ClasseB:
    def __init__(self):
        self.b = "Je suis b"

# Création des objets
a = ClasseA()
b1 = ClasseB()
b2 = ClasseB()

# Association simple
b= a.classe_b = b1
a.classe_b = b2

print(b.b)
