# SRComp Kiosk

This is a general purpose Kiosk application. It runs a WebKit based web
browser pointed at a url provided in a config file and then watches that
config file for changes.

## Pre-reqs

The kiosk runs on Python 3 and relies on PySide's QtCore, QtGui and
QtWebKit to run the actual browser.

## Running

You can run the full kiosk using `./kiosk.py`. This gets its config from
`/etc/srcomp-kiosk/config.yaml`, though this can be changed via an argument.

Quitting the process can be done via Ctrl+backslash (Ctrl+C won't work),
or by closing (Alt+F4) the window it creates.

## Developing

You can run just the browser using `./browser.py`, which uses the provded
`testconf.yaml` config file.
