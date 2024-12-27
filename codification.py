from encoder import *

def encriptando():
    print("Agora Digite uma senha e codificador para alterar a criptografia! ")
    senha = str(input("Digite sua senha: ").lower())
    encodingHash = str(input("Digite seu codificador: ").lower())
    
    countSenha = len(senha) * 2
    senha = senha + senha
    countHash = len(encodingHash)
    if(countSenha > countHash):
        for i in range(countSenha-countHash):
            encodingHash = encodingHash + encodingHash[i]
    elif(countSenha < countHash):
        for i in range(countHash-countSenha):
            j = countHash-countSenha
            encodingHash = encodingHash - encodingHash[j]
            j -= 1
    
    k = 0
    flag = [0, 0]
    hashing()
    with open('senha.txt', 'w', encoding='utf8') as file:
        for m in range(len(encodingHash)):
            for i in range(36):
                cpr = transHash[i][0]
                flag[0] = i
                if(cpr == senha[k]):
                    for j in range(36):
                        cmp = transHash[0][j]
                        flag[1] = j
                        if(cmp == encodingHash[k]):
                            file.write(f'{transHash[flag[0]][0]}{transHash[0][flag[1]]}{transHash[flag[0]][flag[1]]}')
            k += 1

def testarSenha():
    print("Vamos verificar seu login!")
    senha = str(input("Digite sua senha: ").lower())
    encodingHash = str(input("Digite seu codificador: ").lower())
    
    countSenha = len(senha) * 2
    senha = senha + senha
    countHash = len(encodingHash)
    if(countSenha > countHash):
        for i in range(countSenha-countHash):
            encodingHash = encodingHash + encodingHash[i]
    elif(countSenha < countHash):
        for i in range(countHash-countSenha):
            j = countHash-countSenha
            encodingHash = encodingHash - encodingHash[j]
            j -= 1
    
    k = 0
    criptografado = ""
    flag = [0, 0]
    hashing()
    for m in range(len(encodingHash)):
        for i in range(36):
            cpr = transHash[i][0]
            flag[0] = i
            if(cpr == senha[k]):
                for j in range(36):
                    cmp = transHash[0][j]
                    flag[1] = j
                    if(cmp == encodingHash[k]):
                        trasncrever = transHash[flag[0]][0] + transHash[0][flag[1]] + transHash[flag[0]][flag[1]]
                        criptografado = criptografado + trasncrever
        k += 1

    with open('senha.txt', 'r', encoding='utf8') as file:
        senhaCripto = file.readlines()

    acesso = 0
    if(criptografado == senhaCripto[0]):
        print("Acesso Garantigo!!! ")
        acesso = 1
    else:
        print("Senha Incorreta! ")
    return acesso

while True:
    acesso = testarSenha()
    while True:
        if acesso == 1:
            while True:
                alterar = input("Deseja alterar a senha? (s/n): ").strip().lower()
                if alterar == "s":
                    encriptando()
                    testar = input("Deseja testar a nova senha? (s/n): ").strip().lower()
                    if testar == "s":
                        acesso = testarSenha()
                    break
                elif alterar == "n":
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        else:
            tentar_novamente = input("Acesso negado. Deseja tentar novamente? (s/n): ").strip().lower()
            if tentar_novamente == "s":
                print("Teste sua senha novamente.")
                continue
            elif tentar_novamente == "n":
                break
            else:
                print("Opção inválida. Tente novamente.")
        break
    break

print("Encerrando o programa.")
print("Bye bye!")
