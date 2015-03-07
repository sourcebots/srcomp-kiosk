#!/usr/bin/env python3

import argparse
import subprocess
import time
import yaml

# Parse arguments to get the config file location

parser = argparse.ArgumentParser(description='srcomp kiosk system')
parser.add_argument('--config', dest='config', help='Config file location '
        '(default: /etc/srcomp-kiosk/config.yaml)',
        default="/etc/srcomp-kiosk/config.yaml")
parser.add_argument('--browser', dest='browser', help='Browser to use '
        '(Chromium recommended, chromium default)',
        default="chromium")

args = parser.parse_args()

configPath = args.config
browser = args.browser

# Disable screensaver

subprocess.call(["xset", "-dpms"])
subprocess.call(["xset", "s", "off"])
subprocess.call(["xset", "s", "noblank"])
subprocess.Popen(["unclutter"])

oldUrl = None
proc = None

while True:
    time.sleep(1)
    try:
        with open(configPath) as f:
            url = yaml.load(f)['url']
            if url != oldUrl:
                if proc != None:
                    proc.kill()
                proc = subprocess.Popen([browser, "--kiosk", "--incognito",
                    "--noerrdialogs", url])
                oldUrl = url
    except IOError as e:
        print(e)
