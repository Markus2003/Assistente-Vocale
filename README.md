# Assistente Vocale
E non è neanche così terribile...

## Cos'è
```Assistente Vocale``` è appunto un Assistente Vocale scritto in Python altamente personalizzabile, anche se per il momento la personalizzazione si limita all'impostazione del Prefisso e del Nome Utente... 

Comunque conto di portare la personalizzazione a livelli più alti!
<br><br>

# Sviluppo Attivo

| OS | 64-bit | 32-bit | ARM |
|----|--------|--------|-----|
| Windows |  ✓     |  ?     |  ✗     |
| Linux   |  ✓     |  ?     |  ✗     |
| macOS   |  ✗     |  ✗     |  ✗     |

# Installazione
Durante la fase ```ALPHA``` potrai scaricare solo il Codice Sorgente
<!--Puoi scaricare direttamente una Release, altrimenti puoi scaricare il Codice Sorgente e compilarlo da te! (W l'Open Source)

## Installazione di una Release
- Scarica l'archivio da Release (Esempio: ```vocalAssistant - <version> - <platform>.rar```)
- Estrai l'archivio in una cartella a tua scelta
- Esegui ```vocalAssistant.exe``` per Windows, ```vocalAssistant``` per Linux
- Fatto!-->

##  Download Codice Sorgente
- Prima abbiamo detto che ```Assistente Vocale``` è scritto in Python, quindi dovrai scaricare [pip](https://www.python.org/)
- Questa app contiene librerie esterne che non sono incluse nell'installazione di ```pip```, dovrai quindi scaricarle, per farlo ti basterà aprire una finestra del ```CMD``` per Windows o del ```Terminale``` per Linux e scrivere:
```python
pip install pyttsx3 SpeechRecognition wikipedia

#Installazione PyAudio su Windows
pip install pipwin
pipwin install pyaudio

#Installazione PyAudio su Linux
pip install pyaudio
```
- Una volta installate le librerie potrai eseguire ```python vocalAssistant.py``` o ```python3 vocalAssistant.py```
- Fatto!

Python offre inoltre una libreria per la compilazione dei propri script: ```PyInstaller```. Per usarla ti basterà aprire una finestra del ```CMD``` per Windows o del ```Terminale``` per Linux e scrivere:
```python
pip install pyinstaller
```
dopodichè potrai eseguire dalla cartella dello script:
```python
pyinstaller -F -n "vocalAssistant" -i logo.ico vocalAssistant.py
#"-F" chiede a PyInstaller di creare un singolo file eseguibile, questo comando è opzionale
#"-n" imposta il nome del file eseguibile, questo comando è opzionale
#"-i" imposta l'icona dell'applicazione, questo comando è opzionale

#Le mie Release sono fatte con questo comando:
pyinstaller -n "vocalAssistant" -i src/logo.ico vocalAssistant.py
```

# Cosa sa fare
```Assistente Vocale``` sa fare già alcune cose:
- Sa salutare ad un ```Ciao!``` e a un ```Hello There!```
- Sa aprire una finestra di ```Esplorare File``` sia su ```Windows``` che su ```Linux```, o almeno ci prova...
- Sa aprire una finestra di ```Internet``` ed eventalmente fare una ricerca con ```you.com```
- Sa fare una ricerca su ```Wikipedia``` Inglese
- Sa aprire una finestra di ```YouTube Music``` ed eventualmente cercare un brano
- Sa rispondere ad un ```Grazie!```
- Sa dire ```che ore sono``` e ```che giorno è```
- Con un ```addio``` si chiude il programma
<br><br>

# Changelog
<!--## Versione Release
Versione Release attuale: ```V. 0.0.5-ALPHA.2021.11.17```<br>
Versione Base di ```Assistente Vocale```

<br>
-->
## Versione Codice Sorgente
Versione Codice Sorgente attuale: ```V. 0.0.5-ALPHA.2021.11.18```<br>
- ```a9de878``` -> Nuove Funzioni aggiunte (Richiesta ```data``` e ```ora``` )
- ```cd59da9``` -> Maggiore compatibilità con il TextToSpeech
- ```0e681f1``` -> Nuvo struttura per i dati, nuovo sistema di salvataggio e ripristino dati
<br><br>

# Feature in arrivo
A breve:
- Miglioramento Esperienza mediante CLI
- Calendario con Gestione degli Eveenti interno

Tra un po':
- Una incredibile GUI così da evitare la fastidiosa finestra del Terminale...
- Voice Trigger come per "```Hey Google```"
- Creazione di Comandi Personalizzati

Tra molto tempo:
- Porting per la lingua Inglese

Se ho tempo e se si può:
- Versione per ```Linux ARM``` su ```Chromebook```
<br><br>

# BUG
- Se su ```Linux``` viene dato un ```OSError``` quando l'Assistente dovrebbe parlare eseguire il comando ```sudo apt-get install espeak```
- Su ```Linux``` il Sintetizzatore Vocale ```espeak``` non da risultati soddisfacenti, sto cercando una soluzione a questo problema, intanto puoi provare ad utilizzare la versione ```Windows``` mediante ```Wine```
- L'Assistente sente solo quando compare la scritta "```In Ascolto...```", fare quindi attenzione a non parlare a vuoto
<br><br>

# Roadmap
- Dicembre: Migliorare Esperienza CLI
- Entro fine 2021 uscire dalla fase ```ALPHA``` ed entrare in fase ```BETA```
- Gennaio: Creazione dei Comandi Personalizzati
- Poi si vedrà...