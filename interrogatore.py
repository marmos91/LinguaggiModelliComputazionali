# -*- coding: cp1252 -*-
import string
import random
import sys

#La dimensione della lista associata alla domanda permette di deciderne il peso... Maggiore è il numero di elementi più spesso uscirà la domanda associata
#Basta modificare la lista domande 

domande = {
	"[Linguaggi] Computabilità di una funzione":[1,2,3,4,5,6,7],
	"[Linguaggi] Problema dell'Halt della macchina di Turing":[1,2,3,4,5,6,7,8],
	"[Linguaggi] Macchina di Turing":[1,2,3,4,5,6],
	"[Linguaggi] Problema risolubile":[1,2,3,4,5,6],
	"[Linguaggi] Insiemi decidibili e semi-decidibili":[1,2,3,4,5],
	"[linguaggi] Definizione di linguaggio":[1,2,3,4,5,6,7],
	"[linguaggi] Interpretazione e compilazione":[1,2,3,4,5],
	"[linguaggi] Alfabeti":[1,2,3,4,5],
	"[linguaggi] Grammatica formale":[1,2,3,4,5,6,7,8],
	"[linguaggi] Classificazione di Chomsky":[1,2,3,4,5,6,7,8,9,10],
	"[linguaggi] Esempio di eliminazione di epsilon-rules":[1,2,3,4,5,6,7],
	"[linguaggi] Self embedding":[1,2,3,4,5],
	"[linguaggi] Derivazioni canoniche":[1,2,3,4,5,6,7,8],
	"[linguaggi] Forme normali":[1,2,3,4,5,6,7],
	"[linguaggi] Pumping Lemma":[1,2,3,4,5,6,7,8],
	"[linguaggi] Riconoscitore a stati finiti (automi non deterministici?)":[1,2,3,4,5,6,7,8],
	"[linguaggi] PDA":[1,2,3,4,5,6,7,8],
	"[linguaggi] Grammatiche LL(k)":[1,2,3,4,5,6,7,8,9],
	"[linguaggi] Grammatiche LL(1)":[1,2,3,4,5,6],
	"[linguaggi] Starter symbols e director symbols":[1,2,3,4,5,6],
	"[linguaggi] Interpreti":[1,2,3,4],
	"[linguaggi] Stili di interpretazione":[1,2,3,4,5,6,7],
	"[linguaggi] Alcuni strumenti per la generazione di grammatiche LL(k)/LR(k) (lista)":[1,2,3,4,5],
	"[linguaggi] Riconoscitori LR(0)":[1,2,3,4,5,6,7,8],
	"[modelli computazionali] Processi computazionali (iterativo/ricorsivo)":[1,2,3,4,5,6,7],
	"[modelli computazionali] Call by name vs Call by value":[1,2,3,4,5,6,7,8],
	"[modelli computazionali] Chiusure":[1,2,3,4,5,6,7],
	"[javascript] Semafori particolari":[1,2,3,4,5,6],
	"[javacript] Chiusure dinamiche/lessicali":[1,2,3,4,5,6,7],
	"[javascript] Proto, Prototype e type augmenting":[1,2,3,4,5,6,7,8],
	"[javascript] Costruttori Function e funzioni":[1,2,3,4,5,6,7,8],
	"[lambda calcolo] Definizione":[1,2,3,4,5,6,7],
	"[lambda calcolo] Semantica":[1,2,3,4,5,6],
	"[lambda calcolo] Funzioni notevoli":[1,2,3,4,5],
	"[lambda calcolo] Teorema di church-rosser":[1,2,3,4],
	"[lambda calcolo] Strategie di riduzione":[1,2,3,4,5,6],
	"[lambda calcolo] Turing equivalenza":[1,2,3,4,5,6],
	"[lambda calcolo] Ricorsione":[1,2,3],
	"[scala] Idee di base e peculiarità (currying, yield, tratti, estrattori)":[1,2,3,4,5],
	"[scala] Scala vs javascript":[1,2,3],
	"[scala] Interoperabilità con java":[1,2,3]
	}


#######################################################################################################################################################################################################
def menu():
    print "\n"
    print "MENU"
    print "[1]:iniziare"
    print "[2]:lista delle domande"
    print "[3]:Esci"
    print "\n"
    while True:
        choose=raw_input("Scegli un opzione")
        if(choose=="1"):
            start()
            break;
        if(choose=="2"):
            lst()
            break;
        if(choose=="3"):
            esc()
            break;
        else:
            print "valore non riconosciuto"
    
def start():
    history=list()
    nuovadomanda=random.choice([k for k in domande.keys() for x in domande[k]])
    print "\n"
    print "INIZIO DOMANDE"
    print "\n"
    i=1
    while True:
        while True:
            
            if(len(history)==10):
                del history[0]

            nuovadomanda=random.choice([k for k in domande.keys() for x in domande[k]])

            if(nuovadomanda in history):
                print ""
            else:
                break;
            
        print str(i)+")"+nuovadomanda+"?"
        a=raw_input("[invio]:prossima domanda [0]:menu\n")
        history.append(nuovadomanda)
        i=i+1
        if(a=="0"):
            menu()
            break;
        if(a==""):
            print ""
def lst():
    i=1
    print "\n"
    print "LISTA DOMANDE PRESENTI"
    print "\n"
    for key in domande.keys():
        print str(i)+")"+str(key)
        i=i+1
    print "\n"
    menu()


def esc():
    print "ESCO"
    sys.exit()
    
menu()
        
##########################################################################################################################################################################################################
