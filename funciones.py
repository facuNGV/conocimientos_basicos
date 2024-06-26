"""
Un par de funciones de práctica y conocimientos básicos
"""
import random
import requests
import json


#Calcular promedio de una lista de numeros
def promedio(numeros):
    if len(numeros) != 0:
        promedio = sum(numeros) / len(numeros)
    elif numeros == 0:
        promedio = 0
    return promedio


#Calcular porcentajes
def porcentajem2(m2totales, m2cubiertos):
    m2descubiertos = m2totales - m2cubiertos
    pm2cubiertos = (m2cubiertos * 100) / m2totales
    pm2descubiertos = (m2descubiertos * 100) / m2totales
    return pm2cubiertos, pm2descubiertos


def descuento_condicionado(importe_venta):
    if importe_venta < 1000:
        importe_final = importe_venta
    elif importe_venta >= 1000 and importe_venta < 5000:
        importe_final = importe_venta * 0,90
    elif importe_venta >= 5000:
        importe_final = importe_venta * 0,82
    return importe_final


#Obtener el maximo y minimo de una lista random
def may_men():
    numeros = [random.randint(0,50) for x in range(5)]
    
    if numeros[0] > numeros[1]:
        mayor = numeros[0]
        menor = numeros[1]
    elif numeros[0] < numeros[1]:
        menor = numeros[0]
        mayor = numeros[1]
    elif numeros [0] == numeros[1]:
        mayor = numeros[0]
        menor = numeros [1]
    
    for x in numeros:      
        if x > mayor:
            mayor = x
        elif x < menor:
            menor = x    


#Comprobar si un numero es multiplo de otro
def es_multiplo():
    es_multiplo = False
    numero = int(input("Ingrese un numero: "))
    mutiplo_de = int(input("Desea saber si es multiplo de: "))
    if numero % mutiplo_de == 0:
        es_multiplo = True
        print("Es multiplo")
    else:
        print("No es multiplo")
    return es_multiplo


def tabla_del():
    numero = int(input("Cual es la tabla del: "))
    tabla = [numero * x for x in range(1, 10)]
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
# Opción de procesador, Opcion de memoria y si desea extender el Disco
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


#Funciones de Extraccion de un JSON y creación de un dict a partir de este
def extraer(url):
    response = requests.get(url= url)
    if response.ok:
        data = response.json()
        return data

#Analiza un json correspondiente a un registro de estudiantes
def contar_titulos():
    data = extraer(url= 'some url api json')
    titulos = {}
    for i in range(11):
        contador_titulos = 0
        for x in data:            
            if x["userId"] == i and x["completed"] == True:
                contador_titulos += 1
                titulos[i] = contador_titulos
    return titulos

if __name__ == '__main__':
    tabla_del()
    es_multiplo()
    may_men()
    promedio() 
    porcentajem2()
    descuento_condicionado()
    escala_descuentos()
    es_primo()
    compra_combinada()
    extraer()
    contar_titulos()