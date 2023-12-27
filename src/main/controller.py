# -*- coding: utf-8 -*-

from src.interfaces.itoolboxcontroller import IToolBoxController
from .mainwindow import MainWindow
from .model import MainModel

from src.config import get_logger
logger = get_logger()


class MainController(IToolBoxController):

    def __init__(self, ctx, version):
        super(self.__class__, self).__init__()
        logger.debug(f"MainController.__init__({ctx}, {version})")
        self.ctx = ctx
        self.app = ctx.app
        self.app.setStyle('fusion')
        self.cfg = None
        self.set_view(MainWindow(version))
        self.set_model(MainModel())

    def __call__(self, *args, **kwargs):
        logger.debug(f"MainController.__call__({args}, {kwargs})")
        self.load_user_preferences()
        self._init_view()
        self.get_view().show()

    def load_user_preferences(self):
        pass

    def _init_view(self):
        pass

    def register(self, tool_name, tool_controller):
        # update model
        model = self.get_model()
        index = model.register_tool(tool_name, tool_controller)
        # update view
        view = self.get_view()
        view.add_tool_view(index, tool_name, tool_controller.get_view())

    def unregister(self, tool_name):
        model = self.get_model()
        model.unregister_tool(tool_name)
