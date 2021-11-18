import datetime
import os
import platform
import random
import sys
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

#Da aggiungere
#import datetime
#import playsound
#import wolframalpha
#from selenium import webdriver                                                                                     #Controllo Operazioni Browser

#Aggiungere un classe per generare altre classi così da essere compilate ed eseguite in Run-Time (possibilmente come sotto-processo)

prefix = " "
assistantName = " "
assistantPrefix = " "
userName = "Utente"
currentVersion = "0.0.5-ALPHA.2021.11.18"

def checkAndReadData():
    global assistantPrefix
    verifiedUsers = []

    for dir in os.listdir("appStorage/users/"):
        if os.path.isdir("appStorage/users/" + dir) and os.path.isfile("appStorage/users/" + dir + "/userSettings.txt"):
            verifiedUsers.append(dir)
        #elif os.path.isdir("appStorage/users/" + dir):                                                             #TODO: Provare ad aggiungere la posssibilità di eliminare gli utenti vuoti
        #    os.rmdir("appStorage/users/" + dir)

    if len(verifiedUsers) == 0:
        textAndSpeech("Ciao, sono il tuo nuovo e personale Assistente Vocale. Sembra che questa sia la prima volta che mi avvii, ciò significa che è necessaria una configurazione preliminare. Cominciamo!")
        assistantSetup()
    
    elif len(verifiedUsers) == 1:
        textAndSpeech("Ho trovato l'utente " + verifiedUsers[0] + ", vuoi caricare i dati associati?")
        query = takeCommand().lower()
        if query == "si" or query == "Si" or query == "sì" or query == "Sì":
            importUserSettings( verifiedUsers[0] )
        else:
            textAndSpeech("Ciao, sono il tuo nuovo e personale Assistente Vocale. Sembra che questa sia la prima volta che mi avvii, ciò significa che è necessaria una configurazione preliminare. Cominciamo!")
            assistantSetup()

    elif len(verifiedUsers) > 1:
        sampleString = ""
        for user in verifiedUsers:
            sampleString += "- " + user.capitalize() + "\n"
        sampleString += "- Nessuno"
        textAndSpeech("Ho trovato vari Utenti, eccoli:\n" + sampleString + "\nQuale vuoi caricare?")
        query = takeCommand().lower()
        if query in verifiedUsers:
            index = verifiedUsers.index( query )
            importUserSettings( verifiedUsers[index] )
        else:
            textAndSpeech("Ciao, sono il tuo nuovo e personale Assistente Vocale. Sembra che questa sia la prima volta che mi avvii, ciò significa che è necessaria una configurazione preliminare. Cominciamo!")
            assistantSetup()

    assistantPrefix = prefix.lower() + " " + assistantName.lower() + " "
    textAndSpeech("Fantastico, ora sei pronto ad utilizzarmi!")

def importUserSettings(dirName):
    global prefix
    global assistantName
    global userName

    with open("appStorage/users/" + dirName + "/userSettings.txt", "r") as file:
        prefix = file.readline().strip().lower()
        assistantName = file.readline().strip().capitalize()
        userName = dirName.capitalize()
        file.close()

def exportUserSettings():
    textAndSpeech("Inizio Salvataggio...")
    with open("appStorage/users/" + userName.lower() + "/userSettings.txt", "w") as file:
        file.write(prefix + "\n")
        file.write(assistantName + "\n")
        file.close()
    textAndSpeech("Salvataggio completato!")

def saveData():
    try:
        if os.path.isdir("appStorage/users/" + userName.lower()):
            if os.path.isfile("appStorage/users/" + userName.lower() + "/userSettings.txt"):
                textAndSpeech("Sei sicuro di voler sovvrascrivere i dati?")
                query = takeCommand().lower()
                if query == "si" or query == "Si" or query == "sì" or query == "Sì":
                    textAndSpeech("Modalità di Sovrascrittura Dati")
                    exportUserSettings()
                else:
                    return False
            else:
                textAndSpeech("Genero nuovi dati di salvataggio...")
                exportUserSettings()
        else:
            os.makedirs("appStorage/users/" + userName.lower() + "/")
            textAndSpeech("Genero nuovi dati di salvataggio...")
            exportUserSettings()
        return True
    except:
        textAndSpeech("Errore fatale durante il Salvataggio dei dati. Operazione annullata, riprovare più tardi.")
        return False

def assistantSetup():
    global prefix
    global assistantName
    global userName

    textAndSpeech("Che prefisso vuoi usare?\n- Ok\n- Ehi")
    query = takeCommand().lower()
    if query == "Ok" or query == "Ehi":
        prefix = query
    else:
        prefix = "ehi"
    textAndSpeech("Ok, come vuoi chiamarmi?")
    assistantName = takeCommand().capitalize()
    textAndSpeech("Perfetto, adesso come vuoi che ti chiami?")
    userName = takeCommand().capitalize()
    textAndSpeech("Fantastico, sei pronto ad utilizzarmi!")

def speak ( textToSpeech ):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say( textToSpeech )
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("In Ascolto...")
        r.pause_threshold = 0.7
        audio = r.listen(source)

    try:
        print("Riconoscimento...")
        query = r.recognize_google(audio, language='it-IT')
        print(f"{userName} ha detto: {query}\n")

    except Exception as e:
        print(e)
        print("Non ho capito. Ripeti per favore.")
        return "None"
    return query

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        textAndSpeech("Buongiorno " + userName)

    if currentH >= 12 and currentH < 18:
        textAndSpeech("Buon pomeriggio " + userName)

    if currentH >= 18 and currentH != 0:
        textAndSpeech("Buonasera " + userName)

def textAndSpeech ( text ):
    print(text)
    speak(text)

def Take_query():
    while True:
        query = takeCommand().lower()
        query.lower()

        if assistantPrefix + 'ciao' == query or assistantPrefix + 'Ciao' == query:
            greetMe()
        
        elif assistantPrefix + 'hello there' == query or assistantPrefix + 'Hello there' == query or assistantPrefix + 'hello There' == query or assistantPrefix + 'Hello There' == query:
            textAndSpeech("General " + userName + "!")

        elif assistantPrefix + 'apri una finestra di esplora file' == query or assistantPrefix + 'apri esplora file' == query:
            try:
                if platform.system() == "Windows":
                    webbrowser.open("explorer.exe")
                elif platform.system() == "Linux":
                    try:                                                                                            #TODO: Pseudo-Implementazione di xdg-open
                        #os.system("nautilus &")
                        os.system("xdg-open nautilus")
                    except:
                        try:
                            #os.system("nemo &")
                            os.system("xdg-open nemo")
                        except:
                            textAndSpeech("Non riesco a trovare un programma per aprire una finestra di Esplora File")
            except:
                textAndSpeech("Qualcosa non va, non sono riuscita ad aprire un finestra di Esplora File")

        elif assistantPrefix + 'apri una connessione samba' == query:
            textAndSpeech("Non ho ancora implementato questa funzione")

        elif assistantPrefix + 'connettimi al server' == query:
            textAndSpeech("Non ho ancora implementato questa funzione")

        elif assistantPrefix + 'mandami su internet' == query:                                                      #TODO: Valutare l'implementazione di Google
            textAndSpeech("Ok, buona navigazione")
            webbrowser.open("https://www.you.com/")
        
        elif assistantPrefix + 'fai una ricerca su wikipedia' == query:                                             #TODO: Migliorare dump dei risultati
            textAndSpeech("Cosa vuoi cercare?")
            query = takeCommand().lower()
            results = wikipedia.summary(query, sentences=2)
            textAndSpeech("A proposito di " + query)
            textAndSpeech(results)

        elif assistantPrefix + 'fai una ricerca su internet' == query:                                              #TODO: Valutare l'implementazione di Google
            textAndSpeech("Cosa vuoi cercare?")
            query = takeCommand().lower()
            webbrowser.open("https://www.you.com/search?q=" + query)
        
        elif assistantPrefix + 'apri youtube music' == query:
            textAndSpeech("Ok, apro YouTube Music")
            webbrowser.open("https://music.youtube.com/")

        elif assistantPrefix + 'cerca su youtube music' == query:
            textAndSpeech("Cosa vuoi cercare?")
            query = takeCommand().lower()
            webbrowser.open("https://music.youtube.com/search?q=" + query)

        elif assistantPrefix + 'grazie' == query or assistantPrefix + 'Grazie' == query:                           #TODO: Randomizzare il "Non c'è di che" con altro
            thanksDictionary = ["Prego!", "Di nulla!", "Non c'è di che!", "Al tuo sevizio!"]
            textAndSpeech( random.choice(thanksDictionary) )

        elif assistantPrefix + 'che ore sono' == query or assistantPrefix + 'che ore sono?' == query:
            textAndSpeech("Sono le " + datetime.datetime.now().strftime( "%H e %M" ))

        elif assistantPrefix + 'che giorno è' == query or assistantPrefix + 'che giorno è?' == query:
            textAndSpeech("Oggi è il " + datetime.date.today().strftime("%d %B %Y"))

        elif assistantPrefix + 'presentati' == query:
            textAndSpeech("Ma ciao, io sono " + assistantName + ", la tua assistente vocale. Al momento so fare poche cose, ma le so fare molto bene. Sono ancora in fase di sviluppo, se hai quindi dei problemi puoi rivolgerti a mio padre: Marco!")
        
        elif assistantPrefix + 'presentati in maniera accurata' == query:
            textAndSpeech("Nome: " + assistantName + ". Prefisso parziale: " + prefix + ". Prefisso Totale: " + assistantPrefix + ". Versione: " + currentVersion + ". Creato da: Marco")

        elif assistantPrefix + 'addio' == query or assistantPrefix + "Addio" == query:                              #TODO: Cambiare la Keyword con qualcosa di inequivocabile
            textAndSpeech("Prima che tu te ne vada, vuoi salvare i miei dati? Per salvare dì \"Salva\"")
            query = takeCommand().lower()
            if "salva" in query:
                if saveData():
                    textAndSpeech("Ciao ciao " + userName + "!")
                    sys.exit()

if __name__ == '__main__':
    checkAndReadData()
    Take_query()