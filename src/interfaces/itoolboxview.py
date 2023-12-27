# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class IToolBoxView(ABC):
    @abstractmethod
    def show(self) -> None:
        pass

    @abstractmethod
    def hide(self) -> None:
        pass
