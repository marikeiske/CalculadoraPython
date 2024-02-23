def soma(a, b):
  return a + b

def subtracao(a, b):
  return a - b

def multiplicacao(a, b):
  return a * b

def divisao(a, b):
  return a / b

while True:
  print("Selecione a operação:")
  print("1: Soma")
  print("2: Subtração")
  print("3: Multiplicação")
  print("4: Divisão")
  print("0: Sair")

  escolha = input("Digite o número para a operação correspondente: ")

  if escolha == '0':
    print("Saindo da calculadora.")
    break
  elif escolha in ('1', '2', '3', '4'):
    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))

    if escolha == '1':
      resultado = soma(num1, num2)
    elif escolha == '2':
      resultado = subtracao(num1, num2)
    elif escolha == '3':
      resultado = multiplicacao(num1, num2)
    elif escolha == '4':
      resultado = divisao(num1, num2)

    print("Resultado:", resultado)
  else:
    print("Essa opção não existe. Tente novamente.")
