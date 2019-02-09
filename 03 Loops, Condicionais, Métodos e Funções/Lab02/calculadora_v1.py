# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print("Selecione o número da operação desejada:")

print("1-soma \n 2-subtração \n 3-Multiplicação \n 4-Divisão")

op = int(input("Digite a operação desejada(1-2-3-4)"))

num1 = int(input("digite o primeiro numero:"))
num2 = int(input("digite o segundo  numero:"))
if op == 1:
    soma = num1+num2
    print(soma)
    
elif op == 2:    
    sub = num1 - num2
    print(sub)
    
elif op == 3:    
    mult = num1 * num2
    print(mult)   
    
elif op == 4:    
    div = num1 / num2
    print(div)
else:
    print("não e uma operação valida")