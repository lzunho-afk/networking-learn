# Redes de Computadores com Python

## Programação Cliente-Servidor - client_server

- [hostname.py](./client_server/hostname.py): Apresenta o nome da máquina rodando a instância.
- [external_host_addr.py](./client_server/external_host_addr.py): Apresenta o endereço IP a partir de um hostname.
- [ip_convert.py](./client_server/ip_convert.py): Converte o endereço de IPv4 para hexadecimal (empacotamento).
- [service_name.py](./client_server/service_name.py): Devolve o nome do serviço rodando no endereço e porta especificados.
- [get_http.py](./client_server/get_http.py): Solicita um arquivo de um servidor HTTP (GET).
- [change_sock_buffsize.py](./client_server/change_sock_buffsize.py): Altera o valor padrão de buffer do socket utilizando `setsockopt()`, que recebe três argumentos de entrada, o `level` (constante do socket), o `optname` (nome da opção) e o `value` (valor correspondente).
- [cg_blocking_mode.py](./client_server/cg_blocking_mode.py): Altera o modo do socket para `non-blocking`. A necessidade disso pode se dar pelo fato de que os sockets TCP são configurados por padrão em modo de bloqueio (`blocking`), o que significa que o controle não é retornado para o programa até que determinada operação tenha terminado.
- [addr_reuse.py](./client_server/addr_reuse.py): Reusa o endereço utilizado (mesma porta)
- [ntp_print.py](./client_server/ntp_print.py): Utiliza o módulo ntplib para fazer uma requisição para um servidor NTP (Network Time Protocol).
- [echo_server.py](./client_server/echo_server.py) / [echo_client.py](./client_server/echo_client.py): Cliente e Servidor simples - Exemplo mais clássico de client-server

## Multiplexing - Transmissão Simuntânea (I/O

- [echo_multiclient_server.py](./multiplexing/echo_multiclient_server.py): Servidor ECHO com suporte para multiplos clientes através do método "ForkingMixIn".
