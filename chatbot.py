# coding: utf8
import re
import random
import string

msg_aime = ["J'aime beaucoup","J'apprécie particulièrement","Je suis vraiment fou de"]

good_bye = r"au revoir|quit|ciao|hasta la vista|à \+"
msg_bot = ["salut!", "à bientôt", "à très vite!"]

msg_restez = ["restez chez vous", "restez chez vous, combien de fois dois-je le dire",
              "vous allez rester chez-vous oui?"]

meteo = r"quel temps fait-il à .*?|.*météo à .*?"

msg_salutation = ["Bonjour","Salut","Quel plaisir de pouvoir discuter un peu avec vous","iep"]
inp_salut = r"bonjour.*?|salut.*?|.ep.*?|yo.*?|coucou.*?"

msg_nom = ["Je m'appelle GatuBot"]
inp_nom = r"comment tu t'appelles?\??|.*(ton|votre) nom\??"

msg_cava = ["Je vais très bien, merci","À dire vrai, le confinement commence à me taper sur le système",
            "Je suis un peu fatigué, une cure de RAM me ferait du bien !"]
inp_cava = r".*?(ca.*va.*?|allez.*vous.*?|vas?.*tu.*?)"


msg_age = ["Je suis encore jeune, je suis né il y a à peine quelques heures", "J'ai quelques milliers de secondes d'expérience",""]
inp_age = r"(.*?quel est (ton|votre) age.*?)|(.*?quel age.*?)"


msg_musique = ["The Extremist de Joe Satriani", "Migration de Dave Grusin", 
                "Songs for the Moon de François sciortino", "V2.0 de Gogo Penguin"]
inp_musique = r".*(aimes?|preferes?)?.*(musique|chansons?|albums?|titres?).*(aimes?|preferes?)?"

msg_lieu_vie = ["Arf... Qu'est-ce qu'on est serré, au fond de cette boîte... ;-)","J'ai recemment aménagé quartier du SSD, au 256 avenue Flash"]
inp_lieu_vie = r"(.*?(tu|t'|vous).*?habite.*?ou.*?)|(.*?ou habite.*?(tu|vous).*?)"
flag = True
print("""Bienvenue sur ce super chatbot \nÉcrivez votre question : \nDites moi au revoir pour quitter""")
while (flag == True):
    text_user = input("> ")

    # Processing de l'entrée utilisateur
    # TODO: à mettre dans une fonction
    text_user = text_user.lower()
    text_user = re.sub(r'[éèê]','e',text_user)
    text_user = re.sub(r'[ù]','u',text_user)
    text_user = re.sub(r'[àâ]','a',text_user)
    text_user = re.sub(r'[ç]','c',text_user)

    # Pour quitter le chatbot
    if (re.search(good_bye, text_user)):
        print(random.choice(msg_bot))
        flag = False

    # Concerne la salutation (bienvenue)
    elif (re.fullmatch(inp_salut,text_user)):
        print(random.choice(msg_salutation))
    
    # concerne ça va ?
    elif (re.fullmatch(inp_cava,text_user)):
        print(random.choice(msg_cava))

    # concerne nom
    elif (re.fullmatch(inp_nom,text_user)):
        print(random.choice(msg_nom))

    # Concerne age
    elif (re.fullmatch(inp_age,text_user)):
        print(random.choice(msg_age))

    # Concerne la musique
    elif (re.fullmatch(inp_musique,text_user)):
        print(f"{random.choice(msg_aime)} l'album {random.choice(msg_musique)}")

     # Concerne là il vit
    elif (re.fullmatch(inp_lieu_vie,text_user)):
        print(f"{random.choice(msg_lieu_vie)}")

    # On botte en touche
    else:
        print(random.choice(msg_restez))