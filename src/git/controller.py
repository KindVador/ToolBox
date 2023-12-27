# -*- coding: utf-8 -*-
from src.interfaces.itoolboxcontroller import IToolBoxController

from .model import GitModel
from .view import GitView

from src.config import get_logger
logger = get_logger()


class GitController(IToolBoxController):

    def __init__(self):
        super(self.__class__, self).__init__()
        logger.debug(f"GitController.__init__()")
        self.set_model(GitModel())
        self.set_view(GitView())

    def __call__(self, *args, **kwargs):
        logger.debug(f"GitController.__call__({args}, {kwargs})")
        self.load_user_preferences()
        self._init_view()
        self.get_view().show()

    def load_user_preferences(self):
        pass

    def _init_view(self):
        pass
