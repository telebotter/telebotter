# Projekt Installieren

## Projekt lokal Klonen

```
git clone git@github.com:telebotter/telebotter.git
```

## Python Umgebung

### Mit Conda
> Unter Windows geht das auch mit der GUI (Anaconda Navigator) siehe screenshots. Oeffnet man darueber die Konsole, ist diese direkt gesourced und git sollte auch verfuegbar sein. Siehe Screenshot:


![https://github.com/telebotter/telebotter/docs/02_open_term.png](02_open_term)

```bash
conda create telebotter python=3.8 pip
conda activate telebotter
```

### Ohne Conda

Wenn die env direkt aus python heraus erstellt wird, sollte eine aktuelle python verison installiert sein (min 3.5 best 3.8). Wie die venv aktiviert wird, haengt von der verwendeten shell ab.

```bash
python3.8 -m venv /path/to/envs/telebotter
source /path/to/envs/telebotter/bin/activate  # bash/zsh (linux)
\path\to\envs\telebotter\Scripts\activate.bat  # cmd.exe (or .ps1 for powershell)
```

### Abhaengigkeiten installieren
> Unter Windows hatte ich fehler beim installieren mit pip, da scheinbar cython nicht korrekt installiert wurde. Installiert man das vorweg, sollte es aber funktionieren
```
conda install cython
```

Aus dem Projektordner koennen dann alle benoetigten Bibliotheken installiert werden:
```bash
pip install -r requirements.txt
```

## Settings anpassen

Fast alle Einstellungen finden sich in der `telebotter/settings.py`. Darin sind auch Datenbank Logins und Pfade zu logfiles etc. angegeben, daher muss diese Datei auf jedem System individuell angepasst werden. Als Ausgangspunkt kann man sich die Beispieldatei kopieren und den Anweisungen in den Kommentaren folgen:
```bash
cp telebotter/example_settings.py telebotter/settings.py
```

# Bots installieren

## Projekt lokal Klonen
In aktivierter python-Umgebung:
```
cd telebotter
git clone git@github.com:telebotter/projekt47.git
```


## Einstellungen anpassen
In der datei `telebotter/settings.py`
`projekt47` in die `INSTALLED_APPS` eintragen (Kommentar entf.). 
Außerdem eigenen `TOKEN` in die DJANGO_TELEGRAM_BOTS eintragen (ganz unten). 


## DB initialisieren
```
python manage.py makemigrations
python manage.py migrate
```
Sollte eine `lokaldb.sqlite` erzeugen, die Tabellen sollte nicht händisch verändert werden.
Falls die Tabellen für die apps noch nicht automatisch generiert wurden, noch einmal explizit (schadet nicht doppelt):

```
python manage.py makemigrations projekt47 core
python manage.py migrate
```
> Muss wiederholt werden, wenn sich die DB Tabellen veraendern (Bei Aenderung in models.py)

## Django Webserver
Wenn der bot unter polling läuft erstmal nicht direkt nötig, darüber kann aber zB das Django Admin Webinterface auch für die lokale DB verwendet werden.
Wenn die `django-telegram-bot app` nicht verwendet wird, steht auch das webinterface fuer die bots nicht zur Verfuegung. Daher
in der `telebotter/urls.py` die Zeile 
```
# url(r'^', include('django_telegrambot.urls')),
``` 
auskommentieren.
Folgenden Befehl zum generieren einiger css Dateien ausfuehren, damit das Admininterface etwas huebscher wird (falls immernoch haesslich pruefen ob settings.py DEBUG=True ist):
```
python manage.py collectstatic
```
Und einen Administrator fuer die lokale Installation hinzufuegen:
```
django-admin createsuperuser
```
Webserver starten mit
```
python manage.py runserver
```
Und den [Link](localhost:8080) Browser (auf dem selben Geraet) oeffnen.


## Bot(s) starten
Die oberen Schritte waren einmalig, vom Projektordner aus kann der bot von jetzt an immer ueber die `manage.py` gestartet werden und er läuft bis er crashed (oder strg+c). Die management Befehle funktionieren wie scripte, die aufgerufen werden, nachdem die django settings gelesen und initialisiert werden, das heisst in diesen scripten stehen DB Models, settings und logger bereits zur Verfuegung.

```
python manage.py botpolling --username=<username_bot>
```
