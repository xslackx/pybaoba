# pybaoba
## Show installed OS system package like gnome baobab

The Gnome Baobab is the awesome and simple utility to
see disk usage in Gnome.
https://gitlab.gnome.org/GNOME/baobab/

Sometimes i idealize if the Gnome Baobab has CLI tool
who can export data to a local web page, very useful
when you don't have any Xorg interface or in production
server where usually don't have any GUI interface.
So i decided do create a clone inspired in Baobab 
to visualize the basic host information, system packages
installed, basic disk usage on the web browser.


In this release the main goal is.
- Identify OS like
- Determine which package manager
- Get installed packages separate by: Name, Version, Group

By default output is a JSON


## This package is in deploy yet don't use in production.

Before starting you need at least Python version 3.8.10, pip and venv module 
properly installed on OS.

## to use

Create env to pybaoba

```
python3 -m venv baoba/
```

Install all requirements needed

```
python3 -m pip install -r requirements.txt
```

Starting pybaoba listen on default port 5000

```
source bin/activate && python3 wbaoba.py
```