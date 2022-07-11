contador = 0
informacoes_lista = dict()
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
        linha()
    elif vaga == 'cientista de dados'.lower():
        requisito_cidade = input('Digite a sua cidade: ')
        requisito_graduacao = input('Você tem graduação? Se sim, digite qual. Se não, digite NÃO: ')
        print('Bom, queremos saber quais habilidades você tem conhecimento, tudo bem? Vou listar e você me diz quais têm.\n1-Python\n2-Banco de Dados\n3-Machine Learning\n4-Resolução de problemas\n5-Estatística')
        habilidades = input('Escreva quais: ')
        linha ()
    lista_de_nomes = [candidato]
    lista_de_vagas = [vaga]
    lista_de_requisitos_cidade = [requisito_cidade]
    lista_de_requisitos_graduacao = [requisito_graduacao]
    lista_de_habilidades = [habilidades]
    informacoes = [candidato, vaga, requisito_cidade, requisito_graduacao, habilidades]
    informacoes_lista [candidato] = vaga, requisito_cidade, requisito_graduacao, habilidades
    print(informacoes_lista)
    print(type(informacoes_lista))
    contador = contador +1
    if 'python'or 'banco de dados'or 'sql' or 'boa comunicação' or 'power bi' 'machine learning'or 'resolucao de problemas' or 'estatística' in informacoes_lista:
        print(f"{candidato}, você está participando do nosso processo seletivo")
    else: 
        print('Infelizmente diante dos requisitos da vaga, dessa vez você não está participando desse processo seletivo. Mas não desista, {candidato}.')