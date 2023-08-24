

l1=[]
l2=[]
d=dict(zip(l1,l2))
d
print(d.items())
     

chaves=[]
valores=[]
obs=[]
while True:
    r=int(input('Digite 1 para adicionar informações! \n Digite 2 para finalizar! \n '))
    if r == 2:
        d=dict(zip(chaves,valores))
        break
        
    elif r == 1:
        while True:
            pu=str(input('Digite a pergunta que foi feita! \n')).lower()
            ru=str(input('Digite a resposta qu foi dada! \n')).lower()
            cont = str(input('Continua?')).lower()
            chaves.append(pu)
            valores.append(ru)
            if cont == 'não' or cont == 'nao' or cont  == 'n':
                break         

while True:
    acoes = str(input('Ações complementares \n'))
    if 'pesq' in acoes:
        sn=str(input('Você quer pesquisar um item?')).lower()
        if 's' in sn:
            p=str(input('Digite a sua pesquisa! \n')).lower()
            if p in d:
                print(f'{d.get(p)} foi encontrado')
            else:
                print(f'{p} não foi encontrado')
    elif 'edit' in acoes:
        sn=str(input('Você quer editar um item?')).lower()
        if 's' in sn:
            p=str(input('Informe a chave do que deseja editar \n')).lower()
            if p in d:
                d[p]=input('Informe o novo valor! \n')
                print(f'{p} foi atualizado por {d[p] }')                                               
            else:
                print('Não encontrado.')
    elif 'adic' in acoes:
        sn=str(input('Você quer adicionar um novo campo?')).lower()
        if 's'in sn:
            motivo = str(input('Informe o motivo da adição de um novo campo \n'))
            obsAdc=tuple(motivo)
            obs.append(obsAdc)
            p=str(input('Informe a chave a ser adicionada \n'))
            d[p]=str(input('Informe o valor a ser adicionado \n'))
            v=str(input('Deseja visualizar as informações aramazenadas?')).lower()
            if 's' in v:
                print(d)
    elif 'exclu' in acoes:
        sn=str(input('Você quer excluir um item?')).lower()
        if 's' in sn:
            motivo = str(input('Informe o motivo da exclusão de um novo campo \n'))
            obsExc=tuple(motivo)
            obs.append(obsExc)
            p=str(input('Informe a chave que deseja excluir /n')).lower()
            if p in d:
                r=input('Deseja mesmo excluir esse par de informação?').lower()
                if 's' in r:
                    d.pop(p)
    elif 'list' in acoes:
        print(d)
    elif 'he' in acoes:
        p=str(input('As ações disponíveis são: \n Pesquisar, editar, excluir, adicionar, listar, obs (para ums lista de observações) e sair. \n Deseja continuar? \n')).lower()
    elif 'sai' in acoes:
        r=input('Deseja sair da aplicação?').lower()
        if 's' in r:
            break
    elif 'obs' in acoes:
        if len(obs) == 0:
            print('Sem observações para visualizar')
        else:
            print(obs)        
    else:
        print('Você precisa escolher uma opção válida ou HELP para ajuda')  

     