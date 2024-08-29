import socket

HOST = '127.0.0.1' # Endereço padrao do servidor
PORT = 8000      # Porta inicial

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # OBS: usando o TCP/IP4


#user_input1 = input("Qual eh o endereço IP do servidor que voce quer se conectar?\n")
#if user_input1 != '': # Caso o usuario coloque algum valor de endereço IP
#    HOST = user_input1 # substitui o valor do servidor pelo servidor escolhido

#user_input2 = input("Em qual porta voce deseja se conectar?\n")
#if user_input2 != '':
#    PORT = int(user_input2) # substitui a porta em que se conectar

servidor = (HOST, PORT) # passando o servidor e a porta a se conectar como uma tupla
tcp.connect(servidor)   # realizando a conexao


mensagem = input("\nQual mensagem que voce quer enviar?\nDigite SAIR para sair\n\n")
while mensagem != "SAIR":
    tcp.send(str.encode(mensagem)) # envia a mensagem
    mensagem = input ("Qual eh a proxima mensagem?\nDigite SAIR para sair\n\n")

tcp.close() # finalizando a conexao
