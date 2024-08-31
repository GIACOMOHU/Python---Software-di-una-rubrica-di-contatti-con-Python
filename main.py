from utils import Contatto, Rubrica, mostra_menu

def main():
    rubrica = Rubrica()

    while True:
        scelta = mostra_menu()

        if scelta == '1':
            nome = input("Nome: ")
            cognome = input("Cognome: ")
            contatto = Contatto(nome, cognome)
            rubrica.aggiungi_contatto(contatto)

        elif scelta == '2':
            rubrica.visualizza_contatti()

        elif scelta == '3':
            rubrica.visualizza_contatti()
            indice = int(input("Scegli il numero del contatto da modificare: ")) - 1
            nome = input("Nome (premi Invio per non cambiare): ")
            cognome = input("Cognome (premi Invio per non cambiare): ")
            telefono = input("Telefono (premi Invio per non cambiare): ")
            email = input("Email (premi Invio per non cambiare): ")
            rubrica.modifica_contatto(indice, nome, cognome, telefono, email)

        elif scelta == '4':
            rubrica.visualizza_contatti()
            indice = int(input("Scegli il numero del contatto da eliminare: ")) - 1
            rubrica.elimina_contatto(indice)

        elif scelta == '5':
            nome_o_cognome = input("Inserisci nome o cognome da cercare: ")
            rubrica.cerca_contatto(nome_o_cognome)

        elif scelta == '6':
            rubrica.salva_contatti()

        elif scelta == '7':
            rubrica.carica_contatti()

        elif scelta == '8':
            print("Uscita in corso...")
            break

        else:
            print("Opzione non valida. Riprova.")



# runniamo il programma

if __name__ == '__main__':
    main()