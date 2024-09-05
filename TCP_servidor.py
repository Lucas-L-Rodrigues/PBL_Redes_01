import socket
import threading
import json
import Rotas.py
import Passagem.py


def buscarObjeto(objeto, bancoDeDados):
    # Carregar o banco de dados
    # Se encontrado
        # retornar True
    # retornar False

def carregarBancoDeDados (bancoDeDados):
    # Abrir o arquivo como leitura
        # retornar o banco de dados

def comprarPassagem(usuario, rota):
    # Buscar usuario
    # Buscar rota
    # Caso tenha numeroAssentos maior que 0
        # diminuir em 1 o numeroAssentos
        # Criar um novo objeto passagem com o usuario e pegando a rota
        # Criar entrada no banco de passagens de um novo objeto 
    # Caso o numeroAssentos seja menor que 1 
        # mensagem de erro

def reservarPassagem(usuario, rota):
    # Buscar usuario
    # Buscar rota
    # Caso numeroAssentos maior que 0
        # Diminuir em 1  numeroAssentos
        # Criar um novo objeto Passagem com o atributo estaPago zerado
    # Caso seja menor que 1
        # mensagem de erro

def pagarReserva (passagem):
    # Buscar a passagem no banco de dados
    # Caso a passagem seja encontrada no banco de dados
        # Marcar estaPago como True
    # Caso nao seja encontrada
        # Mensagem de erro

def cancelarCompra (passagem, rota):
    # Buscar passagem
    # Buscar rota
    # Caso seja encontrada
        # estaCancelado marcado como True
        # numeroAssentos incrementa 1

# NÃO USADA
def carregarUsuarios():
    with open('usuarios.json', 'r') as f:
        return json.load(f)

def verificarLogin(usuario, bancoDeUsuarios):
    login = usuario.get('login')
    senha = usuario.get('senha')

    if (login in bancoDeUsuarios) and (bancoDeUsuarios[login] == senha):
        print('Logado com Sucesso')
        return True
    else:
        print('Login falhou')

    return False

def novoCliente(conn, addr, bancoDeUsuarios):
    print(f'Nova conexão com {addr}')
    
    try:
        while True:
            credenciaisRecebidas = conn.recv(1024).decode('utf-8')
            
            if not credenciaisRecebidas:
                break
            else:
                credenciais = json.loads(credenciaisRecebidas)
                estaLogado = verificarLogin(credenciais, bancoDeUsuarios)
            
            if estaLogado:
                conn.sendall("Logado com sucesso".encode('utf-8'))
                procedimento = menu(conn)
            else:
                conn.sendall("Falha no login".encode('utf-8'))
    finally:
        conn.close()             

# NÃO USADA
def conectar_com_cliente(con, cliente):                     # Função para se comunicar com o cliente para troca de mensagens
    print("Conectado com ", cliente)                        # Ta aqui so pra dar o feedback que a conexao aconteceu
    while True:
        try:
            mensagem = con.recv(1024).decode()              # Recebe e decodifica a mensagem do cliente
            if not mensagem:                                # Se a mensagem for uma string vazia
                break                                       # Sai do loop, sem mensagem sem conexao
            print(f"Cliente {cliente} enviou: \n{mensagem}") # printa a mensagem que recebeu do cliente
        except ConnectionResetError:                        # ta aqui so por desencargo de consciencia mesmo caso alguma coisa aconteca
            print(f"Cliente {cliente} desconectou inesperadamente.")
            break

    print(f"Conexão encerrada com {cliente}.")  # depois de receber a mensagem encerramos a conexao para evitar sobrecarregar o limite do tcp.listen()
    con.close()                                 # Fecha a conexão com o cliente

HOST = ''        # só declarando o host que vai ser usado na tupla "origem" 
PORT = 8000      # Porta que vai ser usada na conexao

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # criando um novo socket usando endereco IPv4 (AF_INET) do tipo stream de dados, ou TCP (SOCK_STREAM), preferi nao arriscar o "fileno"

origem = (HOST, PORT)  # essa tupla "guarda" a informacao do servidor em que se desej conectar e a porta escolhida, usado nas funcoes do socket 
tcp.bind(origem)       # Ligando o socket a origem
tcp.listen(10)         # Escutando até 10 conexões em fila

bancoDeUsuarios = carregarUsuarios()

# Aqui eh a execucao do programa propriamente dita
while True:
    con, cliente = tcp.accept()                     # Aceita uma nova conexão com "cliente"
    print(f"Nova conexão aceita de {cliente}")      # Mensagem para feedback

    thread = threading.Thread(target=novoCliente, args=(con, cliente, bancoDeUsuarios))          # Criando uma nova thread para a conexao com "cliente"
    thread.start()                                                              # Iniciando a thread
    
    print(f'Número de conexões ativas: {threading.active_count() - 1}')         # Mostra o número de threads ativas

print("FIM")  # Esse print nao acontece na pratica, pois nao tem um break no while, mas caso no futuro apliquemos algo depois do fim da execucao.

