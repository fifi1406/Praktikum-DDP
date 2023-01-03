'''
    * Function
    * Function 
'''

def hello():
    print("Hello,World")

hello()
hello()
hello()
hello()

# Function dengan parameter

def sayHello(name):
    print(f"Hello, nama saya {name}")

sayHello("Budi")
sayHello("Joko")

def pertambahan(bilanganPertama, bilanganKedua):
    total = bilanganPertama + bilanganKedua
    print(total)

pertambahan(10, 5)

'''
    Challenge
'''

# Buat fungsi yang bisa membuat perkalian
# Buat fungsi yang bisa membuat pembagian

def perkalian(bilanganPertama, bilanganKedua):
    total = bilanganPertama * bilanganKedua
    print(total)

def pembagian(bilanganPertama, bilanganKedua):
    total = bilanganPertama / bilanganKedua
    print(total)

perkalian(10, 5)
pembagian(10, 2)
