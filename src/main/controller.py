# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger("DevToolBox")


class MainController(object):

    def __init__(self,ctx, version):
        super(self.__class__, self).__init__()
        logger.debug(f"MainController.__init__({ctx}, {version})")
        self.ctx = ctx
        self.app = ctx.app
        self.app.setStyle('fusion')
        self.cfg = None
        self.model = QStandardItemModel(parent=None)
        self.view = MainWindow(version)

    def __call__(self, *args, **kwargs):
        logger.debug(f"QtMainController.__call__({args}, {kwargs})")
        self.load_user_preferences()
        self._init_view()
        self.view.show()