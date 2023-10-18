"""
Un par de funciones de práctica 
"""


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





if __name__ == '__main__':
    porcentajem2()
    descuento_condicionado()