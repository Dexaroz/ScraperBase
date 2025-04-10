from base_exporter import BaseExporter
import json

class SQLITEExporter(BaseExporter):
    def export(self, data: dict, path: str = None):
        return json.dumps(data, indent=4)
