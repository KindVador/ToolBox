# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from src.interfaces.itoolboxview import IToolBoxView
from src.interfaces.itoolboxmodel import IToolBoxModel

from src.config import get_logger
logger = get_logger()


class IToolBoxController(ABC):

    def __init__(self):
        self._model = None
        self._view = None

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    def get_view(self):
        return self._view

    def set_view(self, view):
        self._view = view

    def display(self, status: bool) -> None:
        if status:
            self._view.show()
        else:
            self._view.hide()

    @staticmethod
    def load_user_preferences(self):
        pass
