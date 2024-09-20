print("Act 9 clase humano")
print("Angel perez Barron 22308051281086")
# zon de class

class Humano1086:
    # zona de atributos dentro de la clase
    edad=0
    genero=" "
    color=" "
    color_pelo=" "
    nacionalidad =" "
    idioma=" "
    # zona de funciones dentro de la clase

    def correr1086(self,n):
        print(f" {n} esta corriendo ufff...")

    def comer1086(self,n):
        print(f" {n} esta comiendo ñami ñami")

    def escuchar1086(self,n):
        print(f" {n} esta escuchando 'fall into you <3' ")

    def cocina1086(self,n):
        print(f" {n} esta preparando una rica comida")
    
    def ejercita1086(self,n):
        print(f" {n} se esta ejercitando mucho uf ufff")

    def descanza1086(self,n):
        print(f" {n} descanza como si chambeara")
# zona de creacion de objetos

Angel=Humano1086()
Sage=Humano1086()


# zona de usando objetos
print("--------------- Resultado para Angel ---------------------")

Angel.edad=17
Angel.genero="hombre"
Angel.color="moreno"
Angel.color_pelo= "negro"
Angel.nacionalidad="mexicano"
Angel.idioma= "español"

print("Atributos\n")
print(f" edad: {Angel.edad}")
print(f" Genero: {Angel.genero}")
print(f" Color de piel: {Angel.color}")
print(f" Color de pelo: {Angel.color_pelo}")
print(f" nacionalidad: {Angel.nacionalidad}")
print(f" idioma natal: {Angel.idioma}")
print("\n Funciones \n")
Angel.correr1086("Angel")
Angel.comer1086("Angel")
Angel.escuchar1086("Angel")
Angel.cocina1086("Angel")
Angel.ejercita1086("Angel")
Angel.descanza1086("Angel")

print("\n -----------------Resultados para Sage --------------")

Sage.edad=21
Sage.genero="Mujer"
Sage.color="Blanca"
Sage.color_pelo= "negro"
Sage.nacionalidad="China"
Sage.idioma= "China"
print("Atributos\n")
print(f" edad: {Sage.edad}")
print(f" Genero: {Sage.genero}")
print(f" Color de piel: {Sage.color}")
print(f" Color de pelo: {Sage.color_pelo}")
print(f" nacionalidad: {Sage.nacionalidad}")
print(f" idioma natal: {Sage.idioma}")
print("\n Funciones \n")
Sage.correr1086("Sage")
Sage.comer1086("Sage")
Sage.escuchar1086("Sage")
Sage.cocina1086("Sage")
Sage.ejercita1086("Sage")
Sage.descanza1086("Sage")


