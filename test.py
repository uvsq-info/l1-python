# Importation des modules nécessaires
import tkinter as tk

# Définition de la fonction de chiffrement César
def chiffre_cesar(texte, cle):

#Cette fonction prend en entrée un texte à chiffrer et une clé de chiffrement, et renvoie le texte chiffré selon la méthode de chiffrement César.
    texte_chiffre = []
    for lettre in texte:
        if lettre.isalpha():
# On calcule la position de la lettre dans l'alphabet, en prenant en compte
# la casse (A = 0, a = 26, etc.)
            if lettre.islower():
                pos = ord(lettre) - 97
            else:
                pos = ord(lettre) - 65
# On applique la clé de chiffrement (déplacement de 'cle' positions)
            nouvelle_pos = (pos + cle) % 26
# On convertit la nouvelle position en une lettre
            if lettre.islower():
                lettre_chiffree = chr(nouvelle_pos + 97)
            else:
                lettre_chiffree = chr(nouvelle_pos + 65)
# On ajoute la lettre chiffrée au texte chiffré
            texte_chiffre.append(lettre_chiffree)
        else:
# On ajoute les caractères spéciaux tels quels
            texte_chiffre.append(lettre)
    return "".join(texte_chiffre)

# Définition de la fonction appelée lorsqu'on appuie sur le bouton Chiffrer
def chiffrer():
    texte_clair = zone_texte_clair.get("1.0", tk.END).strip()
    cle = int(zone_cle.get())
    texte_chiffre = chiffre_cesar(texte_clair, cle)
    zone_texte_chiffre.delete("1.0", tk.END)
    zone_texte_chiffre.insert("1.0", texte_chiffre)

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Chiffrement César")

# Création des widgets
label_clair = tk.Label(fenetre, text="Texte clair:")
zone_texte_clair = tk.Text(fenetre, width=40, height=5)
label_cle = tk.Label(fenetre, text="Clé de chiffrement:")
zone_cle = tk.Entry(fenetre)
bouton_chiffrer = tk.Button(fenetre, text="Chiffrer", command=chiffrer)
label_chiffre = tk.Label(fenetre, text="Texte chiffré:")
zone_texte_chiffre = tk.Text(fenetre, width=40, height=5)

# Placement des widgets dans la fenêtre
label_clair.grid(row=0, column=0, padx=10, pady=10)
zone_texte_clair.grid(row=0, column=1, padx=10, pady=10)
label_cle.grid(row=1, column=0, padx=10, pady=10)
zone_cle.grid(row=1, column=1, padx=10, pady=10)
bouton_chiffrer.grid(row=2, column=0, padx=10, pady=10)
label_chiffre.grid(row=3, column=0, padx=10, pady=10)
zone_texte_chiffre.grid(row=3, column=1, padx=10, pady=10)

fenetre.mainloop()