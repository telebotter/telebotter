## Projekt lokal Klonen

```
git clone git@github.com:telebotter/telebotter.git
```

## Python Umgebung

### Mit Conda

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

Aus dem Projektordner koennen dann alle benoetigten Bibliotheken installiert werden:
```bash
pip install -r requirements.txt
```

## Settings anpassen

Fast alle Einstellungen finden sich in der `telebotter/settings.py`. Darin sind auch Datenbank Logins und Pfade zu logfiles etc. angegeben, daher muss diese Datei auf jedem System individuell angepasst werden. Als Ausgangspunkt kann man sich die Beispieldatei kopieren und den Anweisungen in den Kommentaren folgen:
```bash
cp telebotter/example_settings.py telebotter/settings.py
```

## Bots installieren
siehe README.md
