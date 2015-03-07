#!/usr/bin/env python3

import os.path
import PySide.QtCore
import PySide.QtGui
import PySide.QtWebKit
import sys
import yaml

class Browser():
    def __init__(self, configPath):
        self.app = PySide.QtGui.QApplication(sys.argv)
        self.web = PySide.QtWebKit.QWebView()
        self.configPath = configPath
        self.fileWatcher = PySide.QtCore.QFileSystemWatcher(None)
        self.oldUrl = None

    def updateWebView(self):
        try:
            with open(self.configPath, 'r') as f:
                url = yaml.safe_load(f)['url']
                if self.oldUrl != url:
                    print("Loading new url " + url
                            + " (was " + (self.oldUrl or "None") + ")")
                    self.web.load(PySide.QtCore.QUrl(url))
                    self.oldUrl = url
        except IOError:
            print("File didn't exist") # Error is fine, as some text editors
                                       # momentarily delete the file. So print
                                       # debug message but don't do anything.

    def go(self):
        self.fileWatcher.addPath(self.configPath)
        # Add the directory too, to avoid issues with text editors that delete
        # then rename
        self.fileWatcher.addPath(os.path.dirname(os.path.abspath(
            self.configPath)))
        self.fileWatcher.fileChanged.connect(self.updateWebView)
        self.fileWatcher.directoryChanged.connect(self.updateWebView)

        self.updateWebView()
        self.web.showFullScreen()

        # Hide the cursor
        self.app.setOverrideCursor(PySide.QtCore.Qt.BlankCursor)

        sys.exit(self.app.exec_())

if __name__ == '__main__':
    mydir = os.path.dirname(os.path.realpath(__file__))
    configPath = os.path.join(mydir, 'testconf.yaml')
    web = Browser(configPath)
    web.go()
