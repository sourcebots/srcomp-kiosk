#!/usr/bin/env python3

import argparse
import subprocess

import browser

# Parse arguments to get the config file location

parser = argparse.ArgumentParser(description='srcomp kiosk system')
parser.add_argument('--config', dest='config', help='Config file location '
        '(default: /etc/srcomp-kiosk/config.yaml)',
        default="/etc/srcomp-kiosk/config.yaml")

args = parser.parse_args()

configPath = args.config

# Disable screensaver

subprocess.call(["xset", "-dpms"])
subprocess.call(["xset", "s", "off"])
subprocess.call(["xset", "s", "noblank"])

# Start the web browser module
web = browser.Browser(configPath)
web.go()
