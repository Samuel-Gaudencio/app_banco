# App Banco (Versão 1.0)

Este é um aplicativo de banco simples desenvolvido em Python com a biblioteca Tkinter para a interface gráfica e Excel como banco de dados. Por favor, note que esta é a versão 1.0 e uma versão mais avançada está em desenvolvimento.

## Funcionalidades

- **Criar Conta:** Ao selecionar "Criar conta", o usuário pode inserir seu nome, sobrenome, data de nascimento, CPF e senha para criar uma nova conta bancária. Cada conta criada recebe um número de conta único e um saldo inicial de R$ 100,00.
- **Consultar Extrato:** Ao selecionar "Extrato", o usuário deve inserir seu número de conta e senha para consultar o saldo da conta.
- **Depositar:** Ao selecionar "Depositar", o usuário deve inserir seu número de conta e o valor que deseja depositar.
- **Sacar:** Ao selecionar "Sacar", o usuário deve inserir seu número de conta, senha e o valor que deseja sacar. O saque só é permitido se houver saldo suficiente na conta.
- **Transferir:** Ao selecionar "Transferir", o usuário deve inserir seu número de conta, senha, o número da conta de destino e o valor que deseja transferir. A transferência só é permitida se houver saldo suficiente na conta de origem.


## Requisitos

- Python 3.x
- Biblioteca Tkinter
- Biblioteca openpyxl (para trabalhar com arquivos Excel)

## Como Executar

1. Certifique-se de ter o Python instalado.<br>
Você pode baixá-lo em [python.org](https://www.python.org/).

2. Instale a biblioteca openpyxl usando o seguinte comando:<br>
pip install openpyxl

3. Clone este repositório:<br>
git clone https://github.com/Samuel-Gaudencio/app_banco.git

4. Navegue até o diretório do projeto:<br>
cd app_banco

5. Execute o aplicativo:<br>
python main.py


## Estrutura do Código
main.py: Contém a lógica principal do programa, incluindo a definição das classes para criar a interface gráfica e gerenciar as operações bancárias.<br>
cadastros.xlsx: Arquivo Excel utilizado como banco de dados para armazenar informações das contas bancárias, como número da conta, nome, sobrenome, data de nascimento, CPF, senha e saldo.

## Notas Adicionais
O sistema utiliza a biblioteca CustomTkinter para criar uma interface gráfica amigável e personalizada.<br>
As informações das contas são armazenadas no arquivo cadastros.xlsx.<br>
É importante garantir que o arquivo cadastros.xlsx esteja presente no mesmo diretório que o arquivo main.py para que o programa funcione corretamente.
