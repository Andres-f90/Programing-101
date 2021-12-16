# VARIABLES
# Algo que tiene un valor y que puede cambiar
def main():
    # Definir una variable: En python, para definir una variable, tienes que asignarle un valor con el signo =
    nombre = 'frutas con arepa'

    # Funcion type(): Sirve para saber de que tipo es una variable cualquiera
    type(nombre) # Va a decir que la variable nombre es un str, osea String

def integerIntro():
  # Algunos tipos de variables en python (los mas comunes):
  # 1. Entero: Es un numero sin decimales INTEGER
  andres_1 = 16
  print(f'The variable is a {type(andres_1)}')

def stringIntro():
  # 2. String: Cadena de caracteres. Ejemplo '!2@hgdyE' Debe llevar comillas simples o dobles SIEMPRE.
  variable_string = 'l!#dhaTdrh'
  variable_string_2 = "Also a string"
  andres_2 = "5 Manzanas !"
  print(type(andres_2))

  # Con los strings se pueden hacer muchas cosas, por ejemplo hacer strings con mas variables usando f''
  intTemp = 55
  string_complejo = f'Mi variable entera es: {intTemp}'

  # Cuando haces un string con f'', puedes meter codigo dentro de este con {}
  juan = f'5+4.4 = {"{5}"} aqui'

  print(juan)

  # Special String Methods
  my_string = 'string value'
  special_string_methods = []

  special_string_methods.append(my_string.capitalize())
  special_string_methods.append(my_string.find('v'))

  print(special_string_methods)

def booleanIntro():
  # 3. Boolean: Variable que tiene solo dos posibilidades [True, False].
  variable_boolean_t = True
  variable_boolean_f = False
  andres_3 = True
  print(type(andres_3))

def listIntro():
  # 4. Listas: Lista de variables.
  variable_lista = [35, 25, True]
  andres_4 = ['frutas', 'arepas', 'algo']
  andres_4_1 = ["h", 4.5, 78, False, [35, 25, True]]
  print(type(andres_4))

def floatIntro():
  # 5. Float: Un numero con decimales. Se le llama float porque tiene una coma flotando entre los numeros
  variable_float = 1.5
  andres_5 = 4.4
  print(type(andres_5))

#Tarea: Poner un ejemplo de cada tipo de variable
# ----- Correcciones primer intento:
# ----- 1. Los nombres de las variables no deben ser iguales porque si no, no se pueden diferenciar
# ----- 2. Poner nombres faciles y ser consistente
# ----- 3. NO OLVIDAR PONER COMILLAS A LOS STRINGS

# ----- Preguntas aparte -----

# Que pasa si definimos la variable abajo ?
# Como poner ' sin tener que poner una letra ??

def changeType():
  print('We are about to sum a couple numbers...')
  firstNumber = input('Number 1: ')
  secondNumber = input('Number 2: ')

  print(f'The sum of the two numbers is: {firstNumber + secondNumber}')
  print(f'The number 1 type is {type(firstNumber)} and the number 2 type is {type(secondNumber)}')
  print('Converting strings to integers with int()...')
  
  firstNumber = int(firstNumber)
  secondNumber = int(secondNumber)

  print(f'The number 1 type is {type(firstNumber)} and the number 2 type is {type(secondNumber)}')
  print(f'Finally, the sum of the two numbers is: {firstNumber + secondNumber}')
  return

if __name__ == '__main__':
    main()
