# Importiamo i moduli e le funzioni necessarie

import json
from validate_email_address import validate_email
import phonenumbers





# definiamo le classi e le funzioni necessarie

class Contatto:
    def __init__(self, nome, cognome, telefono=None, email=None, skip_validation=False):
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono if telefono or skip_validation else self.chiedi_telefono_valido()
        self.email = email if email or skip_validation else self.chiedi_email_valida()

    def chiedi_email_valida(self):
        email = input("Email (o lascia vuoto): ")
        while email and not self.is_email_valid(email):
            print(f"L'email '{email}' non è valida.")
            email = input("Inserisci un'email valida (o lascia vuoto): ")
        return email

    def is_email_valid(self, email):
        return validate_email(email)

    def chiedi_telefono_valido(self):
        telefono = input("Telefono (o lascia vuoto): ")
        while telefono and not self.is_telefono_valido(telefono):
            print(f"Il telefono '{telefono}' non è valido.")
            telefono = input("Inserisci un telefono valido (o lascia vuoto): ")
        return telefono

    def is_telefono_valido(self, telefono):
        try:
            parsed_number = phonenumbers.parse(telefono, "IT")
            return phonenumbers.is_valid_number(parsed_number)
        except phonenumbers.NumberParseException:
            return False

    def __str__(self):
        return f"{self.nome} {self.cognome} - Tel: {self.telefono or 'N/D'} - Email: {self.email or 'N/D'}"
    

class Rubrica:
    def __init__(self):
        self.contatti = []

    def aggiungi_contatto(self, contatto):
        self.contatti.append(contatto)
        print(f"Contatto {contatto.nome} {contatto.cognome} aggiunto con successo.")

    def visualizza_contatti(self):
        if not self.contatti:
            print("Nessun contatto presente.")
        else:
            for idx, contatto in enumerate(self.contatti, 1):
                print(f"{idx} {contatto}")

    
    def modifica_contatto(self, indice, nome=None, cognome=None, telefono=None, email=None):
        if 0 <= indice < len(self.contatti):
            contatto = self.contatti[indice]

            if nome:
                contatto.nome = nome
            if cognome:
                contatto.cognome = cognome

            # Prima gestiamo il telefono
            if telefono:
                while not contatto.is_telefono_valido(telefono):
                    print(f"Il telefono '{telefono}' non è valido.")
                    telefono = input("Inserisci un telefono valido (premi Invio per non cambiare): ")
                    if not telefono:  # Se l'utente preme Invio, mantiene il vecchio numero
                        telefono = contatto.telefono
                        break
                contatto.telefono = telefono  # Aggiorniamo il telefono solo dopo la validazione

            # Solo dopo la validazione del telefono, passiamo all'email
            if email:
                while not contatto.is_email_valid(email):
                    print(f"L'email '{email}' non è valida.")
                    email = input("Inserisci un'email valida (premi Invio per non cambiare): ")
                    if not email:  # Se l'utente preme Invio, mantiene la vecchia email
                        email = contatto.email
                        break
                contatto.email = email  # Aggiorniamo l'email solo dopo la validazione

            print("Contatto modificato con successo.")
        else:
            print("Indice non valido.")



    def elimina_contatto(self, indice):
        if 0 <= indice < len(self.contatti):
            contatto = self.contatti.pop(indice)
            print(f"Contatto {contatto.nome} {contatto.cognome} eliminato.")
        else:
            print("Indice non valido.")


    def cerca_contatto(self, nome_o_cognome):
        risultati = [contatto for contatto in self.contatti if nome_o_cognome.lower() in contatto.nome.lower() or nome_o_cognome.lower() in contatto.cognome.lower()]
        if risultati:
            for idx, contatto in enumerate(risultati, 1):
                print(f"{idx}. {contatto}")
        else:
            print("Nessun contatto trovato.")

    def salva_contatti(self, filename='rubrica.json'):
        with open(filename, 'w') as file:
            json.dump([contatto.__dict__ for contatto in self.contatti], file, indent=4)
        print("Contatti salvati con successo.")

    def carica_contatti(self, filename='rubrica.json'):
        try:
            with open(filename, 'r') as file:
                self.contatti = [Contatto(**dati, skip_validation=True) for dati in json.load(file)]
            print("Contatti caricati con successo.")
        except FileNotFoundError:
            print("Nessun file trovato. Verrà creata una nuova rubrica.")

                      
def mostra_menu():
    print("\n--- Rubrica ---")
    print("1 Aggiungi Contatto")
    print("2 Visualizza Contatti")
    print("3 Modifica Contatto")
    print("4 Elimina Contatto")
    print("5 Cerca Contatto")
    print("6 Salva Contatti")
    print("7 Carica Contatti")
    print("8 Esci")
    return input("Scegli un'opzione: ")
