""" Codage en langue Leet Speak (1337 sp34k) """


SUBSTITUTIONS = [['e', '3'], ['a', '4'], ['l', '1'], ['o', '0'], ['t', '7']]

def coder_message(message, substitutions):
    for s in substitutions:
        vcar = s[0]
        ncar = s[1]
        message = message.replace(vcar, ncar)
    return message


message = raw_input('Message que je dois crypter : ')
txt_converti = coder_message(message, SUBSTITUTIONS)
print("Tu avais saisi ceci : " + message)
print("Le codage donne ceci : " + txt_converti)
