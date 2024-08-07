peso = float(input("Insira seu peso em kgs: "))
altura = float(input("Insira sua altura em metros: "))

imc = peso/(altura*altura)

if imc < 18.5:
    print("Você está abaixo do peso")

elif imc > 18.5 and imc <25:
    print("Você está saudavel")

elif imc >25 and imc <30:
    print("Você está acima do peso")

elif imc > 30 and imc <35:
    print("Você está com obesidade grau 1")

elif imc > 35 and imc <40:
    print("Você está com obesidade grau 2")

elif imc >= 40:
    print("Você está com obesidade grau 3")