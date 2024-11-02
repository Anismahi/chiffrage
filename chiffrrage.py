liste=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


message=input('entrez votre message:').upper()
clef=int(input('entrez votre clef:'))


def chiffrage_lettre(lettre,liste,clef):
    for i in range(len(liste)):
        if lettre==' ':
            return ' '
        elif liste[i]==lettre:
            return str(liste[i+clef])
    return '?'
    
    
message_chiffré = str()

for lettre in message:
    message_chiffré += chiffrage_lettre(lettre,liste,clef)

print(message_chiffré)


