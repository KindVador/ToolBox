# -*- coding: utf-8 -*-

from src.interfaces.itoolboxmodel import IToolBoxModel
from src.config import get_logger
logger = get_logger()


class MainModel(IToolBoxModel):

    def __init__(self):
        self.tools = dict()
        self.tab_indexes = dict()

    def register_tool(self, name, controller):
        self.tools[name] = controller
        self.tab_indexes[name] = len(self.tab_indexes)
        logger.info(f"Register tool: {name} in the main model")
        return self.tab_indexes[name]

    def unregister_tool(self, name):
        if name in self.tools.keys():
            self.tools.pop(name)
            logger.info(f"Unregister tool: {name} from the main model")
        else:
            logger.error(f"Unknown tool: {name}")
