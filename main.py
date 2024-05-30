from datetime import date
import customtkinter as ctk  # Módulo personalizado para estilização da interface
import tkinter  # Biblioteca para criar interfaces gráficas
from tkcalendar import DateEntry  # Widget de calendário para seleção de datas
import mysql.connector  # Módulo para interagir com o banco de dados MySQL

# Estabelecendo a conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='banco'
)


class BancoApp:
    def __init__(self, root):
        # Configurações iniciais da janela principal
        self.root = root
        self.root.title('SGBANK')  # Título da janela
        self.root.geometry('400x300')  # Tamanho da janela
        self.root.minsize(500, 400)  # Tamanho mínimo da janela
        self.root.maxsize(500, 400)  # Tamanho máximo da janela
        self.initialize_ui()  # Inicialização da interface do usuário
        ctk.set_appearance_mode('dark')  # Configuração do modo de aparência (dark)


    def initialize_ui(self):
        # Função para adicionar margem entre os elementos da interface
        self.margin(30)

        # Título da aplicação
        title = ctk.CTkLabel(self.root, text='Bem-vindo ao SGBANK', text_color='#fff', font=('Montserrat', 26, 'bold'))
        title.pack()

        self.margin(5)  # Margem entre elementos
        # Subtítulo
        subtitle = ctk.CTkLabel(self.root, text='O que deseja fazer?', text_color='#fff',
                                font=('Montserrat', 20, 'bold'))
        subtitle.pack()

        # Botões para as funcionalidades principais
        self.margin(20)
        create_user = ctk.CTkButton(self.root, text='Criar conta', text_color='#fff', font=('Montserrat', 20, 'bold'),
                                    command=self.janela_user)  # Botão para criar conta
        create_user.pack()

        self.margin(20)
        extrato = ctk.CTkButton(self.root, text='Saldo', text_color='#fff', font=('Montserrat', 20, 'bold'),
                                command=self.janela_extrato)  # Botão para verificar saldo
        extrato.pack()

        self.margin(20)
        depositar = ctk.CTkButton(self.root, text='Depositar', text_color='#fff', font=('Montserrat', 20, 'bold'),
                                  command=self.janela_depositar)  # Botão para depositar
        depositar.pack()

        self.margin(20)
        sacar = ctk.CTkButton(self.root, text='Sacar', text_color='#fff', font=('Montserrat', 20, 'bold'),
                              command=self.janela_sacar)  # Botão para sacar
        sacar.pack()

        self.margin(20)
        transferir = ctk.CTkButton(self.root, text='Transferir', text_color='#fff', font=('Montserrat', 20, 'bold'),
                                   command=self.janela_transferir)  # Botão para transferir
        transferir.pack()


    def margin(self, height):
        # Adiciona margem entre os elementos da interface
        margem = ctk.CTkCanvas(self.root, highlightthickness=0, height=height, background='#242424')
        margem.pack()

    # Funções para abrir janelas secundárias
    def janela_user(self):
        criar_conta_app = CriarContaApp(self)
        self.root.wait_window(criar_conta_app.ja_user)

    def janela_extrato(self):
        extrato_app = ExtratoApp(self)
        self.root.wait_window(extrato_app.ja_extrato)

    def janela_depositar(self):
        depositar_app = DepositarApp(self)
        self.root.wait_window(depositar_app.ja_depo)

    def janela_transferir(self):
        transferir_app = TransferirApp(self)
        self.root.wait_window(transferir_app.ja_transferir)

    def janela_sacar(self):
        sacar_app = SacarApp(self)
        self.root.wait_window(sacar_app.ja_sacar)


class CriarContaApp:
    def __init__(self, parent):
        self.parent = parent
        # Configurações da janela
        self.ja_user = ctk.CTkToplevel(parent.root)
        self.ja_user.geometry('400x400')
        self.ja_user.title('Criar Conta')
        self.ja_user.maxsize(500, 400)
        self.ja_user.minsize(500, 400)
        self.ja_user.focus_force()
        self.ja_user.grab_set()

        self.initialize_ui() # Inicialização da interface do usuário

    def initialize_ui(self):
        # Configurações dos elementos da interface
        titulo = ctk.CTkLabel(self.ja_user, text='Criar conta', text_color='#fff',
                              font=('Montserrat', 26, 'bold'))
        titulo.pack(pady=30)

        label_nome = ctk.CTkLabel(self.ja_user, text='Informe seu nome:', text_color='#fff',
                                  font=('Montserrat', 18, 'bold'))
        label_nome.place(x=30, y=90)

        self.entry_nome = ctk.CTkEntry(self.ja_user, placeholder_text='Insira seu nome', placeholder_text_color='#fff',
                                       font=('Montserrat', 12, 'bold'), fg_color='transparent')
        self.entry_nome.place(x=200, y=90)

        label_sobrenome = ctk.CTkLabel(self.ja_user, text='Informe seu sobrenome:', text_color='#fff',
                                       font=('Montserrat', 18, 'bold'))
        label_sobrenome.place(x=30, y=130)

        self.entry_sobrenome = ctk.CTkEntry(self.ja_user, placeholder_text='Insira seu sobrenome', placeholder_text_color='#fff',
                                            font=('Montserrat', 12, 'bold'), fg_color='transparent')
        self.entry_sobrenome.place(x=250, y=130)

        label_nascimento = ctk.CTkLabel(self.ja_user, text='Informe sua data de nascimento:', text_color='#fff',
                                        font=('Montserrat', 18, 'bold'))
        label_nascimento.place(x=30, y=170)

        self.entry_nascimento = DateEntry(self.ja_user, selectmode='day', date_pattern='yyyy-mm-dd', locale='pt_BR',
                                          font=('Montserrat', 12, 'bold'), background='#242424', foreground='#fff',
                                          normalbackground='#242424', headersbackground='#242424', weekendbackground='#242424',
                                          normalforeground='#fff', headersforeground='#fff', weekendforeground='#fff',
                                          maxdate=date(2006, 12, 31))
        self.entry_nascimento.place(x=320, y=170)

        label_cpf = ctk.CTkLabel(self.ja_user, text='Informe seu CPF:', text_color='#fff',
                                 font=('Montserrat', 18, 'bold'))
        label_cpf.place(x=30, y=210)

        self.entry_cpf = ctk.CTkEntry(self.ja_user, placeholder_text=' 000.000.000-00 ', placeholder_text_color='#fff',
                                      font=('Montserrat', 12, 'bold'), fg_color='transparent')
        self.entry_cpf.place(x=185, y=210)

        label_senha = ctk.CTkLabel(self.ja_user, text='Crie sua senha(com 4 digitos): ', text_color='#fff',
                                   font=('Montserrat', 18, 'bold'))
        label_senha.place(x=30, y=250)

        self.entry_senha = ctk.CTkEntry(self.ja_user, placeholder_text=' **** ', placeholder_text_color='#fff',
                                        font=('Montserrat', 12, 'bold'), fg_color='transparent', show='*')
        self.entry_senha.place(x=300, y=250)

        button_criar = ctk.CTkButton(self.ja_user, text='Criar Conta', text_color='#fff', font=('Montserrat', 18, 'bold'),
                                     command=self.criar_conta)
        button_criar.place(x=175, y=300)

    def criar_conta(self):
        # Função para criar uma nova conta no banco de dados
        nome = self.entry_nome.get()
        sobrenome = self.entry_sobrenome.get()
        data = self.entry_nascimento.get_date().strftime('%Y-%m-%d')
        cpf = self.entry_cpf.get()
        senha = self.entry_senha.get()
        saldo = 1000 # Saldo inicial da conta

        if nome == "" or sobrenome == "" or data == "" or cpf == "" or senha == "":
            # Verifica se todos os campos foram preenchidos
            tkinter.messagebox.showwarning('Sistema', "ERROR\nPor favor prenchar todos os campos!!")
            self.entry_nome.delete(0, tkinter.END)
            self.entry_sobrenome.delete(0, tkinter.END)
            self.entry_nascimento.delete(0, tkinter.END)
            self.entry_cpf.delete(0, tkinter.END)
            self.entry_senha.delete(0, tkinter.END)

        else:
            # Insere os dados da nova conta no banco de dados
            cursor = conexao.cursor()
            comando = (f"INSERT INTO cliente (nome, sobrenome, data_nasc, cpf, senha, saldo) VALUES "
                       f"('{nome}', '{sobrenome}', '{data}', "
                       f"'{cpf}', {int(senha)}, {int(saldo)})")
            cursor.execute(comando)
            conexao.commit()
            # Recupera o número da conta recém-criada
            conta = cursor.lastrowid

            tkinter.messagebox.showinfo('Sistema', f"Conta criada com sucesso!! \nO numero da sua conta é {conta}"
                                                   f"\n Você ganhou um saldo de R$: 1.000,00 por cadastrar!!")
            # Limpa os campos após a criação da conta
            self.entry_nome.delete(0, tkinter.END)
            self.entry_sobrenome.delete(0, tkinter.END)
            self.entry_nascimento.delete(0, tkinter.END)
            self.entry_cpf.delete(0, tkinter.END)
            self.entry_senha.delete(0, tkinter.END)

            cursor.close()

            


class ExtratoApp:
    def __init__(self, parent):
        # Inicialização da janela para exibir o extrato
        self.parent = parent
        self.ja_extrato = ctk.CTkToplevel(parent.root)
        self.ja_extrato.geometry('400x300')
        self.ja_extrato.title('Extrato')
        self.ja_extrato.maxsize(500, 300)
        self.ja_extrato.minsize(500, 300)
        self.ja_extrato.focus_force()
        self.ja_extrato.grab_set()

        self.initialize_ui()

    def initialize_ui(self):
        # Interface gráfica para exibir o extrato
        titulo = ctk.CTkLabel(self.ja_extrato, text='Saldo', text_color='#fff',
                              font=('Montserrat', 26, 'bold'))
        titulo.pack(pady=30)

        label_conta = ctk.CTkLabel(self.ja_extrato, text='Informe o numero da sua conta: ', text_color='#fff',
                                   font=('Montserrat', 17, 'bold'))
        label_conta.place(x=30, y=90)

        self.entry_conta = ctk.CTkEntry(self.ja_extrato, placeholder_text='Insira a conta', placeholder_text_color='#fff',
                                   font=('Montserrat', 12, 'bold'), fg_color='transparent')
        self.entry_conta.place(x=290, y=90)

        label_senha = ctk.CTkLabel(self.ja_extrato, text='Informe a senha: ', text_color='#fff',
                                   font=('Montserrat', 17, 'bold'))
        label_senha.place(x=30, y=130)

        self.entry_senha = ctk.CTkEntry(self.ja_extrato, placeholder_text='Insira a senha', placeholder_text_color='#fff',
                                        font=('Montserrat', 12, 'bold'), fg_color='transparent', show='*')
        self.entry_senha.place(x=170, y=130)

        extrato_button = ctk.CTkButton(self.ja_extrato, text='Verificar saldo', text_color='#fff',
                                       font=('Montserrat', 18, 'bold'), width=30, command=self.extrato)
        extrato_button.place(x=170, y=180)

        self.label_extrato = ctk.CTkLabel(self.ja_extrato, text='', text_color='#fff',
                                          font=('Montserrat', 24, 'bold'))
        self.label_extrato.place(x=100, y=240)


    def extrato(self):
        # Função para exibir o saldo na interface gráfica
        e_conta = self.entry_conta.get()
        e_senha = self.entry_senha.get()

        if e_conta == "" or e_senha == "":
            self.label_extrato.configure(text='')
            tkinter.messagebox.showwarning('Sistema', "ERROR\nPor favor prenchar todos os campos!!")
        else:

            cursor = conexao.cursor()
            comando = (f"SELECT * FROM cliente WHERE conta = {e_conta};")
            cursor.execute(comando)
            result = cursor.fetchall()

            if result != []:
                if str(result[0][4]) == str(e_senha):
                    self.label_extrato.configure(text=f'Seu saldo é de R${result[0][5]:.2f}')
                    cursor.close()
                else:
                    self.label_extrato.configure(text='')
                    tkinter.messagebox.showwarning('Sistema', "ERROR\nSenha invalida!!")
            else:
                self.label_extrato.configure(text='')
                tkinter.messagebox.showwarning('Sistema', "ERROR\nConta invalida!!")

            
            


class DepositarApp:
    def __init__(self, parent):
        # Inicialização da janela para fazer depósito
        self.parent = parent
        self.ja_depo = ctk.CTkToplevel(parent.root)
        self.ja_depo.geometry('500x250')
        self.ja_depo.title('Depositar')
        self.ja_depo.maxsize(500, 250)
        self.ja_depo.minsize(500, 250)
        self.ja_depo.focus_force()
        self.ja_depo.grab_set()

        self.initialize_ui()

    def initialize_ui(self):
        # Interface gráfica para fazer depósito
        titulo = ctk.CTkLabel(self.ja_depo, text='Depositar', text_color='#fff',
                              font=('Montserrat', 26, 'bold'))
        titulo.pack(pady=30)

        label_conta = ctk.CTkLabel(self.ja_depo, text='Informe o numero da sua conta: ', text_color='#fff',
                                   font=('Montserrat', 17, 'bold'))
        label_conta.place(x=30, y=90)

        self.entry_conta = ctk.CTkEntry(self.ja_depo, placeholder_text='Insira a conta', placeholder_text_color='#fff',
                                   font=('Montserrat', 12, 'bold'), fg_color='transparent')
        self.entry_conta.place(x=290, y=90)

        label_valor = ctk.CTkLabel(self.ja_depo, text='Informe o valor do deposito: ', text_color='#fff',
                                   font=('Montserrat', 17, 'bold'))
        label_valor.place(x=30, y=130)

        self.entry_valor = ctk.CTkEntry(self.ja_depo, placeholder_text='Insira o valor', placeholder_text_color='#fff',
                                   font=('Montserrat', 12, 'bold'), fg_color='transparent')
        self.entry_valor.place(x=260, y=130)

        deposito_button = ctk.CTkButton(self.ja_depo, text='Fazer deposito', text_color='#fff',
                                        font=('Montserrat', 18, 'bold'),
                                        width=30, command=self.deposito)
        deposito_button.place(x=170, y=180)

    def deposito(self):
        # Função para realizar um depósito na conta
        e_conta = self.entry_conta.get()
        e_valor = self.entry_valor.get()


        if e_conta == "" or e_valor == "":
            tkinter.messagebox.showwarning('Sistema', "ERROR\nPor favor prenchar todos os campos!!")
        else:

            cursor = conexao.cursor()
            comando = (f"SELECT * FROM cliente WHERE conta = {e_conta};")
            cursor.execute(comando)
            result = cursor.fetchall()
            
            if result != []:
                if int(e_conta) == int(result[0][0]):
                    if float(e_valor) > 0:

                        comando = (f"UPDATE cliente SET saldo = {result[0][5] + float(e_valor)} WHERE conta = {e_conta};")
                        cursor.execute(comando)
                        conexao.commit()
                        cursor.close()
                        tkinter.messagebox.showwarning('Sistema', "Deposito realizado com sucesso!!")
                        self.entry_conta.delete(0, tkinter.END)
                        self.entry_valor.delete(0, tkinter.END)
                    else:
                        tkinter.messagebox.showwarning('Sistema', "ERROR\nValor invalido!!")
            else:
                tkinter.messagebox.showwarning('Sistema', "ERROR\nConta invalida!!")
            
            
            



class TransferirApp:
    def __init__(self, parent):
        # Inicialização da janela para fazer uma trasferência entre contas.
        self.parent = parent
        self.ja_transferir = ctk.CTkToplevel(parent.root)
        self.ja_transferir.geometry('500x350')
        self.ja_transferir.title('Transferir')
        self.ja_transferir.maxsize(500, 350)
        self.ja_transferir.minsize(500, 350)
        self.ja_transferir.focus_force()
        self.ja_transferir.grab_set()

        self.initialize_ui()

    def initialize_ui(self):
        # Interface gráfica para fazer uma trasferência entre contas.
        titulo = ctk.CTkLabel(self.ja_transferir, text='Transferir', text_color='#fff',
                              font=('Montserrat', 26, 'bold'))
        titulo.pack(pady=30)

        label_conta = ctk.CTkLabel(self.ja_transferir, text='Informe o numero da sua conta: ', text_color='#fff',
                                   font=('Montserrat', 17, 'bold'))
        label_conta.place(x=30, y=90)

        self.entry_conta = ctk.CTkEntry(self.ja_transferir, placeholder_text='Insira a conta', placeholder_text_color='#fff',
                                   font=('Montserrat', 12, 'bold'), fg_color='transparent')
        self.entry_conta.place(x=290, y=90)

        label_senha = ctk.CTkLabel(self.ja_transferir, text='Informe a senha: ', text_color='#fff',
                                   font=('Montserrat', 17, 'bold'))
        label_senha.place(x=30, y=130)

        self.entry_senha = ctk.CTkEntry(self.ja_transferir, placeholder_text='Insira a senha', placeholder_text_color='#fff',
                                   font=('Montserrat', 12, 'bold'), fg_color='transparent', show='*')
        self.entry_senha.place(x=170, y=130)

        label_conta2 = ctk.CTkLabel(self.ja_transferir, text='Informe o numero da outra conta: ', text_color='#fff',
                                    font=('Montserrat', 17, 'bold'))
        label_conta2.place(x=30, y=170)

        self.entry_conta2 = ctk.CTkEntry(self.ja_transferir, placeholder_text='Insira a outra conta',
                                    placeholder_text_color='#fff',
                                    font=('Montserrat', 12, 'bold'), fg_color='transparent')

        self.entry_conta2.place(x=300, y=170)

        label_valor = ctk.CTkLabel(self.ja_transferir, text='Informe o valor da transferência: ', text_color='#fff',
                                   font=('Montserrat', 17, 'bold'))
        label_valor.place(x=30, y=210)

        self.entry_valor = ctk.CTkEntry(self.ja_transferir, placeholder_text='Insira o valor', placeholder_text_color='#fff',
                                   font=('Montserrat', 12, 'bold'), fg_color='transparent')
        self.entry_valor.place(x=290, y=210)

        transferir_button = ctk.CTkButton(self.ja_transferir, text='Fazer transferência', text_color='#fff',
                                          font=('Montserrat', 18, 'bold'), command=self.transferir)
        transferir_button.place(x=160, y=260)

    def transferir(self):
        # Função para realizar uma trasferência entre contas.
        e_conta = self.entry_conta.get()
        e_conta2 = self.entry_conta2.get()
        e_senha = self.entry_senha.get()
        e_valor = self.entry_valor.get()


        if e_conta == "" or e_conta2 == "" or e_valor == "" or e_senha == "":
            tkinter.messagebox.showwarning('Sistema', "ERROR\nPor favor prenchar todos os campos!!")
        else:
            cursor = conexao.cursor()
            comando1 = (f"SELECT * FROM cliente WHERE conta = {e_conta};")
            comando2 = (f"SELECT * FROM cliente WHERE conta = {e_conta2};")
            cursor.execute(comando1)
            conta1 = cursor.fetchall()
            cursor.execute(comando2)
            conta2 = cursor.fetchall()


            if conta1 != []:
                if conta2 != []:
                    if int(e_conta) != int(e_conta2):
                        if int(conta1[0][4]) == int(e_senha):
                            if float(e_valor) != 0:
                                if float(e_valor) <= float(conta1[0][5]):
                                    
                                    comando = (f"UPDATE cliente SET saldo = {conta2[0][5] + float(e_valor)} WHERE conta = {e_conta2};")
                                    cursor.execute(comando)
                                    conexao.commit()
                                    cursor.close()

                                    tkinter.messagebox.showwarning('Sistema', "Tranferencia realizada com sucesso!!")
                                    
                                    self.entry_conta.delete(0, tkinter.END)
                                    self.entry_conta2.delete(0, tkinter.END)
                                    self.entry_senha.delete(0, tkinter.END)
                                    self.entry_valor.delete(0, tkinter.END)
                                else:
                                    tkinter.messagebox.showwarning('Sistema',
                                                                   "ERROR\nVocê não tem saldo para realizar a transferencia!!")
                            else:
                                tkinter.messagebox.showwarning('Sistema', "ERROR\nValor invalido!!")
                        else:
                            tkinter.messagebox.showwarning('Sistema', "ERROR\nSenha invalida!!")
                    else:
                        tkinter.messagebox.showwarning('Sistema',
                                                       "ERROR\nVocê não poder transferir para sua propria conta!!")
                else:
                    tkinter.messagebox.showwarning('Sistema', "ERROR\nConta que deseja transferir esta invalida!!")
            else:
                tkinter.messagebox.showwarning('Sistema', "ERROR\nConta invalida!!")


class SacarApp:

    def __init__(self, parent):
        # Inicialização da janela para fazer saque
        self.parent = parent
        self.ja_sacar = ctk.CTkToplevel(parent.root)
        self.ja_sacar.geometry('450x300')
        self.ja_sacar.title('Sacar')
        self.ja_sacar.maxsize(450, 300)
        self.ja_sacar.minsize(450, 300)
        self.ja_sacar.focus_force()
        self.ja_sacar.grab_set()

        self.initialize_ui()

    def initialize_ui(self):
        # Interface gráfica para fazer saque
        titulo = ctk.CTkLabel(self.ja_sacar, text='Sacar', text_color='#fff',
                              font=('Montserrat', 26, 'bold'))
        titulo.pack(pady=30)

        label_conta = ctk.CTkLabel(self.ja_sacar, text='Informe o numero da sua conta: ', text_color='#fff',
                                   font=('Montserrat', 17, 'bold'))
        label_conta.place(x=30, y=90)

        self.entry_conta = ctk.CTkEntry(self.ja_sacar, placeholder_text='Insira a conta', placeholder_text_color='#fff',
                                        font=('Montserrat', 12, 'bold'), fg_color='transparent')
        self.entry_conta.place(x=290, y=90)

        label_senha = ctk.CTkLabel(self.ja_sacar, text='Informe a senha: ', text_color='#fff',
                                   font=('Montserrat', 17, 'bold'))
        label_senha.place(x=30, y=130)

        self.entry_senha = ctk.CTkEntry(self.ja_sacar, placeholder_text='Insira a senha', placeholder_text_color='#fff',
                                        font=('Montserrat', 12, 'bold'), fg_color='transparent', show='*')
        self.entry_senha.place(x=170, y=130)

        label_valor = ctk.CTkLabel(self.ja_sacar, text='Informe o valor do saque: ', text_color='#fff',
                                   font=('Montserrat', 17, 'bold'))
        label_valor.place(x=30, y=170)

        self.entry_valor = ctk.CTkEntry(self.ja_sacar, placeholder_text='Insira o valor', placeholder_text_color='#fff',
                                        font=('Montserrat', 12, 'bold'), fg_color='transparent')
        self.entry_valor.place(x=240, y=170)

        sacar_button = ctk.CTkButton(self.ja_sacar, text='Fazer saque', text_color='#fff',
                                     font=('Montserrat', 18, 'bold'), command=self.saque)
        sacar_button.place(x=160, y=220)

    def saque(self):
        # Função para realizar um saque na conta
        e_conta = self.entry_conta.get()
        e_valor = self.entry_valor.get()
        e_senha = self.entry_senha.get()


        if e_conta == "" or e_valor == "" or e_senha == "":
            tkinter.messagebox.showwarning('Sistema', "ERROR\nPor favor prenchar todos os campos!!")
        else:

            cursor = conexao.cursor()
            comando = (f"SELECT * FROM cliente WHERE conta = {e_conta};")
            cursor.execute(comando)
            result = cursor.fetchall()
            
            if result != []:
                if int(result[0][4]) == int(e_senha):
                    if float(e_valor) != 0:
                        if float(e_valor) <= result[0][5]:

                            # Atualiza os saldos no banco de dados
                            comando = (f"UPDATE cliente SET saldo = {result[0][5] - float(e_valor)} WHERE conta = {e_conta}")
                            cursor.execute(comando)
                            conexao.commit()
                            cursor.close()

                            tkinter.messagebox.showwarning('Sistema', "Saque realizado com sucesso!!")
                            
                            self.entry_conta.delete(0, tkinter.END)
                            self.entry_senha.delete(0, tkinter.END)
                            self.entry_valor.delete(0, tkinter.END)
                        else:
                            tkinter.messagebox.showwarning('Sistema',
                                                           "ERROR\nVocê não tem saldo suficiente para realizar o saque!!")
                    else:
                        tkinter.messagebox.showwarning('Sistema', "ERROR\nValor invalido!!")
                else:
                    tkinter.messagebox.showwarning('Sistema', "ERROR\nSenha invalida!!")
            else:
                tkinter.messagebox.showwarning('Sistema', "ERROR\nConta invalida!!")



    
# Inicializa a aplicação
if __name__ == "__main__":
    root = ctk.CTk()
    app = BancoApp(root)
    root.mainloop()
    conexao.close()
