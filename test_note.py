import tkinter as tk

# Fonction de chiffrement de César
def encrypt_cesar(plaintext, shift):
    ciphertext = ''
    for letter in plaintext:
        if letter.isalpha():
            ciphertext += chr((ord(letter) + shift - 65) % 26 + 65)
        else:
            ciphertext += letter
    return ciphertext

# Fonction de déchiffrement de César
def decrypt_cesar(ciphertext, shift):
    plaintext = ''
    for letter in ciphertext:
        if letter.isalpha():
            plaintext += chr((ord(letter) - shift - 65) % 26 + 65)
        else:
            plaintext += letter
    return plaintext

# Fonction de chiffrement de Vigenère
def encrypt_vigenere(plaintext, keyword):
    ciphertext = ''
    keyword = keyword.upper()
    index = 0
    for letter in plaintext:
        if letter.isalpha():
            shift = ord(keyword[index % len(keyword)]) - 65
            ciphertext += chr((ord(letter) + shift - 65) % 26 + 65)
            index += 1
        else:
            ciphertext += letter
    return ciphertext

# Fonction de déchiffrement de Vigenère
def decrypt_vigenere(ciphertext, keyword):
    plaintext = ''
    keyword = keyword.upper()
    index = 0
    for letter in ciphertext:
        if letter.isalpha():
            shift = ord(keyword[index % len(keyword)]) - 65
            plaintext += chr((ord(letter) - shift - 65) % 26 + 65)
            index += 1
        else:
            plaintext += letter
    return plaintext

# Fonction de chiffrement de Scytale
def encrypt_scytale(plaintext, key):
    key = int(key)
    ciphertext = [''] * key
    index = 0
    for letter in plaintext:
        ciphertext[index] += letter
        index = (index + 1) % key
    return ''.join(ciphertext)

# Fonction de déchiffrement de Scytale
def decrypt_scytale(ciphertext, key):
    key = int(key)
    plaintext = [''] * len(ciphertext)
    index = 0
    for i in range(len(ciphertext)):
        plaintext[i] = ciphertext[index]
        index = (index + 1) % key
    return ''.join(plaintext)

def crypter_texte(texte, cle, methode):
    """
    Fonction qui chiffre ou déchiffre un texte selon la méthode choisie.
    texte: le texte à chiffrer ou déchiffrer
    cle: la clé de chiffrement ou déchiffrement
    methode: la méthode de chiffrement ou déchiffrement à utiliser ('cesar', 'vigenere', 'scytale')
    """
    if methode == 'cesar':
        resultat = ''
        for lettre in texte:
            if lettre.isalpha():
                code = ord(lettre)
                code += cle
                if lettre.isupper():
                    if code > ord('Z'):
                        code -= 26
                    elif code < ord('A'):
                        code += 26
                else:
                    if code > ord('z'):
                        code -= 26
                    elif code < ord('a'):
                        code += 26
                resultat += chr(code)
            else:
                resultat += lettre
        return resultat
    
    elif methode == 'vigenere':
        cle = cle.upper()
        resultat = ''
        i = 0
        for lettre in texte:
            if lettre.isalpha():
                decalage = ord(cle[i]) - ord('A')
                i = (i + 1) % len(cle)
                code = ord(lettre)
                if lettre.isupper():
                    code = (code - ord('A') + decalage) % 26 + ord('A')
                else:
                    code = (code - ord('a') + decalage) % 26 + ord('a')
                resultat += chr(code)
            else:
                resultat += lettre
        return resultat
    
    elif methode == 'scytale':
        cle = int(cle)
        texte = texte.replace(' ', '')
        nb_lignes = len(texte) // cle
        if len(texte) % cle != 0:
            nb_lignes += 1
        resultat = ''
        for i in range(cle):
            for j in range(nb_lignes):
                index = j * cle + i
                if index < len(texte):
                    resultat += texte[index]
        return resultat
    
    else:
        return 'Méthode de chiffrement/déchiffrement invalide'

def crypter():
    texte = zone_texte.get('1.0', 'end-1c')  # Récupération du texte dans la zone de texte
    cle = entree_cle.get()  # Récupération de la clé dans l'entrée de texte
    methode = var_methode.get()  # Récupération de la méthode choisie
    texte_crypte = crypter_texte(texte, cle, methode)  # Appel de la fonction de chiffrement/dé


# Création de la fenêtre et du Canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Boutons pour les méthodes de chiffrement et de déchiffrement
button_cesar_chiffrement = tk.Button(canvas, text="Chiffrement de César", command=encrypt_cesar)
button_cesar_dechiffrement = tk.Button(canvas, text="Déchiffrement de César", command=decrypt_cesar)
button_vigenere_chiffrement = tk.Button(canvas, text="Chiffrement de Vigenère", command=encrypt_vigenere)
button_vigenere_dechiffrement = tk.Button(canvas, text="Déchiffrement de Vigenère", command=decrypt_vigenere)
button_scytale_chiffrement = tk.Button(canvas, text="Chiffrement de Scytale", command=encrypt_scytale)
button_scytale_dechiffrement = tk.Button(canvas, text="Déchiffrement de Scytale", command=decrypt_scytale)

# Placement des boutons sur le Canvas
button_cesar_chiffrement.place(x=50, y=50)
button_cesar_dechiffrement.place(x=50, y=100)
button_vigenere_chiffrement.place(x=50, y=150)
button_vigenere_dechiffrement.place(x=50, y=200)
button_scytale_chiffrement.place(x=50, y=250)
button_scytale_dechiffrement.place(x=50, y=300)

root.mainloop()