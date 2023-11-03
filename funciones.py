"""
Un par de funciones de práctica y conocimientos básicos
"""
import random
import requests
import json

#Calcular porcentajes
def porcentajem2(m2totales, m2cubiertos):
    m2descubiertos = m2totales - m2cubiertos
    pm2cubiertos = (m2cubiertos * 100) / m2totales
    pm2descubiertos = (m2descubiertos * 100) / m2totales
    return pm2cubiertos, pm2descubiertos


def descuento_condicionado(importe_venta):
    if importe_venta < 1000:
        importe_final = 1000
    elif importe_venta >= 1000 and importe_venta < 5000:
        importe_final = importe_venta * 0,90
    elif importe_venta >= 5000:
        importe_final = importe_venta * 0,82
    return importe_final

#Obtener el mayor y el menor en una lista numerica random
def may_men():
    numeros = [random.randint(0,100) for x in range(10)]
    for x in numeros:

        if x == numeros[1] and x > numeros[0]:
                mayor = x
                menor = numeros[0]
        elif x == numeros[1] and x < numeros[0]:
            mayor = numeros[0]
            menor = x
        elif x != numeros[0]:
            if x > mayor:
                mayor = x
            elif x < menor:
                menor = x
         
#Comprobar si un numero es multiplo de otro
def multiplo_5(numero):
    if numero % 5 == 0:
        es_multiplo = True


def tabla_del(numero):

    tabla = [numero * x for x in range(50)]
    return tabla


#Descuentos sabiendo la cantidad de litros vendidos y el importe a pagar 
def escala_descuentos(importe_total, litros_vendidos):
    if litros_vendidos > 500:
        importe_final = importe_total * 0.75
    elif litros_vendidos >= 301:
        importe_final = importe_total * 0.85
    elif litros_vendidos >= 101:
        importe_final = importe_total * 0.90
    else:
        importe_final = importe_total
    return importe_final


#Escala de precios segun el usuario combine, 
# Opción de procesador, memoria y si desea extender el Disco
def compra_combinada(OP, OM, OD):
    match OP:
        case 1:
            match OM:
                case 1:
                    p = 800
                case 2:
                    p = 900
                case 3:
                    p = 1000
        case 2:
            match OM:
                case 1:
                    p = 900
                case 2:
                    p = 1000
                case 3:
                    p = 1400
        case 3:
            match OM:
                case 1:
                    p = 1200
                case 2:
                    p = 1400
                case 3:
                    p = 2000
    if OD == 1:
        p = p + 300
    print (p)
    return p


def es_primo(numero):
    acu = 0
    for x in range(1, numero+1):
        if (numero % x) == 0:
            acu += 1
    if acu == 2:
        return True

#Calcular promedio de una lista de numeros
def promedio(numeros):

    if len(numeros) != 0:
        promedio = sum(numeros) / len(numeros)
    elif numeros == 0:
        promedio = 0
    return promedio


#Funciones de Extraccion de un JSON y manipulación de sus datos
def extraer(url):
    response = requests.get(url= url)
    if response.ok:
        data = response.json()
        return data

def contar_titulos(data):
    titulos = {}
    for i in range(11):
        contador_titulos = 0
        for x in data:            
            if x["userId"] == i and x["completed"] == True:
                contador_titulos += 1
                titulos[i] = contador_titulos
    return titulos

if __name__ == '__main__':
    promedio()   
    porcentajem2()
    descuento_condicionado()
    may_men()
    multiplo_5()
    tabla_del()
    escala_descuentos()
    es_primo()
    compra_combinada()
    extraer()
    contar_titulos()