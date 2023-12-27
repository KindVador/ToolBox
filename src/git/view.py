# -*- coding: utf-8 -*-
import logging

from PySide6.QtWidgets import QWidget

from src.config import get_project_name
from .ui_gitview import Ui_GitWidget


logger = logging.getLogger(get_project_name())


class GitView(QWidget, Ui_GitWidget):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setupUi(self)
