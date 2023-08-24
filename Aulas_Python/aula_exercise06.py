#Formulário

#def age():
#  sum
#  return

chaves = []
valores = []

formulario = {
    "Nome": "",
    "Idade": "",
    "Gênero": "",
    "Ocupação": ""
}

while True:
    resp = int(input("Tecle 1 para se inscrever, 3 para pesquisar e 2 para sair: \n "))
    if resp == 2:
        print("Encerrando Acesso")
        dic = dict(zip(chaves, valores))
        break
    elif resp == 3:
        proc = str(input("Digite o nome a ser procurado: \n"))
        if proc in chaves:
            print(f"O usuário {proc} está registrado.")
        proc1 = proc.get(chaves)
        
    elif resp == 1:
        while True:
            keys = str(input("Digite o seu nome: \n")).capitalize()
            values = int(input("Digite seu ano de nascimento: \n"))
            cont = str(input("Continuar? \n")).lower()
            chaves.append(keys)
            valores.append(values)
            if cont == "não" or cont == "nao" or cont == "n":
                break

print(dic)