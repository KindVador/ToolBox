# -*- coding: utf-8 -*-
import os
from pathlib import Path
import logging


__project_name__ = "DevToolBox"
__project_version__ = "2023.1"
__config_dir__ = os.path.join(str(Path.home()), f".{__project_name__}")


def get_project_name():
    return __project_name__


def get_project_version():
    return __project_version__


def get_config_dir():
    return __config_dir__


def get_logger() -> logging.Logger:
    return logging.getLogger(__project_name__)
