#  Network Discovery Scanner (Python)

En enkel og praktisk **network discovery-skanner** skrevet i Python, designet for læring innen cybersikkerhet.
Prosjektet viser hvordan man bruker Python og `nmap` for å finne alle aktive enheter på et nettverk og lagre resultatene i strukturert JSON-format.

---

##  Funksjoner

* Oppdager alle aktive enheter på nettverket (ping-scan)
* Henter IP-, MAC- og vendor-informasjon
* Lagre funn i JSON-filer under `data/`
* CLI-argumenter: `--network`, `--output`
* Kan brukes på hjemmenettverk, lab-miljøer og VM-nettverk
* Lett å bygge videre på med portskanning og risikovurdering

---

##  Krav

For å kjøre prosjektet trenger du:

* **Python 3**
* **Nmap installert** (må ligge i PATH)
  Last ned: [https://nmap.org/download.html](https://nmap.org/download.html)
* Python-pakken `python-nmap` (installeres automatisk via `requirements.txt`)

---

##  Installering og oppstart

### 1. Klon prosjektet

```bash
git clone https://github.com/<brukernavn>/network-discovery-scanner.git
cd network-discovery-scanner
```

### 2. Opprett og aktiver virtuelt miljø

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 3. Installer avhengigheter

```bash
pip install -r requirements.txt
```

---

##  Bruk

###  Standard scanning (bruker default 192.168.4.0/22)

```bash
python -m discovery.discovery
```

Lagrer automatisk resultatet som JSON i `data/`.

###  Skann et spesifikt nettverk

```bash
python -m discovery.discovery --network 192.168.7.0/24
```

###  Lagre til en egendefinert JSON-fil

```bash
python -m discovery.discovery --network 192.168.4.0/22 --output data/min_scan.json
```

---

##  Eksempel på JSON-resultat

En typisk output-fil kan se slik ut:

```json
{
  "generated_at": "2025-11-23T00:45:12",
  "host_count": 4,
  "hosts": [
    {
      "ip": "192.168.4.1",
      "mac": "64:97:14:B2:CC:4D",
      "vendor": "eero",
      "state": "up"
    },
    {
      "ip": "192.168.7.155",
      "mac": "FC:3C:D7:0C:05:E6",
      "vendor": "Tuya Smart",
      "state": "up"
    }
  ]
}
```

---

## Om prosjektet

Dette prosjektet er laget som en del av en personlig læringsreise innen cybersikkerhet, med fokus på:

* Nettverksanalyse og kartlegging
* Automatisering i Python
* JSON-databehandling
* Git/GitHub-workflow
* Forståelse av Nmap og nettverksinfrastruktur

Verktøyet er et utmerket tillegg til en sikkerhetsportefølje og svært nyttig i intervjusituasjoner.

---