contador = 0
contador_analista = 0
contador_cientista = 0
cientista_qualificado = 0
analista_qualificado = 0
informacoes_lista = dict()
curriculo_stephanie = dict ()

def linha ():
    print(' -'*35)
    
quantidadedecandidatos = int(input('Quantos candidatos você gostaria de cadastrar: '))
while contador < quantidadedecandidatos:
    candidato = input('Digite o seu nome: ')
    print('candidato: {candidato}')
    linha()
    print('VAGAS DISPONÍVEIS:\n1- Analista de Dados\n2- Cientista de Dados')
    linha()
    vaga = input(f'{candidato}, digite a vaga desejada: ')
    linha()
    if vaga == 'analista de dados'.lower(): 
        requisito_cidade = input('Digite a sua cidade: ')
        requisito_graduacao = input('Você tem graduação? Se sim, digite qual. Se não, digite NÃO: ')
        print('Bom, queremos saber quais habilidades você tem conhecimento, tudo bem? Vou listar e você me diz quais têm.\n1-Python\n2-Power BI\n3-SQL\n4-Boa comunicação\n')
        habilidades = input('Escreva quais: ')
        

        if 'python' or 'sql' or'power bi' or 'boa comunicação' in vaga.items():
            print(f'{candidato} está qualificado')
            contador_analista += 1
        else:
            print(f'Infelizmente diante dos requisitos da vaga, dessa vez {candidato} não está participando desse processo seletivo.')
            
        for analista_qualificado in contador_analista.values():
            if len(analista_qualificado) > 0:   
                print(f'Candidatos com possível competência à vaga para analista: ')
        linha()
    elif vaga == 'cientista de dados'.lower():
        requisito_cidade = input('Digite a sua cidade: ')
        requisito_graduacao = input('Possui graduação? Se sim, digite qual. Se não, digite NÃO: ')
        if requisito_graduacao == 'não' or 'nao' or 'Não' or 'Nao' or 'NÃO' or 'NAO':
            requisito_graduacao = ('sem graduação')
        print('\n1-Python\n2-Banco de Dados\n3-Machine Learning\n4-Resolução de problemas\n5-Estatística')
        habilidades = input(f'Escreva quais habilidades listadas acima {candidato} possui: ')
        
        if 'python' or 'banco de dados' or 'machine learning' or 'resolucao de problemas' or 'estatística' in informacoes_lista.items():
            print(f'{candidato} está qualificado')
            contador_cientista += 1
        else:
            print(f'Infelizmente diante dos requisitos da vaga, dessa vez {candidato} não está participando desse processo seletivo.')
            contador_cientista.pop()
            
        for cientista_qualificado in contador_cientista.values():
            if len(cientista_qualificado) > 0:
                print(f'Candidatos com possível competência à vaga para cientista: ')
                
        linha ()
    lista_de_nomes = [candidato]
    lista_de_vagas = [vaga]
    lista_de_requisitos_cidade = [requisito_cidade]
    lista_de_requisitos_graduacao = [requisito_graduacao]
    lista_de_habilidades = [habilidades]
    contador = contador +1

    informacoes = [candidato, vaga, requisito_cidade, requisito_graduacao, habilidades]
    informacoes_lista [candidato] = vaga, requisito_cidade, requisito_graduacao, habilidades
    print(informacoes_lista)
    print(type(informacoes_lista))

print(f'Quantidade de analistas de dados inscritos: {len(contador_analista)}\nQuantidade de cientistas de dados inscritos: {len(contador_cientista)}')
        

def criacao ():
    with open ('G:\\Meu Drive\\Data Analytics\\Resilia\Módulo 2\\informacoes_lista.txt','w') as arquivo:
        for valor in informacoes_lista:
            arquivo.write(str(valor) + '\n')
            print(informacoes_lista)