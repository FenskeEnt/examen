
def lista_impar(lista):
    if len(lista) % 2 != 0:
        lista.pop(0)

    p_central = int(len(lista) / 2)
    valor_usuario = int(input('Ingrese un valor entre [24, 130]: '))

    if valor_usuario >= 24 and valor_usuario <= 130:
        lista.insert(p_central, valor_usuario) 
    else:
        print('El valor debe ser entre 24 y 130')

def nuevo_valor_x(lista):
    valor_usuario = int(input('Ingrese un valor no repetido a la lista: '))
    if valor_usuario not in lista:
        lista.append(valor_usuario)


def mostrar_promedio_lista(lista):
    return sum(lista) / len(lista)

def mostrar_lista_creciente(lista):
    if lista == lista.sort():
        print('Creciente')

def es_primo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def suma_primo(lista):
    if es_primo(len(lista)) == True:
        print('Suma primo')

#Programa inicial
listaV = [4, 5, 7, 9, 10, 11, 12, 13, 14]
lista_impar(listaV)
print('Ingrese una opcion')
print('Para mostrar el promedio de la listaV ingrese 1')
print('Para mostrar un mensaje CRECIENTE si la listaV esta ordena de forma creciente ingrese 2')
print('Para mostrar el mensaje SUMA PRIMO si la suma de los valores de la listaV es un numero primo ingrese 3')
opcion = int(input('Opcion: '))
if opcion == 1:
    print(mostrar_promedio_lista(listaV))
elif opcion == 2:
    mostrar_lista_creciente(listaV)
elif opcion == 3:
    suma_primo(listaV)
else:
    print('Esa opcion no existe')




