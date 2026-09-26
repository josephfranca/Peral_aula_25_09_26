# teste = "Jeniffer cabecinha de guidão"
# print(teste)

def calcularMedia(nota1,nota2):
    return (nota1 + nota2) / 2

print("=== Sistema de notas dos alunos")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = calcularMedia(n1,n2)

print(f"A média final é: {media: .2f} ")

if media >= 7.0:
    print("Resultado: Aprovado!")
else:
    print("Resultado: Reprovado!")
