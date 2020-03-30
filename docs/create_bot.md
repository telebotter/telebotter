# Neuen Bot erstellen
Ein kurzer Guide um einen neuen Bot zu erstellen, der sich gut ins
Telebotter-Projekt einbinden lässt. Dabei kann optional mit dem bottemplate
gestartet werden.

## Vorbereitung
1. Bot im Botfather erstellen. Der Name kann deutsch oder denglisch sein (zumindest solange der Bot auch auf deutsch ist), da viele englischen Namen bereits vergeben sind. Zuerst wird der Anzeigename angegeben und kann emojis enthalten: `:EM: Name des Bots Bot`. Dann: Hoffen, dass `namedesbotsbot` noch nicht vergeben ist.
2. Neues Repository erstellen. Am besten bei GitHub mit dem namen `namedesbotsbot`. Wenn das Bottemplate verwendet werden soll, ist das einfachste keine README.md anzulegen (wird im vom Template generiert). Die Seite offenlassen um die Befehle (local init) einfach zu kopieren.
3. Sicherstellen, dass das telebotter und das bottemplate repository aktuell ist.

## Aus Template erstellen
Das bottemplate, umfasst allen notwendigen Code um einen Telegrambot als django app zu verwalten. Ausserdem werden bereits seperate dateien `commands.py`, `utils.py` und `constants.py` erstellt und importiert. Der Bot beantwortet den `/start` und `/help` Befehl und weitere Beispiele sind als Kommentare enthalten.

1. App erstellen
Aus dem Projektordner:
```bash
(telebotter)$ python manage.py startapp <namedesbots> --template bottemplate
```
In der `main()` Funktion der `telegrambot.py` muss ggf. noch der username des bots angepasst werden (wenn abweichend vom projektnamen).

2. App registrieren
Damit die App (der Bot) automatisch mit gestartet und überwacht wird, muss er in der `telebotter/settings.py` in die Liste `BOTS = [ ... ]` aufgenommen werden. Eingetragen wird der `<namedesbots>` der auch im letzten Befehl verwendet wurde (falls abweichend zum echten bot name). Ganz unten unter `DJANGO_TELEGRAM_BOTS` den Bot mit seinem `TOKEN` (vom botfather) registrieren. Das setzen der settings (token, appname) im telebotter projekt ist [noch](https://github.com/telebotter/telebotter/issues/20) notwendig, soll aber in eine bot spezifische settings datei verschoben werden.

3. Testen
Jetzt sollte der bot schon laufen. Je nach einstellung kann er über polling
```bash
TODO: startbot command here
```
oder webhook (reload webserver) gestartet werden.

4. Pushen
Ist der Test erfoglrich verlaufen: README.md anpassen alle Dateien committen und ins soeben erstellte GitHub repository pushen.


## From Scratch
TODO: vgl. telegrambot.py und erstelle beispiel datei schritt 2-4 identisch.

## Projekt Integration
Neben dem notwendigen Eintrag des tokens kann der bot optional auf der telebotter website gelistet werden, der status des bots angezeigt werden sowie ein zugriff auf die issues des botrepositories durch den metabot gewaehrt werden. Dazu sind folgende (optionale) angaben wichtig:

1. Eintrag in die Liste (webseite):
Im Backend einen Eintrag in der `core/bots` tabelle machen. Token sind nur als backup hinterlegt. botusername und Anzeigename sollten mit den Telegramnamen uebereinstimmen. Die Kurzbeschreibung wird in der Liste angezeigt die Lange, als eigene Seite/Popup wenn keine Website hinterlegt ist. Website und Repo werden als buttons angezeigt wenn links bzw. reponame eingegeben werden.

2. Github Integration
TODO


## Website
Wenn der Bot eine eigene website haben soll laeuft diese normalerweise auf `telebotter.sarbot.de/<projektname>`

TODO

## Logging
Der logger `logging.getLogger(__name__)` schreibt per default in eine extra logfile für den bot (Info) und ab level error in eine gesammelte error datei. Alle Dateien werden um Mitternacht rotiert. 
