# PyBaoba
## Show installed OS system package like gnome baobab

The Gnome Baobab is the awesome and simple utility to
see disk usage in Gnome.
https://gitlab.gnome.org/GNOME/baobab/

Sometimes i idealize if the Gnome Baobab has CLI tool
who can export data to a local web page, very useful
when you don't have any Xorg interface or in production
server where usually don't have any GUI interface.

In this release the main goal is.
- Identify OS like
- Determine which package manager
- Get installed packages separate by: Name, Version, Group

By default output is a JSON


This package is in deploy yet don't use in production env,
utils/packformat consume too much ram.
