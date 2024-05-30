# SGBANK - Sistema de Banco Simples

## Descrição
O SGBANK é um sistema bancário simples desenvolvido em Python usando a biblioteca Tkinter para a interface gráfica e o banco de dados MySQL para armazenar as informações dos clientes e realizar transações financeiras básicas, como criar contas, verificar saldo, depositar, sacar e transferir dinheiro entre contas.

## Requisitos
- Python 3.x
- Bibliotecas: `customtkinter`, `tkinter`, `tkcalendar`, `mysql-connector-python`

## Instalação
1. Instale as bibliotecas necessárias:
    ```bash
    pip install customtkinter tkcalendar mysql-connector-python
    ```
2. Certifique-se de ter um servidor MySQL em execução e ajuste as configurações de conexão no arquivo `banco.py` de acordo com o seu ambiente.

## Como Executar
1. Execute o arquivo `banco.py`:
    ```bash
    python banco.py
    ```
2. A interface gráfica será aberta, permitindo ao usuário interagir com as funcionalidades do sistema bancário.

## Funcionalidades
O SGBANK oferece as seguintes funcionalidades:
- **Criar conta**: Permite que o usuário crie uma nova conta bancária inserindo informações pessoais.
- **Verificar saldo**: Permite que o usuário verifique o saldo da sua conta bancária inserindo o número da conta e a senha.
- **Depositar**: Permite que o usuário deposite dinheiro na sua conta bancária inserindo o número da conta, a senha e o valor a ser depositado.
- **Sacar**: Permite que o usuário saque dinheiro da sua conta bancária inserindo o número da conta, a senha e o valor a ser sacado.
- **Transferir**: Permite que o usuário transfira dinheiro entre contas inserindo o número da sua conta, a senha, o número da conta de destino e o valor a ser transferido.

## Observações
- Este é um sistema bancário de demonstração e pode ser expandido com mais funcionalidades e melhorias de segurança, como autenticação de dois fatores, validação de entrada de dados mais robusta e tratamento de erros mais detalhado.
- Certifique-se de proteger adequadamente suas informações de conexão com o banco de dados e considere usar um servidor MySQL remoto seguro para produção.
- Este sistema foi desenvolvido como um projeto de aprendizado e pode não atender a todos os requisitos de segurança e conformidade necessários para implantação em um ambiente de produção.
