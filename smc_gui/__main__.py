# File: main.py
import sys
import os
# import xdg
import subprocess
import logging
import urllib.request
# import contextlib
# from itertools import islice
# from more_itertools import islice_extended

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (QApplication, QMessageBox, QFileDialog)
from PySide6.QtCore import QFile, QIODevice, QCoreApplication, Qt
from PySide6.QtGui import QIcon

TOOL = "spectre-meltdown-checker"
PROG = "spectre-meltdown-checker GUI"
VERSION = "0.1.2"
AUTHOR = "Copyright (C) 2023, 2024, by Michael John"
DESC = "A simple GUI for spectre-meltdown-checker"
GithubLink = "https://github.com/amstelchen/smc_gui"

sheet = """
QGroupBox {
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);
    border: 2px solid gray;
    border-radius: 5px;
    margin-top: 1ex; /* leave space at the top for the title */
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left; /* position at the top center */
    margin-left: 3 px;
    padding: 0 3px;
}"""

def main():
    ResultFilePath = "/tmp/smc_output_nohw.txt"
    data = {}

    def ReadResultFile(ResultFilePath):
        logging.debug(f"Reading {ResultFilePath}...")
        with open(ResultFilePath, "rt") as result_file:
            try:
                tool_name = result_file.readline()
                result_file.readline()
                result_file.readline()
                kernel = result_file.readline()
                cpu = result_file.readline()
                result_file.readline()
            except ValueError:
                result_file.seek(0)
                # do nothing
            finally:
                window.label_Systeminfo.setText(f"{tool_name}{kernel}{cpu}")
            logging.debug(f"{tool_name}{kernel}{cpu}")

            cve_count = 0
            for line in result_file.readlines(): # list(islice_extended(result_file, 5, -2)):
                cond1 = [  # noqa: F841
                    not str(line).startswith("*"), 
                    not str(line).startswith(" "), 
                    not str(line).startswith(">"),
                    not str(line).startswith("\n")
                ]
                cond2 = [
                    not str(line).startswith("> SUMMARY"),
                    "--explain" not in str(line),
                    "--disclaimer" not in str(line)
                ]
                if str(line).startswith('CVE'):
                    subs = []
                    cve = line.split(' ')[0]
                    data[cve] = []
                    logging.debug(f"{cve} found in file.")
                    cve_count += 1
                    window.listWidget.insertItem(
                        window.listWidget.count(), line.strip().replace('aka', '\n  aka'))
                elif all(cond2):
                    subs.append(line)
                    data[cve] = subs
            logging.debug(f"There were a total of {cve_count} CVEs found in the file.")

    def action_Run_checker_clicked(s):
        try:
            with open(ResultFilePath, "wt") as result_file:
                subprocess.run(["pkexec", TOOL, "--no-color", "--no-hw"], stdout=result_file) # capture_output=True
        except Exception as e:
            logging.debug(f"{e}")
        finally:
            ReadResultFile(ResultFilePath)

    def action_Open_file_clicked(s):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.ExistingFile)
        ResultFilePath, _ = dialog.getOpenFileName(window)
        if ResultFilePath != "":
            ReadResultFile(ResultFilePath)

    def actionVisit_clicked(s):
        if sys.platform == "linux":
            subprocess.run(["xdg-open", GithubLink])

    def actionAbout_clicked(s):
        QMessageBox.about(window, PROG + " " + VERSION, PROG + "\n" + VERSION  + "\n" + DESC + "\n" + AUTHOR)

    def actionExit_clicked(s):
        sys.exit()

    def ShowDetail():
        cve_num = window.listWidget.currentItem().text().split()[0]
        cve_title = window.listWidget.currentItem().text()
        logging.debug(f"{cve_num} selected.")
        cve_data = '<p>'.join(data[cve_num])
        cve_data = cve_data.replace(': VULNERABLE', ': <span style=" font-weight:700; background-color:red;">VULNERABLE</span>')
        cve_data = cve_data.replace(': NOT VULNERABLE', ': <span style=" font-weight:700; background-color:#32CD32;">NOT VULNERABLE</span>')
        cve_data = cve_data.replace('STATUS:', '<span style=" font-weight:700; background-color:#00FFFF;">STATUS:</span>')
        window.label_Details.setText('<b>' + cve_title + '</b><p>' + cve_data)
    
    def CheckUpdate():
        window.label_Systeminfo.setText("Checking for latest version of spectre-meltdown-checker...")
        installed = subprocess.run(["sh", "-c", "grep '^VERSION' $(which " + TOOL + ")"], capture_output=True).stdout.decode('utf-8').split('=')[1].strip()
        contents = urllib.request.urlopen("https://meltdown.ovh").read().decode('utf-8')
        for line in contents.split('\n'):
            if line.startswith("VERSION="):
                version = line.split('=')[1].strip()
        window.label_Systeminfo.setText(window.label_Systeminfo.text() + f"\nInstalled: {installed}, available: {version}.")
        window.label_Systeminfo.setText(window.label_Systeminfo.text() + "\nPlease open an existing result file, or run spectre-meltdown-checker.")

    if len(sys.argv) > 1:
        loglevel = sys.argv[1]
    else:
        loglevel = "INFO"
    numeric_level = getattr(logging, loglevel.upper(), logging.INFO)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(format='%(levelname)s:%(message)s', level=numeric_level)

    #os.environ["PYSIDE_DESIGNER_PLUGINS"]=os.path.dirname(__file__)
    #app = QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    #app = QApplication.setAttribute(Qt.AA_ShareOpenGLContexts, False)
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

    app = QApplication(sys.argv)
    #QCoreApplication.setAttribute(QtCore Application.Qt", True)
    #app.setAttribute(attribute) # Qt::AA_ShareOpenGLContexts

    ui_file_name = os.path.dirname(__file__) + "/smc_gui.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        logging.debug(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        logging.debug(loader.errorString())
        sys.exit(-1)

    icon = QIcon(os.path.dirname(__file__) + "/smc_gui.png")

    window.setWindowTitle(PROG + " " + VERSION)

    #window.windowIcon = icon
    window.setWindowIcon(icon)
    window.setStyleSheet(sheet)

    window.show()

    window.action_Run_checker.triggered.connect(action_Run_checker_clicked)
    window.action_Open_file.triggered.connect(action_Open_file_clicked)
    window.action_Visit.triggered.connect(actionVisit_clicked)
    window.action_About.triggered.connect(actionAbout_clicked)
    window.action_Exit.triggered.connect(actionExit_clicked)
    window.listWidget.currentItemChanged.connect(ShowDetail)

    print(PROG + ' ' + VERSION + '\n' + AUTHOR) 

    CheckUpdate()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
