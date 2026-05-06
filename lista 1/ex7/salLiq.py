def calcSal(valHora, horasT):
    bruto = valHora * horasT
    
    liq = bruto * 0.81 if bruto > 5000 else bruto * 0.89
    return round(liq , 2)

    