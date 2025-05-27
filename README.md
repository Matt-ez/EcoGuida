# 🌿 EcoGuida 2025

Un’applicazione desktop scritta in **Python** con **PyQt6**, che ti permette di esplorare informazioni sui principali **parchi nazionali italiani**: flora, fauna, attività e regole. Include una schermata iniziale con caricamento e una GUI interattiva.

---

## 🏗️ Architettura del progetto

EcoGuida2025/\n
├── src/\n
│ └── text.py # Contiene i testi dei parchi (flora, fauna, ecc.)\n
├── GUI/\n
│ ├── main.ui # Layout UI della finestra principale (Qt Designer)\n
│ └── landing.ui # Layout UI della landing page (Qt Designer)\n
├── images/\n
│ └── Logo_EcoGuida.png # Icona del programma\n
├── main.py # Codice principale dell'applicazione\n
├── README.md # Documentazione del progetto\n
└── requirements.txt # Librerie necessarie\n

---

## 📚 Funzionalità principali

✅ **Landing page** con progress bar simulato e pulsante “Entra”.  
✅ **Finestra principale** con selezione di parchi e visualizzazione di testi informativi.  
✅ **Controllo selezione**: l’utente deve selezionare un parco prima di poter esplorare le informazioni.  
✅ **Gestione dinamica degli eventi**: connessione e disconnessione dei bottoni in base alla selezione del parco.  
✅ **Messaggi di alert**: avvisi se l’utente cerca di esplorare senza selezionare un parco.  
✅ **Icone e grafica**: icona personalizzata e stile base.

---

## 🔍 Dettaglio del funzionamento

### 📖 Classi principali

### `Landing(QWidget)`
- Mostra la schermata di benvenuto.
- Contiene una progress bar e un pulsante "Entra".
- Metodo `openApp`: simula il caricamento e apre la finestra principale (`Window`).

### `Window(QWidget)`
- La finestra principale del programma.
- Contiene una ComboBox per selezionare i parchi, pulsanti per esplorare e una label per visualizzare i testi.
- Metodo `deSelect`: deseleziona il parco, resetta lo stato e ricollega i bottoni agli alert.
- Metodo `deselecter`: disconnette i bottoni da qualsiasi funzione collegata.
- Metodo `alert`: mostra un messaggio d’errore se l’utente non ha selezionato un parco.
- Metodo `parcoChanger`: cambia lo stato della selezione e connette i bottoni alle funzioni specifiche del parco.
- Metodi `granParadiso`, `parcoCilento`, `parcoCinqueTerre`: collegano i bottoni ai testi importati da `src.text`.

### 📚 Contenuto `src/text.py`
Contiene le variabili:
- `floraGranParadiso`, `faunaGranParadiso`, `activityGranParadiso`, `regoleGranParadiso`
- `floraCilento`, `faunaCilento`, `activityCilento`, `regoleCilento`
- `floraCinqueTerre`, `faunaCinqueTerre`, `activityCinqueTerre`, `regoleCinqueTerre`

---

# 🌿 Esplora i parchi e rispetta la natura!
> Creato da: Riccardo Dal Zotto e Matteo Bonaccini

