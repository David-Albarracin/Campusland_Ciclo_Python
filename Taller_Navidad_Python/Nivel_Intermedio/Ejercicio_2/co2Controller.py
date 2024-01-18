import reusable

def co2Encuesta(dependencia) -> list:
    pcs = reusable.inputFloat("¿Cuántos computadores tiene la oficina?")
    pcsC02 = (((250 * pcs)* 8) / 1000) * 30

    tvs = reusable.inputFloat("¿Cuántos televisores tiene la oficina? ")
    tvsCo2 =  (((100 * tvs)* 1) / 1000) * 30

    micro = reusable.yesORnot("¿Cuenta la oficina con horno microondas?")
    microC02 = 0
    if micro:
        microC02 = ((800 * 1) / 1000) * 30

    transporte = reusable.yesORnot("¿La oficina dispone de mensajeros que utilizan el carro o la moto de la empresa?")
    trasC02 = 0
    if (transporte):
        kilo = reusable.inputFloat("¿cuántos kilómetros aproximados recorren estos mensajeros al Mes?")
        trasC02 = ((kilo / 30 ) * 3.7 ) * 0.023

    dependencia["dispositivos"] = (pcsC02 + tvsCo2 + microC02) * 0.03
    dependencia["transporte"] = trasC02
    dependencia["CO2"] = (dependencia["dispositivos"] + dependencia["transporte"]) / 720
    return dependencia
