from abc import ABC, abstractmethod

class BaseExporter(ABC):
    @abstractmethod
    def export(self, data: dict, path: str = None):
        pass