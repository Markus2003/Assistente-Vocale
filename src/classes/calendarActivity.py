import datetime
import time

import vocalAssistant

class calendarActivity:
    validClass = True

    creationDate = ""
    eventTitle = ""
    eventDate = ""
    timeEvent = ""

    def __init__():
        global validClass
        global creationDate
        global eventTitle
        global eventDate
        global timeEvent

        #creationDate = datetime.datetime.now().date()#Data e ora attuale
        vocalAssistant.textAndSpeech("Che nome vuoi dare all'Evento?")
        while True:
            query = vocalAssistant.takeCommand().lower()
            if query == "annulla" or query == "cancella" or query == "Annulla" or query == "Cancella":
                validClass = False
                return None
            vocalAssistant.textAndSpeech("Titolo Evento: " + query + ". Corretto?")
            temp = vocalAssistant.takeCommand().lower()
            if temp == "si" or temp == "sì" or temp == "Si" or temp == "Sì" or temp == "esatto" or temp == "Esatto" or temp == "corretto" or temp == "Corretto":
                eventTitle = query
                break
            else:
                vocalAssistant.textAndSpeech("Ripeti il nome dell'Evento per favore")

        vocalAssistant.textAndSpeech("In che giorno si svolge l'Evento? (In formato Giorno Mese Anno)")             #TODO: Aggiungere più compatibilità con le Date
        while True:
            query = vocalAssistant.takeCommand().lower()
            if query == "annulla" or query == "cancella" or query == "Annulla" or query == "Cancella":
                validClass = False
                return None
            query = query.split(" ")
            query[1] = calendarActivity.textMonthToNumber(query[1])
            try:
                datetime.date(int(query[2]), int(query[1]), int(query[0]))
                vocalAssistant.textAndSpeech("Data Evento: " + query[0] + " " + calendarActivity.numberMonthToText(query[1]) + " " + query[2] + ". Corretto?")
                temp = vocalAssistant.takeCommand().lower()
                if temp == "si" or temp == "sì" or temp == "Si" or temp == "Sì" or temp == "esatto" or temp == "Esatto" or temp == "corretto" or temp == "Corretto":
                    eventDate = datetime.date(int(query[2]), int(query[1]), int(query[0]))
                    break
                else:
                    vocalAssistant.textAndSpeech("Ripeti la data dell'Evento per favore")
            except ValueError:
                vocalAssistant.textAndSpeech("Data Evento non esistente. Ripeti la data dell'Evento per favore")
        
        vocalAssistant.textAndSpeech("A che ora ci sarà l'Evento? (In formato Ora e Minuti)")                       #TODO: Aggiungere più compatibilità con l'Orario
        while True:
            query = vocalAssistant.takeCommand().lower()
            if query == "annulla" or query == "cancella" or query == "Annulla" or query == "Cancella":
                validClass = False
                return None
            try:
                temp = query.split(":")
                time.strptime(query, "%H:%M")
                vocalAssistant.textAndSpeech("Orario Evento: " + query + ". Corretto?")
                temp = vocalAssistant.takeCommand().lower()
                if temp == "si" or temp == "sì" or temp == "Si" or temp == "Sì" or temp == "esatto" or temp == "Esatto" or temp == "corretto" or temp == "Corretto":
                    timeEvent = query
                    break
                else:
                    vocalAssistant.textAndSpeech("Ripeti l'orario dell'Evento per favore")
            except ValueError:
                vocalAssistant.textAndSpeech("Orario Evento non corretto. Ripeti l'orario dell'Evento per favore")

        validClass = True

    def textMonthToNumber(month:str):
        monthSample = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]
        return monthSample.index(month.lower()) + 1

    def numberMonthToText(month:int):
        monthSample = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]
        return monthSample[month - 1]

    def getValidClass(self):
        return validClass