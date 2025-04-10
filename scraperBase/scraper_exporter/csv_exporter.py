import csv

from base_exporter import BaseExporter

class CSVExporter(BaseExporter):
    def export(self, data: dict, path: str = None):
        with open('archivo.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(data.keys())
            writer.writerows(data.values())
