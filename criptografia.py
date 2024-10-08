mensagem = input("Digite sua mensagem: ")
chave = input("Digite sua chave(a chave deve ter o mesmo número de letras que a mensagem): ")
msgFinal = ""
if len(mensagem) == len(chave):
    for i, l in zip(mensagem, chave):
        msg = ord(i)
        chaveUsada = ord(l)-97
        if msg + chaveUsada > 122:
            msg -= 26
        msgFinal+= chr(msg+chaveUsada)     
    print(msgFinal)
    
    
mensagem = input("Digite sua mensagem criptografada: ")
chave = input("Digite sua chave(a chave deve ter o mesmo número de letras que a mensagem): ")
msgFinal = ""
if len(mensagem) == len(chave):
    for i, l in zip(mensagem, chave):

            msg = ord(i)
            chaveUsada = ord(l)-97
            if msg - chaveUsada < 97:
                msg += 26
            msgFinal+= chr(msg-chaveUsada)     
    print(msgFinal)