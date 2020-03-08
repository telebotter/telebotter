# Neuen Bot erstellen
Ein kurzer Guide um einen neuen Bot zu erstellen, der sich gut ins
Telebotter-Projekt einbinden lässt. Dabei kann optional mit dem bottemplate
gestartet werden.

## Vorbereitung
1. Bot im Botfather erstellen. Der Name kann deutsch oder denglisch sein (zumindest solange der Bot auch auf deutsch ist), da viele englischen Namen bereits vergeben sind. Zuerst wird der Anzeigename angegeben und kann emojis enthalten: `:EM: Name des Bots Bot`. Dann: Hoffen, dass `namedesbotsbot` noch nicht vergeben ist.
2. Neues Repository erstellen. Am besten bei GitHub mit dem namen `namedesbots` (ohne zusaetzliches `bot` am Ende). Wenn das bottemplate verwendet werden soll, ist das einfachste keine README.md anzulegen (diese wird im naechsten Schritt generiert). Die Seite direkt offenlassen um die Befehle (local init) einfach zu kopieren.
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
Damit die App (der Bot) automatisch mit gestartet und überwacht wird, muss er in der `telebotter/settings.py` in die Liste `BOTS = [ ... ]` aufgenommen werden. Eingetragen wird der `<namedesbots>` der auch im letzten Befehl verwendet wurde (falls abweichend zum echten bot name). Ganz unten unter `DJANGO_TELEGRAM_BOTS` den Bot mit seinem `TOKEN` (vom botfather) registrieren.

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

## Website
Wenn der Bot eine eigene website haben soll laeuft diese normalerweise auf `telebotter.sarbot.de/<projektname>`
