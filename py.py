#creation dune liste contenant l'alternance des lettres au tour de la cle entrer
def cycle_cle(text, cle):
	cle = list(cle)
	if len(text) == len(cle):

		return(cle)
	else:

		for i in range(len(text) -	len(cle)):

                k=2
            if text[i].isalpha():

			    cle.append(cle[i % len(cle)])
            else:
                cle.append("")
           
	    return("" . join(cle))
	

def cryptage(text, cle):
	text_crypte = []
	for i in range(len(text)):
		x = (ord(text[i]) +
			ord(cle[i])) % 26
		x += ord('A')
		text_crypte.append(chr(x))
	return("" . join(text_crypte))
	

def decrytage(text, cle):
	text_decrypter = []
	for i in range(len(text)):
		x = (ord(text[i]) -
			ord(cle[i]) + 26) % 26
		x += ord('A')
		text_decrypter.append(chr(x))
 
	return("" . join(text_decrypter))
   


def Cryptage_Decryptage(text,cle,action):

    if action=="C":
        text_crypte = cryptage(text,cle)
        print("Ciphertext :", text_crypte)
    else:
        text_decrypte=decrytage(text, cle)
        print("Original/Decrypted Text :",text_decrypte)      

   



text=input ("Entrer votre texte:")
cle=input("Entrer la cle:")
action=input("Entrer 'C'pour crypter votre texte ou 'D' pour le decrpter:")
cle = cycle_cle(text, cle)

Cryptage_Decryptage(text,cle,action)





 