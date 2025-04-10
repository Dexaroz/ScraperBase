from base_exporter import BaseExporter
import json

class JSONExporter(BaseExporter):
    def export(self, data: dict, path: str = None):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
