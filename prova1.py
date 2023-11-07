email = "meuemail@hotmail.com"
senha = "senha123456"

while True:
    email_usuario = input("Digite seu email: ")
    senha_usuario = input("Digite sua senha: ")

    if email_usuario == email and senha_usuario == senha:
        print("Login bem-sucedido!")
        break 
    else:
        print("Email ou senha incorretos. Tente novamente.")
