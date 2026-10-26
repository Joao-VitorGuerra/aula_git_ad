nomes_aprovados = ["João", "Maria", "Pedro", "Mainara"]

nome = input("Digite o seu nome: ").strip()

if nome.lower() in [n.lower() for n in nomes_aprovados]:
    print(f"{nome} aprovade!")
else:
    print(f"{nome} reprovade!")