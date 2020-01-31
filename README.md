> This repository contains the telebotter project folder and is only for development purpose. The bot related stuff is in the corresponding bot repository.


## Ueberblick
Dieses Repo ist der Rootordner des Telebotterprojekts. 
Es enthaelt den Code fuer die Website und Botuebergreifende Einstellungen. 
Jeder Bot hat ein eigenes Repository, das lokal in dieses Repository geklont werden kann. 
Ist der Bot als Djangoapp angelegt, kann er (appname und token) in die settings.py eingetragen werden. 
Dort eingetragene Bots werden vom Webserver serviert und ueberwacht. 
Django models, werden direkt in der Telebotterdatenbank gespeichert.
Bots koennen auf der Website gelisted werden und/oder eine eigene Weboberflaeche mitbringen.

## Lokale Installation
Siehe [Installation am Beispiel Projekt47](https://github.com/telebotter/projekt47)

## Neuen Bot erstellen

## Maintain

### Servererror 500
Bei einem Servererror sollte wenigstens eine Fehlermeldung im web_error.log auftauchen. Vermutlich auch schon eine im django_error.log. Wenn kein Zugriff auf die files moeglich ist, oder keine hilfreichen Fehler gefunden werden, kann in den settings.py debug aktiviert werden. Dies sollte allerdings nur in einer Testumgebung geschehen und ist keine Dauerloesung, da Django bei Fehlern Tracebacks und Variablenwerte als Webansicht ausgibt.

### Telegram Errors
telegram_error.log

### Aenderung in models.py
```
python manage.py makemigrations
python manage.py migrate
```

### Direkter Zugriff auf die DB
Wenn noetig sag bescheid, ansonsten sollte erstmal Djangoadmin ausreichen.


### Webserver neustarten
Ueber ssh auf dem Server.
```
# service apache2 restart
```
