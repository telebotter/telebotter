> This repository contains the telebotter project folder and is only for development purpose. The bot related stuff is in the corresponding bot repository.

![language](https://img.shields.io/github/languages/top/telebotter/telebotter)
![closed issues](https://img.shields.io/github/issues-closed/telebotter/telebotter)
![Website](https://img.shields.io/website?url=https%3A%2F%2Ftelebotter.sarbot.de)

```
 _____    _      _           _   _         
|_   _|__| | ___| |__   ___ | |_| |_ ___ _ __ 
  | |/ _ \ |/ _ \ '_ \ / _ \| __| __/ _ \ '__|
  | |  __/ |  __/ |_) | (_) | |_| ||  __/ |   
  |_|\___|_|\___|_.__/ \___/ \__|\__\___|_| 
```  


## Ueberblick
Dieses Repo ist der Rootordner des Telebotterprojekts. 
Es enthaelt den Code fuer die Website und Botuebergreifende Einstellungen. 
Jeder Bot hat ein eigenes Repository, das lokal in dieses Repository geklont werden kann. 
Ist der Bot als Djangoapp angelegt, kann er (appname und token) in die settings.py eingetragen werden. 
Dort eingetragene Bots werden vom Webserver serviert und ueberwacht. 
Django models, werden direkt in der Telebotterdatenbank gespeichert.
Bots koennen auf der Website gelisted werden und/oder eine eigene Weboberflaeche mitbringen.

## Lokale Installation
[Installationsanleitung](https://github.com/telebotter/telebotter/blob/master/INSTALL.md)

## Neuen Bot erstellen

### 1. App aus Template erstellen
In der aktivierten Umgebung (`conda activate telebotter`) im Projektverzeichnis (`telebotter`) kann eine neuer bot nach einem Template erstellt werden:
```
python manage.py startapp --template=templates/telegrammbot <app_name>
```
Dies erstellt einen Ordner mit dem Namen der App. Darin befindet sich der eigentliche bot (`telegrambot.py`) sowie eine Vorlage fuer Datenbanktabellen (`models.py`) und Webseiten (`views.py`). Und ein paar Ordner die ggf. spaeter oder von Django benoetigt werden.

### 2. Bot im Projekt eintragen
Damit der Bot serviert wird, muss sein token und der <app_name> in die `telebotter/settings.py` eingetragen werden. Der name der app (=name des ordners/moduls) wird der Liste von `INSTALLED_APPS` hinzugefuegt. Wo der Token gesetzt und der Bot gestartet wird, haengt davon ab, ob er als script (local) oder ueber den Webserver gestartet werden soll.

__a) Webserver__ Der Token kommt in das Dictionary `DJANGO_TELEGRAMBOT` sollte selbsterklaerend sein anhand der anderen Beispiele. Der Bot kann jetzt durch ausfuehren der bot datei gestartet werden:
```bash
python telegrambot.py
```

__b) Lokal__ Der Token kommt in das Dictionary `DEV_TOKENS` oder als eigene Variable und muss entsprechend in der `telegrambot.py` gelesen werden. Wenn der Bot selbst funktioniert, kann er durch ein Neustart des Webservers
```bash
sudo service apache2 reload  # restart oder force-reload bei Fehler
```
aktiviert werden. Wenn wir auf nummer sichergehen wollen, waere es gut den app ordner noch der `.gitignore` dieses Repositories hinzuzufuegen, damit man nicht versehentlich, das eine Repo dem anderen hinzufuegt.. zumindest, bis wir eine bessere Loesung haben #5.

__Optional__ koennen noch spezielle Logfiles festgelegt werden, ansonsten werden nur fehler in `telegram_error` und aufwaerts geloggt. Sollte vorallem fuer die laufenden Bots wichtig sein, weniger fuer die in der Entwicklung. (Siehe Kapitel Logging)

### 4. Optional: Repository erstellen
Wenn der Botcode Open Source sein soll, ein neues Repository (`telebotter/<app_name>`) erstellen ohne irgendetwas hinzuzufuegen. Im Template befindet sich bereits eine `.gitignore`, sodass theoretisch alles andere mit `*` hinzugefuegt werden kann. Jedoch sollte diese vorher einmal geprueft, oder nur ausgewaehlte Dateien commited werden, damit keine Tokens oder Passwoerter veroeffentlicht werden. __Vom App-Ordner (`telebotter/<app_name>`) aus__ kann der neue Bot ins Repository geschoben werden mit:

```bash
git init
git add *
git commit -m 'new bot'
git remote add origin git@github.com:telebotter/<app_name>.git
git push -u origin master
```

## Logging
Das Logging wird in der `telebotter/setup.py` configuriert. Auf dem Server wird allen installierten Bots automatisch eine logfile (level INFO -> `botname.log`) zugewiesen. Hoehere level (WARNING) gehen zusaetzlich in den Telegramchat und ERRORs werden mit Traceback in einer gemeinsamen `error.log` Datei gesammelt. Debug Nachrichten werden nicht ausgegeben koennen im Bedarfsfall an die Konsole (im pollmode) oder in eine `debug.log` geschrieben werden.

Alle Logfiles werden taeglich (0uhr) archiviert und 7 Tage aufbewahrt. In den Dateien befinden sich also nur tagesaktuelle Nachrichten. Die Archive liegen im selben Verzeichnis mit entspraechend angepasster Dateiendung.

Sollte der Fehler schon vor der Konfiguration der logger auftreten, oder das gesamte Projekt crashen, findet sich vermutlich eine Fehlermeldung vom webserver in der `error_log` im selben Verzeichnis.

## Troubleshooting

### Servererror 500
Bei einem Servererror sollte wenigstens eine Fehlermeldung im web_error.log auftauchen. Vermutlich auch schon eine im django_error.log. Wenn kein Zugriff auf die files moeglich ist, oder keine hilfreichen Fehler gefunden werden, kann in den settings.py debug aktiviert werden. Dies sollte allerdings nur in einer Testumgebung geschehen und ist keine Dauerloesung, da Django bei Fehlern Tracebacks und Variablenwerte als Webansicht ausgibt.

### Telegram Errors
telegram_error.log

### Aenderung in models.py
```
python manage.py makemigrations
python manage.py migrate
```

### RuntimeError("populate() isn't reentrant")

Details in Issue #6

### Direkter Zugriff auf die DB
Wenn noetig sag bescheid, ansonsten sollte erstmal Djangoadmin ausreichen.


### Webserver neustarten
Ueber ssh auf dem Server.
```
# service apache2 restart
```
