nome = input("Informe o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"{nome} foi aprovade, com a media {media}")
elif media >= 5: 
    print(f"{nome} está de exame, com a media {media}!")
else: 
    print(f"{nome} foi reprovade, com a media {media}!")