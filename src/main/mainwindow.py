# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QMainWindow, QDialog

from src.config import get_logger, get_project_name

from .ui_mainwindow import Ui_MainWindow
from .ui_logdialog import Ui_LogDialog

logger = get_logger()


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, version):
        super(self.__class__, self).__init__()
        self.version = version
        self.setup_ui()

    def setup_ui(self):
        self.setupUi(self)
        self.setWindowTitle(f"{get_project_name()} v{self.version}")

    def add_tool_view(self, index, tool_name, tool_widget):
        self.tabWidget.insertTab(index, tool_widget, tool_name)


class LogFileWindow(QDialog, Ui_LogDialog):

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.ok_btn.clicked.connect(self.close_action)

    def close_action(self):
        self.log_text_edit.clear()
        self.close()

    def show_log_content(self, filepath):
        self.log_file_value.setText(filepath)
        self.log_text_edit.clear()
        with open(filepath, mode='r') as log_content:
            self.log_text_edit.appendPlainText(''.join(log_content.readlines()))
        self.show()
