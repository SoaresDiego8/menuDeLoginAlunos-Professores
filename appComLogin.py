'''
CRIADOR: Diego Henrique Silva Soares
APP: Menu para alunos e professores em uma faculdade
'''


# BIBLIOTECAS IMPORTADAS =======================================================================================================================================================
import os 
from datetime import datetime
from time import sleep



# LISTAS CRIADAS ===============================================================================================================================================================
listaDeAluno = [{'nome': 'Admin', 'idade': 00, 'sexo': 'M', 'dataNascimento': '00-00-0000', 'matricula': False}]
listaDeProfessor = [{'nome': 'Admin', 'idade': 00, 'sexo': 'F', 'dataNascimento': '00-00-0000','status': False}]
listaLoginAluno = [{'usuario': 'admin', 'senha': 'admin', 'status': True}]
listaLoginProfessor = [{'usuario': 'admin', 'senha': 'admin', 'status': True}]

# FUNÇÕES GERAIS ===============================================================================================================================================================
''' Cores = vermelho e verde em negrito'''
negrito = f'\033[1m'
red = f'{negrito}\033[91m'
green = f'{negrito}\033[92m'
reset = '\033[0m'


def limparTerminal():
    os.system('cls') # função para limpar o terminal

def exibirTitulo(texto):
    limparTerminal()
    '''
    Utilizei da biblioteca OS para usar o 'get_terminal_size' e descobrir o tamanho do terminal
    independente do computador/notebook utilizado e fazer um menu.
    '''
    tamanho_terminal = os.get_terminal_size().columns
    '''
    Utilizei a função LEN para ler o tamanho do texto inserido e colocar o mesmo tanto de '_'
    '''
    # Centraliza o texto, adicionando espaços ao redor
    texto_centralizado = texto.center(tamanho_terminal)
    linhaDoSubTitulo = '_' * (len(texto_centralizado))
    print(f'{negrito}{linhaDoSubTitulo}{reset}')
    print(f'{negrito}{texto_centralizado}{reset}')
    print(f'{negrito}{linhaDoSubTitulo}{reset}')
    print()

def sairDoApp():
    print(f'{negrito}Finalizando o aplicativo...{reset}')
    limparTerminal()

def opcaoInvalida():
    print(f'{red}Opção inválida.{reset}')

def voltarAoMenuLogin():
    input(f'{negrito}Digite qualquer tecla para voltar ao MENU DE LOGIN:{reset} ')
    menuLogin()
def voltarAoMenuAluno():
    input(f'{negrito}Digite qualquer tecla para voltar ao MENU DO ALUNO:{reset} ')
    menuDoAluno()

def voltarAoMenuProfessor():
    input(f'{negrito}Digite qualquer tecla para voltar ao MENU DO PROFESSOR:{reset} ')
    menuDoProfessor()


# LOGIN ========================================================================================================================================================================
def menuLogin():
    limparTerminal()
    exibirTitulo('MENU DE LOGIN')
    print(f'''{green}
1. Login aluno.
2. Login professor.
3. Criar login p/ aluno.
4. Criar login p/ professor.
5. Sair.{reset}''')
    
    escolherOpcaoAlunoOrProfessor = input(f'{negrito}Escolha uma opção:{reset} ')
    print(f'{negrito}A opção escolhida foi:{reset} {escolherOpcaoAlunoOrProfessor} ')
    try:
        if escolherOpcaoAlunoOrProfessor == '1':
            loginAluno()
        elif escolherOpcaoAlunoOrProfessor == '2':
            loginProfessor()
        elif escolherOpcaoAlunoOrProfessor == '3':
            criarLoginAluno()
        elif escolherOpcaoAlunoOrProfessor == '4':
            criarLoginProfessor()
        elif escolherOpcaoAlunoOrProfessor == '5':
            sairDoApp()
        else:
            opcaoInvalida()
            sleep(2)
            voltarAoMenuLogin()
    except:
        opcaoInvalida()
        sleep(2)
        voltarAoMenuLogin()

def loginAluno():
    limparTerminal()
    exibirTitulo('Login Aluno')

    nomeUsuario = input(f'{negrito}Usuário:{reset} ')
    senhaUsuario = input(f'{negrito}Senha:{reset} ')
    loginEncontrado = False
    # Verificando se o usuario e senha digitados se encontram válidos. Caso não, retorne um erro
    for aluno in listaLoginAluno:
        if nomeUsuario == aluno['usuario'] and senhaUsuario == aluno['senha']:
            loginEncontrado = True
            mensagem = f'{green}Logando...{reset}'  
            print(mensagem)
            sleep(1.5)
            menuDoAluno()

    if not loginEncontrado:
        print(f'{red}O usuário não foi encontrado, verifique os dados e tente novamente!{reset}')
        while True:
            resposta = input((f'{negrito}Dejesa tenta fazer o login novamente [S/N]?{reset} ')).title()
            if resposta == 'S':
                sleep(1.5)
                loginAluno()
            elif resposta == 'N':
                menuLogin()
                break
            else:
                print(f'{red}Por favor, digite apenas "S" ou "N".{reset}')

def loginProfessor():
    limparTerminal()
    exibirTitulo('Login Professor')
    
    usuarioProfessor = input(f'{negrito}Usuario:{reset} ')
    senhaProfessor = input(f'{negrito}Senha:{reset} ')
    loginEncontrado = False
    
    # Verificando se o usuario e senha digitados se encontram válidos. Caso não, retorna um erro
    for professor in listaLoginProfessor:
        if usuarioProfessor == professor['usuario'] and senhaProfessor == professor['senha']:
            loginEncontrado = True
            mensagem = f'{green}Logando...{reset}'
            print(mensagem)
            sleep(1.5)
            menuDoProfessor()

    if not loginEncontrado:
        print(f'{red}O usuário não foi encontrado, verifique os dados e tente novamente!{reset}')
        while True:
            resposta = input((f'{negrito}Dejesa tenta fazer o login novamente [S/N]?{reset} ')).title()
            if resposta == 'S':
                sleep(1.5)
                loginAluno()
            elif resposta == 'N':
                menuLogin()
                break
            else:
                print(f'{red}Por favor, digite apenas "S" ou "N".{reset}')


def criarLoginAluno():
    '''
    Criando um login para o aluno
    '''
    limparTerminal() 
    exibirTitulo('Criando login para aluno\n')

    usuarioAluno = input(f'{negrito}Usuario:{reset} ')
    senhaAluno = input(f'{negrito}Senha:{reset} ')
    dadosLoginAluno = {'usuario': usuarioAluno, 'senha': senhaAluno, 'status': True}
    listaLoginAluno.append(dadosLoginAluno)
    print(f'{green}O usuário {usuarioAluno} foi criado com sucesso!{reset}\n')
    sleep(2)
    menuLogin()

def criarLoginProfessor():
    ''' 
    Criando um login para o professor
    '''
    limparTerminal()
    exibirTitulo('Criando login para professor')

    usuarioProfessor = input(f'{negrito}Usuario:{reset} ')
    senhaProfessor = input(f'{negrito}Senha:{reset} ')
    dadosLoginProfessor = {'usuario': usuarioProfessor, 'senha': senhaProfessor, 'status': True}
    listaLoginProfessor.append(dadosLoginProfessor)
    print(f'{green}O usuário {usuarioProfessor} foi criado com sucesso!{reset}\n')
    sleep(2)
    menuLogin()






# MENU ALUNO ========================================================================================================================================================================

def menuDoAluno():
    limparTerminal()
    exibirTitulo('ÁREA DO ALUNO')
    print(f'''{green}
1. Cadastrar aluno.
2. Listar alunos.
3. Alternar status do aluno.
4. Voltar ao menu de login.{reset}''')
    escolherOpcaoAluno = int(input(f'{negrito}Escolha uma opção:{reset} '))
    print(f'{negrito}A opção escolhida foi:{reset} {escolherOpcaoAluno}')
    try:
        if escolherOpcaoAluno == 1:
            cadastrarAluno()
        elif escolherOpcaoAluno == 2:
            listarAluno()
        elif escolherOpcaoAluno == 3:
            alternarStatusDoAluno()
        elif escolherOpcaoAluno == 4:
            menuLogin()
        else:
            opcaoInvalida()
            sleep(2)
            menuDoAluno()
    except:
        opcaoInvalida()
        sleep(2)
        menuDoAluno()

def cadastrarAluno():
    limparTerminal()
    '''
    Nesta função, pedi ao aluno seus dados e fiz uma verificação para aceitar apenas dados válidos
    '''
    exibirTitulo('Cadastrando aluno')
    nomeDoAluno = input(f'{negrito}Nome completo:{reset} ')
    while True:
        idadeDoAluno = int(input(f'{negrito}Idade do(a) {nomeDoAluno}:{reset} '))
        if idadeDoAluno >= 16 and idadeDoAluno <= 60:
            break
    while True:
        sexoDoAluno = input(f'{negrito}Genêro [F/M]:{reset} ').title()
        if sexoDoAluno == 'F' or sexoDoAluno =='M':
            break
    while True:
        dataDeNascimentoDoAluno = input(f'{negrito}Digite uma data no formato DD-MM-YYYY:{reset} ')
        try:
            # Tenta converter a string para um objeto datetime
            data = datetime.strptime(dataDeNascimentoDoAluno, '%d-%m-%Y')
            break
        except:
            # Se a conversão falhar, exibe uma mensagem de erro e pede nova entrada
            print(f'{red}Data inválida. Por favor, digite a data no formato correto (DD-MM-YYYY).{reset}')

    dadosDoAluno = {'nome': nomeDoAluno, 'idade': idadeDoAluno,'sexo': sexoDoAluno,'dataNascimento': dataDeNascimentoDoAluno, 'matricula': False}
    listaDeAluno.append(dadosDoAluno)
    print(f'{green}* {nomeDoAluno} foi cadastrado com sucesso!{reset}\n')
    voltarAoMenuAluno()


def listarAluno():
    limparTerminal()
    exibirTitulo('Listando alunos')
    print(f'{negrito}{'NOME DO ALUNO'.ljust(32)} | {'IDADE'.ljust(30)} | {'GENERO'.ljust(30)} | {'DATA DE NASCIMENTO'.ljust(30)} | {'MATRICULA'}{reset}')
    for aluno in listaDeAluno:
        nomeDoAluno = aluno['nome']
        idadeDoAluno = aluno['idade']
        sexoDoAluno = aluno['sexo']
        dataDeNascimentoDoAluno = aluno['dataNascimento']
        matriculaDoAluno = f'{green}Aberta{reset}' if aluno['status'] else f'{red}Trancada{reset}'
        print(f'# {nomeDoAluno.ljust(30)} | {str(idadeDoAluno).ljust(30)} | {sexoDoAluno.ljust(30)} | {dataDeNascimentoDoAluno.ljust(30)} | {matriculaDoAluno}')
    voltarAoMenuAluno()


def alternarStatusDoAluno():
    limparTerminal()
    exibirTitulo('Alternando matricula do aluno')
    nomeDoAluno = input(f'{negrito}Digite o nome completo do aluno que deseja alternar o status:{reset} ')
    alunoEncontrado = False
    for aluno in listaDeAluno:
        if nomeDoAluno == aluno['nome']:
            alunoEncontrado = True
            aluno['matricula'] = not aluno['matricula']
            mensagem = f'{negrito}A matricula do(a) {nomeDoAluno} foi {green}Aberta{reset} com sucesso!{reset}\n' if aluno['status'] else f'{negrito}A matricula do(a) {nomeDoAluno} foi {red}Trancada{reset} com sucesso!{reset}\n'
            print(mensagem)
            voltarAoMenuAluno()
    if not alunoEncontrado:
        print(f'{red}{nomeDoAluno} não foi encontrado em nossa instituição, por favor, digite o nome completo correto.{reset}\n')
    voltarAoMenuAluno()
    


# MENU PROFESSOR ========================================================================================================================================================================
def menuDoProfessor():
    limparTerminal()
    exibirTitulo('ÁREA DO PROFESSOR')
    print(f'''{green}
1. Cadastrar professor.
2. Listar professores.
3. Alternar status do professor.
4. Voltar ao menu de login.{reset}''')

    escolherOpcaoProfessor = int(input(f'{negrito}Escolha uma opção:{reset} '))
    print(f'{negrito}A opção escolhida foi:{reset} {escolherOpcaoProfessor}')
    try:
        if escolherOpcaoProfessor == 1:
            cadastrarProfessor()
        elif escolherOpcaoProfessor == 2:
            listarProfessor()
        elif escolherOpcaoProfessor == 3:
            alternarStatusDoProfessor()
        elif escolherOpcaoProfessor == 4:
            menuLogin()
        else:
            opcaoInvalida()
            sleep(2)
            menuDoProfessor()
    except:
        opcaoInvalida()
        sleep(2)
        menuDoProfessor()

def cadastrarProfessor():
    limparTerminal()
    '''
    Nesta função, pedi ao professor seus dados e fiz uma verificação para aceitar apenas dados válidos
    '''
    exibirTitulo('Cadastrando professor')
    nomeDoProfessor = input(f'{negrito}Nome completo:{reset} ')
    while True:
        idadeDoProfessor = int(input(f'{negrito}Idade do(a) {nomeDoProfessor}:{reset} '))
        if idadeDoProfessor >= 25 and idadeDoProfessor <= 60:
            break
    while True:
        sexoDoProfessor = input(f'{negrito}Genêro [F/M]:{reset} ').title()
        if sexoDoProfessor == 'F' or sexoDoProfessor =='M':
            break
    while True:
        dataDeNascimentoDoProfessor = input(f'{negrito}Digite uma data no formato DD-MM-YYYY:{reset} ')
        try:
            # Tenta converter a string para um objeto datetime
            data = datetime.strptime(dataDeNascimentoDoProfessor, '%d-%m-%Y')
            break
        except:
            # Se a conversão falhar, exibe uma mensagem de erro e pede nova entrada
            print(f'{red}Data inválida. Por favor, digite a data no formato correto (DD-MM-YYYY).{reset}')

    dadosDoProfessor = {'nome': nomeDoProfessor, 'idade': idadeDoProfessor,'sexo': sexoDoProfessor,'dataNascimento': dataDeNascimentoDoProfessor, 'status': False}
    listaDeProfessor.append(dadosDoProfessor)
    print(f'{green}* {nomeDoProfessor} foi cadastrado com sucesso!{reset}\n')
    voltarAoMenuProfessor()

def listarProfessor():
    limparTerminal()
    exibirTitulo('Listando professores')
    print(f'{negrito}{'NOME DO PROFESSOR'.ljust(32)} | {'IDADE'.ljust(30)} | {'GENERO'.ljust(30)} | {'DATA DE NASCIMENTO'.ljust(30)} | {'STATUS'}{reset}')
    for professor in listaDeProfessor:
        nomeDoProfessor = professor['nome']
        idadeDoProfessor = professor['idade']
        sexoDoProfessor = professor['sexo']
        dataNascimentoDoProfessor = professor['dataNascimento']
        statusDoProfessor = f'{green}Ativado{reset}' if professor['status'] else f'{red}Desativado{reset}'
        print(f'{negrito}# {nomeDoProfessor.ljust(30)} | {str(idadeDoProfessor).ljust(30)} | {sexoDoProfessor.ljust(30)} | {dataNascimentoDoProfessor.ljust(30)} | {statusDoProfessor}{reset}')
    voltarAoMenuProfessor()


def alternarStatusDoProfessor():
    limparTerminal()
    exibirTitulo('Alternando status do(a) professor(a)')
    nomeDoProfessor = input('Digite o nome completo do professor que deseja alternar o status: ')
    professorEncontrado = False
    
    for professor in listaDeProfessor:
        if nomeDoProfessor == professor['nome']:
            professorEncontrado = True
            professor['status'] = not professor['status']
            mensagem = f'{negrito}O status do(a) {nomeDoProfessor} foi {green}ativado{reset} com sucesso!{reset}\n' if professor['status'] else f'{negrito}O status do(a) {nomeDoProfessor} foi {red}desativado{reset} com sucesso!{reset}\n'
            print(mensagem)
            voltarAoMenuProfessor()

    if not professorEncontrado:
        print(f'{red}{nomeDoProfessor} não foi encontrado em nossa instituição, por favor, digitar o nome completo correto.{reset}')
        voltarAoMenuProfessor()


# MAIN  ========================================================================================================================================================================
def main():
    limparTerminal()
    menuLogin()

if __name__ == '__main__':
    main()



'''
    CRIAR UM BANCO DE DADOS COM AS SEGUINTES TABELAS:

    Aluno - id, nome, idade, sexo, data
    Professor - id, nome, idade, sexo, data
    LoginAluno = id, usuario, senha
    LoginProfessor = id, usuario, senha
'''
