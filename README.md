# Assistente Vocale
E non è neanche così terribile...

## Cos'è
```Assistente Vocale``` è appunto un Assistente Vocale scritto in Python altamente personalizzabile, anche se per il momento la personalizzazione si limita all'impostazione del Prefisso e del Nome Utente... 

Comunque conto di portare la personalizzazione a livelli più alti!

## Installazione
Puoi scaricare direttamente una Release, altrimenti puoi scaricare il Codice Sorgente e compilarlo da te! (W l'Open Source)

# Installazione di una Release
- Scarica l'archivio da Release (Esempio: ```vocalAssistant - <version> - <platform>.rar```)
- Estrai l'archivio in una cartella a tua scelta
- Esegui ```vocalAssistant.exe``` per Windows, ```vocalAssistant``` per Linux
- Fatto!

#  Download Codice Sorgente
- Prima abbiamo detto che ```Assistente Vocale``` è scritto in Python, quindi dovrai scaricare [pip](https://www.python.org/)
- Questa app contiene librerie esterne che non sono incluse nell'installazione di ```pip```, dovrai quindi scaricarle, per farlo ti basterà aprire una finestra del ```CMD``` per Windows o del ```Terminale``` per Linux e scrivere:
```python
    pip install pyttsx3
    pip install SpeechRecognition
    pip install wikipedia
```
- Una volta installate le librerie potrai eseguire ```pip vocalAssistant.py```
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

# Feature in arrivo
A breve:
- Miglioramento esperienza mediante CLI
- Creazione di Comandi Personalizzati

Tra un po':
- Una incredibile GUI così da evitare la fastidiosa finestra del Terminale...
- Voice Trigger come per "```Hey Google```"
- Calendario con Gestione degli Eventi interno

Tra molto tempo:
- Porting per la lingua Inglese

# BUG
- Su ```Linux``` il Sintetizzatore Vocale ```emacs``` e ```espeak``` non danno risultati soddisfacenti, sto cercando una soluzione a questo problema, intanto puoi provare ad utilizzare la versione ```Windows``` mediante Wine
- L'Assistente sente solo quando compare la scritta "```In Ascolto...```", fare quindi attenzione a non parlare a vuoto