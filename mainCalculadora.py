from calculadora import Calculadora

calculadora = Calculadora()

while True:
    print("+--------------+")
    print(f"|             {calculadora.visor}|")
    print("+--------------+")
    print("(+) somar")
    print("(-) subtrair")
    print("(/) dividir")
    print("(*) multiplicar")
    print("(r) resetar")
    print("(d) desfazer")
    operacao = (input("Informe o operador: "))
    if operacao == '-':
        numero = int(input("Informe o numero: "))
        print("Operação: -")
        calculadora.subtrair(numero)
    elif operacao == '+':
        numero = int(input("Informe o numero: "))
        print("Operação: +")
        calculadora.somar(numero)
    elif operacao == '/':
        numero = int(input("Informe o numero: "))
        print("Operação: /")
        calculadora.dividir(numero)
    elif operacao == '*':
        numero = int(input("Informe o numero: "))
        print("Operação: *")
        calculadora.multiplicar(numero)

    elif operacao == 'r': 
        calculadora.resetar()
    elif operacao == 'd':
        calculadora.voltar()
     
