import string
final = []
e_final = ''


# função para verificar o nome:
def checknome(nome):
    letras = 0
    espacos = 0
    for c in nome:  # por cada letra no nome
        if c == ' ':  # se o carater for espaço, incrementa a respetiva variável
            espacos += 1
            continue  # e segue para a próxima iteração
        for l in string.ascii_letters:  # comparar cada letra do nome com letra do abecedário
            if c == l:  # se tiver correspondência
                letras += 1  # incrementa a respetiva variável
# se sum(letras,espacos)= comprimento da string e os espaços<letras
    if letras+espacos == len(nome) and espacos < letras:
        return True
    else:
        return False


# função para verificar o e-mail:
def checkmail(mail):
    if mail.count('@')!=1:  # se a ocorrência de @ não for 1
        print('Email invalido, precisa conter um e apenas um "@"')
        return False
    else:
        m = mail.split('@', 1)  # divide em 2 pela @
# verificação da 1a parte do endereço:
        if ' ' in m[0] or len(m[0]) <= 1:
            print("O endereco nao pode conter espacos e tem de ter mais que 1 carater")
            return False
        for c in string.punctuation:
            if m[0].startswith(c) or m[0].endswith(c):
                print('Email inválido, não pode começar nem terminar por carateres especiais')
                return False
# verificação da 2a parte do endereço (o lado do servidor)
        if m[1].count('.')==1 and not m[1].startswith('.') and not m[1].endswith('.'):
            servidor = m[1].split('.')  # divide em 2 pelo ponto
# se forem todos letras
            if servidor[0].isalpha() and servidor[1].isalpha():
                if int(len(servidor[0])) < 3:
                    print("Nome do servidor pequeno demais")
                    return False
                if int(len(servidor[1])) > 1 and int(len(servidor[1]) < 4):
                    return True
        else:
            print("Servidor incorreto")
            return False


if __name__ == '__main__':
    while True:
        nome=input("Introduza o seu nome: ")
        if not checknome(nome):
            print(f"Nome \"{nome}\" invalido")
        else:
            print(f"Nome aceite\n{nome} registado com sucesso")
            break
    while True:
        mail=input("Introduza o seu mail: ")
        if not checkmail(mail):
            print(f"Email introduzido:\n\"{mail}\" invalido")
        else:
            break
    final = mail.split('@')
    final[1] = final[1].lower()
    e_final += final[0]
    e_final += '@'
    e_final += final[1]
    print(f"Email aceite\n{e_final} registado com sucesso")
