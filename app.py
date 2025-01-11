import customtkinter as ctk
# Configuração para deixar no modo claro ou escuro(usando dark/light)
ctk.set_appearance_mode('dark')

#Criando as funções de funcinalidades
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    #verificar se o usuario é gabriel e a senha 1234
    if usuario == "gabriel" and senha == '1234':
        resultado_login.configure(text = 'Login feito com sucesso!',text_color = 'green')
    else:
        resultado_login.configure(text = 'Login incorreto!', text_color = 'red')

#Criando a janela principal
app = ctk.CTk()
app.title('login Haen')
app.geometry('300x300')
# Criação dos campos(label entry button)
#parte de usuário
label_usuario = ctk.CTkLabel(app, text='Usuário:')
label_usuario.pack(pady = 10)
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady = 10)
#parte de senha
label_senha = ctk.CTkLabel(app,text='Senha:' )
label_senha.pack(pady = 10)
campo_senha = ctk.CTkEntry(app,placeholder_text='Digite sua senha', show = '*' )
campo_senha.pack(pady = 10)
#Login
login = ctk.CTkButton(app, text='Login', command=validar_login)
login.pack(pady = 10)
#campo feedback de login
resultado_login = ctk.CTkLabel(app, text = '')
resultado_login.pack(pady = 5)
#Inicialização
app.mainloop()