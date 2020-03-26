# coding: utf8
import re
import random
import string
from textblob import TextBlob
from textblob_fr import PatternAnalyzer

# Fonction nettoyage input user
def input_cleaner(text_user):
    text_user = text_user.lower()
    text_user = re.sub(r'[éèê]','e',text_user)
    text_user = re.sub(r'[ù]','u',text_user)
    text_user = re.sub(r'[àâ]','a',text_user)
    text_user = re.sub(r'[ç]','c',text_user)
    return text_user

# On peut stocker certaines infos de l'utilisateur dans un dictionnaire
user = {}

msg_aime = [
"J'aime beaucoup",
"J'apprécie particulièrement",
"Je suis vraiment fou de"
]

good_bye = r"au revoir|quit|ciao|hasta la vista|à \+"
msg_bot = ["Au revoir!", "à bientôt", "à très vite!","ciao ciao"]

msg_restez = [
"Restez chez vous", 
"Restez chez vous, combien de fois dois-je le dire",
"vous allez rester chez-vous oui?"
]

meteo = r"quel temps fait-il à .*?|.*météo à .*?"

msg_salutation = [
"Bonjour",
"Salut",
"Quel plaisir de pouvoir discuter un peu avec vous",
"iep",
"Egun On"
]
inp_salut = r"bonjour.*?|salut.*?|.ep.*?|yo.*?|coucou.*?"

msg_nom = ["Je m'appelle GatuBot, (indice \"gatu\" c'est \"chat\" en basque)\nEt toi ?"]
inp_nom = r"comment tu t'appelles?\??|.*(ton|votre) nom\??"

msg_cava = [
"Je vais très bien, merci. Et vous ?",
"À dire vrai, le confinement commence à me taper sur le système.\nMais assez parlé de moi, comment allez VOUS ?",
"Je suis un peu fatigué ces temps-ci, une cure de RAM me ferait du bien !\nEt toi, ça farte ?"
]
inp_cava = r".*?(ca.*va.*?|allez.*vous.*?|vas?.*tu.*?)"

# TODO: ajouter un calcul en jours/heures/minutes avec datetime
msg_age = [
"Je suis encore jeune, je suis né il y a à peine quelques heures",
"J'ai quelques milliers de secondes d'expérience",
""
]
inp_age = r"(.*?quel est (ton|votre) age.*?)|(.*?quel age.*?)"

msg_musique = [
"The Extremist de Joe Satriani", 
"Migration de Dave Grusin", 
"Songs for the Moon de François sciortino",
"V2.0 de Gogo Penguin"
]
inp_musique = r".*(aimes?|preferes?)?.*(musique|chansons?|albums?|titres?).*(aimes?|preferes?)?"

msg_lieu_vie = ["Arf... Qu'est-ce qu'on est serré, au fond de cette boîte... ;-)",
"J'ai recemment aménagé quartier du SSD, au 256 avenue Flash"]
inp_lieu_vie = r"(.*?(tu|t'|vous).*?(habite|vi).*?ou.*?)|(.*?ou (habite|vi).*?(tu|vous).*?)"

msg_occupation = [
"Je lis du code sur StackOverFlow",
"Je regarde des vidéos de chatons sur YouTube",
"Je joue au Démineur puis au Solitaire... mais en activant le raytracing, en 4K et en 120i/s !!!"
]
inp_occupation = r"(.*?(fais?|faites?).*(tu|vous).*)|(.*?aime.*?(tu|vous) faire.*?)|(.*?(tu|vous) (fais|fait|faites?) quoi.*?)"

flag = True
print("""Bienvenue sur ce super chatbot \nÉcrivez votre question : \nDites moi au revoir pour quitter""")
while (flag == True):
    text_user = input("> ")

    # Processing entrée utilisateur
    text_user = input_cleaner(text_user)

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
        text_user = input("> ")
        blob = TextBlob(text_user, analyzer=PatternAnalyzer())
        user['humeur'] = blob.sentiment[0]
        if (user['humeur'] > 0.5):
            print("Ah ça me fait plaisir de lire ça ! :-D")
        elif (user['humeur'] > 0):
            print("Et demain ça ira encore mieux :-)")
        elif (user['humeur'] > -0.5):
            print("Y'a des jours comme ça... :-/")
        else:
            print("Et si on parlait de musique plutôt ? :-(")

    # concerne nom
    elif (re.fullmatch(inp_nom,text_user)):
        print(random.choice(msg_nom))
        user['name'] = input("> ")
        print(f"Enchanté {user['name']}")

    # Concerne age
    elif (re.fullmatch(inp_age,text_user)):
        print(random.choice(msg_age))

    # Concerne la musique
    elif (re.fullmatch(inp_musique,text_user)):
        print(f"{random.choice(msg_aime)} l'album {random.choice(msg_musique)}")

     # Concerne là il vit
    elif (re.fullmatch(inp_lieu_vie,text_user)):
        print(f"{random.choice(msg_lieu_vie)}")

    # Concerne ce qu'il fait
    elif (re.fullmatch(inp_occupation,text_user)):
        print(f"{random.choice(msg_occupation)}")

    # On botte en touche
    else:
        print(random.choice(msg_restez))


print("Pour débug: ",user)