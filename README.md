# 🌿 EcoGuida 2025

Un’applicazione desktop scritta in **Python** con **PyQt6**, che ti permette di esplorare informazioni sui principali **parchi nazionali italiani**: flora, fauna, attività e regole. Include una schermata iniziale con caricamento e una GUI interattiva.
> **Parchi disponibili**: Parco Nazionale del Gran Paradiso, Parco Nazionale del Cilento, Vallo di Diano e Alburni, Parco Nazionale delle Cinque Terre

---

## 🏗️ Architettura del progetto

```plaintext
EcoGuida2025/
├── src/
│   ├── text.py               # Contiene i testi dei parchi (flora, fauna, ecc.)
|   └── main.py               # Codice principale dell'applicazione
├── GUI/
│   ├── main.ui               # Layout UI della finestra principale (Qt Designer)
│   └── landing.ui            # Layout UI della landing page (Qt Designer)   
├── images/
│   ├── Logo_EcoGuida.png     # Icona del programma
|   ├── Logo_EcoGuidaNoBG     # Icona del programma (senza sfondo)
|   ├── cilento.jpg           # Immagine Parco Cilento
|   ├── cinqueterre.jpg       # Immagine Parco Cinque Terre
|   └── granparadiso.jpg      # Immagine Parco Gran Paradiso
├── README.md                 # Documentazione del progetto
└── app.py                    # Codice con QApplication da cui parte il programma
```
>**L'applicazione parte dal file app.py** per eseguirla va quindi mandato in esecuzione quel file con i **file necessari nella stessa path**

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

