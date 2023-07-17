# tsv.py

from ..formatter import TableFormatter

class TSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print('\t'.join(headers))
    def row(self, rowdata):
        print('\t'.join(str(d) for d in rowdata))
