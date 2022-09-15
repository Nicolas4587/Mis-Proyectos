def mi_len(word):
    tmp = 0
    for i in word:
        tmp += 1
    return tmp

print(mi_len('hola'))


def calcular_iva(valor):
    return int(valor)*0.19

print(f'El iva del valor que ingresaste es: {calcular_iva(int(input("Por favor ingresa un valor para calcular el iva de este: ")))}')

def es_multiplo(primero, segundo):
    if primero%segundo == 0:
        return 'El primero SI es múltiplo del segundo'
    else:
        return 'El primero NO es múltiplo del segundo'

primer_numero = int(input('Por favor ingresa el primer número: '))

segundo_NUMERO = int(input('Por favor ingresa el segundo número: '))

print(es_multiplo(primer_numero, segundo_NUMERO))
