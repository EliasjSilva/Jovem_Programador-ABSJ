frutas = ("uva", "maça", "uva", "tangerina", "uva")
set(frutas)
print(set(frutas))

l1 = ["Nome" , "idade"]
l2 = ["Fulano" , 12]
d = dict(zip(l1,l2))
#print(d.items())

lista = [("nome", "fulano"), ("idade", 12)]
d2 = dict(lista)
#print(d2)

#for chave in d:
#    for valor in d:
#       print(chave, valor)

chaves = []
valores = []

while True:
    r = int(input("Digite o número 1 para adicionar imformações: \n Digete 2 para finalizar: \n"))
    if r == 2:
        dic = dict(zip(chaves, valores))
        break
    elif r == 1:
        while True:
            pu = str(input("Digite a pergunta que foi feita! \n")).capitalize()
            ru = str(input("Digite a resposta que foi dade! \n")).capitalize()
            cont = str(input("Continuar? \n")).lower()
            chaves.append(pu)
            valores.append(ru)
            if cont == "não" or cont == "nao" or cont == "n":
                break
print(dic)





