import tkinter as tk

# Fonction de chiffrement de César
def encrypt_cesar():
    plaintext = entry_text.get()
    shift = int(entry_key.get())
    ciphertext = ''
    for letter in plaintext:
        if letter.isalpha():
            ciphertext += chr((ord(letter) + shift - 65) % 26 + 65)
        else:
            ciphertext += letter
    label_resultat.config(text=ciphertext)

# Fonction de déchiffrement de César
def decrypt_cesar():
    ciphertext = entry_text.get()
    shift = int(entry_key.get())
    plaintext = ''
    for letter in ciphertext:
        if letter.isalpha():
            plaintext += chr((ord(letter) - shift - 65) % 26 + 65)
        else:
            plaintext += letter
    label_resultat.config(text=plaintext)

# Fonction de chiffrement de Vigenère
def encrypt_vigenere():
    plaintext = entry_text.get()
    keyword = entry_key.get()
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
    label_resultat.config(text=ciphertext)

# Fonction de déchiffrement de Vigenère
def decrypt_vigenere():
    ciphertext = entry_text.get()
    keyword = entry_key.get()
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
    label_resultat.config(text=plaintext)

# Fonction de chiffrement de Scytale
def encrypt_scytale():
    plaintext = entry_text.get()
    key = int(entry_key.get())
    ciphertext = [''] * key
    index = 0
    for letter in plaintext:
        ciphertext[index] += letter
        index = (index + 1) % key
    label_resultat.config(text=''.join(ciphertext))

# Fonction de déchiffrement de Scytale
def decrypt_scytale():
    ciphertext = entry_text.get()
    key = int(entry_key.get())
    plaintext = [''] * len(ciphertext)
    index = 0
    for i in range(len(ciphertext)):
        plaintext[i] = ciphertext[index]
        index = (index + 1) % key
    label_resultat.config(text=''.join(plaintext))

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
    texte = label_text.get('1.0', 'end-1c')  # Récupération du texte dans la zone de texte
    cle = label_key.get()  # Récupération de la clé dans l'entrée de texte
    methode = var_methode.get()  # Récupération de la méthode choisie
    texte_crypte = crypter_texte(texte, cle, methode)  # Appel de la fonction de chiffrement/dé



# Création de la fenêtre et du Canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Zone de texte pour le message à chiffrer/déchiffrer et pour la clé
label_text = tk.Label(canvas, text="Message : ")
label_text.place(x=50, y=400)
entry_text = tk.Entry(canvas)
entry_text.place(x=150, y=400)

label_key = tk.Label(canvas, text="Clé : ")
label_key.place(x=50, y=450)
entry_key = tk.Entry(canvas)
entry_key.place(x=150, y=450)

# Création du label pour afficher le résultat
label_resultat = tk.Label(canvas, text="")
label_resultat.place(x=50, y=500)
label_resultat.config(text="crypter")

# Boutons
button_cesar_chiffrement = tk.Button(canvas, text="Chiffrement de César", command=encrypt_cesar)
button_cesar_dechiffrement = tk.Button(canvas, text="Déchiffrement de César", command=decrypt_cesar)
button_vigenere_chiffrement = tk.Button(canvas, text="Chiffrement de Vigenère", command=encrypt_vigenere)
button_vigenere_dechiffrement = tk.Button(canvas, text="Déchiffrement de Vigenère", command=decrypt_vigenere)
button_scytale_chiffrement = tk.Button(canvas, text="Chiffrement de Scytale", command=encrypt_scytale)
button_scytale_dechiffrement = tk.Button(canvas, text="Déchiffrement de Scytale", command=decrypt_scytale)
button_crypter = tk.Button(canvas, text="Crypter", command=crypter)


# Placement des boutons sur le Canvas
button_cesar_chiffrement.place(x=40, y=50)
button_cesar_dechiffrement.place(x=40, y=100)
button_vigenere_chiffrement.place(x=40, y=150)
button_vigenere_dechiffrement.place(x=40, y=200)
button_scytale_chiffrement.place(x=40, y=250)
button_scytale_dechiffrement.place(x=40, y=300)
button_crypter.place(x=40, y=350)


root.mainloop()