> This repository contains the telebotter project folder and is only for development purpose. The bot related stuff is in the corresponding bot repository.


## Ueberblick
Dieses Repo ist der Rootordner des Telebotterprojekts. 
Es enthaelt den Code fuer die Website und Botuebergreifende Einstellungen. 
Jeder Bot hat ein eigenes Repository, das lokal in dieses Repository geklont werden kann. 
Ist der Bot als Djangoapp angelegt, kann er (appname und token) in die settings.py eingetragen werden. 
Dort eingetragene Bots werden vom Webserver serviert und ueberwacht. 
Django models, werden direkt in der Telebotterdatenbank gespeichert.
Bots koennen auf der Website gelisted werden und/oder eine eigene Weboberflaeche mitbringen.

## Installation
Siehe [Installation am Beispiel Projekt47](https://github.com/telebotter/projekt47)
