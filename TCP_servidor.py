import socket
import threading
import json

def verificarLogin(login, senha, usuarios):
    for usuario in usuarios:
        if (usuario['login']==login and usuario['senha']==senha):
            return True
    return False

def novoCliente(conn, addr):
    print(f'Nova conexão com {addr}')
    
    while True:
        try:
            credenciais = conn.recv(1024)  # Recebe dados
            if not credenciais:
                break               # Sai do loop se o cliente não enviar nada, no caso digitando SAIR no TCP_Cliente

            print(f'{addr} mandou: {credenciais.decode()}\n')   # Mensagem de confirmação
            conn.sendall(b'O servidor recebeu as informacoes.')  # Envia resposta ao cliente

        except ConnectionResetError:
            break                       # Sai do loop se a conexão for resetada

    conn.close()                        # Fecha a conexão ao sair do loop
    print(f'Conexão encerrada: {addr}')

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

tcp.listen(10)         # Escutando até 10 conexões em fila

# Aqui eh a execucao do programa propriamente dita
while True:
    con, cliente = tcp.accept()                     # Aceita uma nova conexão com "cliente"
    print(f"Nova conexão aceita de {cliente}")      # Mensagem para feedback

    thread = threading.Thread(target=novoCliente, args=(con, cliente))          # Criando uma nova thread para a conexao com "cliente"
    thread.start()                                                              # Iniciando a thread

    print(f'Número de conexões ativas: {threading.active_count() - 1}')         # Mostra o número de threads ativas

print("FIM")  # Esse print nao acontece na pratica, pois nao tem um break no while, mas caso no futuro apliquemos algo depois do fim da execucao.

