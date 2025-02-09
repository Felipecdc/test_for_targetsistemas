def inverter_string(s):
    inversa = ''
    for i in range(len(s)-1, -1, -1):
        inversa += s[i]
    return inversa

texto = input("Digite uma string para inverter: ")
print(f"Texto invertido: {inverter_string(texto)}")
