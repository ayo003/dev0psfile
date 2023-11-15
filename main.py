def calcolatrice():
    domanda=input("inserisci operazione effettuare")
    numero1=int(input("valore1 \n"))
    numero2=int(input("valore2 \n"))
    risultato=0

    def somma(numero1, numero2):
        return numero1+numero2

    def sottrazione(numero1, numero2):
        return numero1-numero2

    def moltiplicazione(numero1, numero2):
        return numero1*numero2

    def divisione (numero1, numero2):
        return numero1/numero2

    if domanda == "+":
        risultato = somma(numero1,numero2)

    elif domanda == "-":
        risultato = sottrazione(numero1, numero2)

    elif domanda == "*":
        risultato = moltiplicazione(numero1, numero2)

    elif domanda == "/":
        risultato = divisione(numero1, numero2)

    print(risultato)

#execute
if __name__ == "__main__":
    calcolatrice()