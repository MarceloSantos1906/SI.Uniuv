'''
exercicio 8

Faça um programa que informe a distância em quilômetros de um raio para o
observador.
• O observador deve informar o tempo (em segundos) transcorrido entre ver o
raio e ouvir o trovão;
• Assuma que a velocidade do som seja 340 m/s.

'''
v_som = 340
delay_trovao = float(input("Insira o quanto tempo em segundos se passaram entre ver o trovao e ouvi-lo: "))

distancia = v_som*delay_trovao

print("O trovão foi aproximadamente a %2.f" % distancia, "metros")