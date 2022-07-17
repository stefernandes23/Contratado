contador_candidatos_analista = {}
contador_candidatos_cientista = {}
contador_cientista = contador_analista = palavra_chave_analista_de_dados = palavra_chave_cientista_de_dados = contador =  0
informacoes_lista = dict()
curriculo_stephanie = dict ()

def linha ():
    print(' -'*35)

linha() 
print('                    Bem-vindo!')
linha()
quantidadedecandidatos = int(input('Quantos candidatos você gostaria de cadastrar: '))
print(quantidadedecandidatos)
while contador < quantidadedecandidatos:
    candidato = input('\nDigite o nome do candidato: ').lower()
    print(f'candidato: {candidato}')
    linha()
    print('VAGAS DISPONÍVEIS:\na- Analista de Dados\nb- Cientista de Dados')
    vaga = input(f'{candidato}, digite a vaga desejada [ESCREVA A LETRA CORRESPONDENTE À VAGA]: \n').lower()
    if vaga == 'a': 
        vaga = ('Analista de Dados')
        contador_analista += 1
        requisito_cidade = input('Digite a sua cidade: \n').lower()
        requisito_graduacao = input('Possui graduação na área de tecnologia? [S]/[N]: \n').lower()
        if requisito_graduacao == 'não' or 'nao' or 'Não' or 'Nao' or 'NÃO' or 'NAO' or 'n' or 'N':
            requisito_graduacao = ('sem graduacao')
        elif requisito_graduacao == 'sim' or 'Sim' or 'SIM' or 'S' or 's': 
            requisito_graduacao = ('possui graduacao')
        linha()
        habilidades = (input(f'\nPython\nPower BI\nSQL\nBoa comunicação\nParar\n \nDigite sim se o candidato tiver pelo menos alguma dessas habilidades [S/N]: ')).lower()
        if habilidades == 'n':
            habilidades = ('não possui habilidades')
            print(f'{candidato} não está participando desse processo seletivo.\n')
        elif habilidades == 's':
            habilidades = ('possui habilidades')
            print(f'{candidato} está participando desse processo seletivo.\n')
            palavra_chave_analista_de_dados += 1
        contador += 1
    elif vaga == 'b':
        vaga = ('Cientista de Dados')
        contador_cientista += 1
        requisito_cidade = input('Digite a sua cidade: \n').lower()
        requisito_graduacao = input('Possui graduação na área de tecnologia?\n[S]/[N]\n').lower()
        if requisito_graduacao == 'não' or 'nao' or 'Não' or 'Nao' or 'NÃO' or 'NAO' or 'n' or 'N':
            requisito_graduacao = ('sem graduacao')
        elif requisito_graduacao == 'sim' or 'Sim' or 'SIM' or 'S' or 's': 
            requisito_graduacao = ('possui graduacao')
        linha()
        habilidades = (input(f'Agora habilidades.\nPython\nBanco de Dados\nMachine Learning\nResolução de Problemas\nEstatística\nParar\n{candidato} tem pelo menos alguma dessas habilidades? Digite [S/N]: \n')).lower()
        if habilidades == 'n': 
            habilidades = ('não possui habilidades')
            print(f'{candidato} não está participando desse processo seletivo.\n')
        elif habilidades == 's':
            habilidades = ('possui habilidades')
            print(f'{candidato} está participando desse processo seletivo.\n')
            palavra_chave_cientista_de_dados += 1
        contador += 1
    lista_de_nomes = [candidato]
    lista_de_vagas = [vaga]
    lista_de_requisitos_cidade = [requisito_cidade]
    lista_de_requisitos_graduacao = [requisito_graduacao]
    lista_de_habilidades = [habilidades]
    informacoes = [candidato, vaga, requisito_cidade, requisito_graduacao, habilidades]
    informacoes_lista [candidato] = vaga, requisito_cidade, requisito_graduacao, habilidades
    print(f'Candidatos inscritos para a vaga de Analista de Dados: {contador_analista}')
    print(f'Candidatos com palavra-chave para Analista de Dados: {palavra_chave_analista_de_dados}\n')
    print(f'Candidatos inscritos para a vaga de Cientista de Dados: {contador_cientista}')
    print (f'Candidatos com palavra-chave para Cientista de Dados: {palavra_chave_cientista_de_dados}\n')
    total_de_candidatos = [contador_cientista + contador_analista]
    print(f'O total de candidatos inscritos é: {total_de_candidatos}')
    informacoes = [candidato, vaga, requisito_cidade, requisito_graduacao, habilidades]
    print(informacoes_lista)

def criacao ():
    arquivo = open ('G:\\Meu Drive\\Data Analytics\\Resilia\Módulo 2\\curriculo_stephanie.txt','w')
    for valor in informacoes_lista:
        arquivo.write(str(informacoes_lista))
        arquivo.write('\n')
criacao ()
