# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
image bg bespin = "bespin.png"

image darkv sabre = "darth.png"

define d = Character('Dark Vador', color="#c8ffc8")


# Le jeu commence ici
label start:
    scene bg bespin
    show darkv sabre
    play music "imperial_march.mp3"
    d "Je suis ton père!"

menu:
    "Ah! D'accord, si vous le dites...":
         jump accord

    "Vous êtes sûr?":
         jump sur

label accord:
    d "Ensemble, nous règnerons sur la Galaxie!."
    jump finale

label sur:
    d "Puisque je te le dis..."
    jump finale

label finale:
    d "Tu connaîtras la suite... quand tu l'auras écrite!"
    return