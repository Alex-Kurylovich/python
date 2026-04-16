import urllib.request
import ssl
from enum import Enum

url = "file:///C:./features.html"

from html.parser import HTMLParser

class ColType(Enum):
    TH = "th"
    TD = "td"

class Col:
    def __init__(self, type=ColType.TD, data=''):
        self. type = type
        self.data = data

class Row:
    def __init__(self, cols=None):
        if cols is None:
            self.cols = []
        else:
            self.cols = cols
    def addCol(self, type):
        col = Col(type)
        self.cols.append(col)

class Table:
    def __init__(self, rows=None):
        if rows is None:
            self.rows = []
        else:
            self.rows = rows
    def addRow(self):
        row = Row()
        return self.rows.append(row)

class MyHTMLParser(HTMLParser):

    data_expected = None
    table = Table()

    def handle_starttag(self, tag, attrs):
        global row
        if tag == 'table':
            print("Encountered a start tag:", tag)
        if tag == 'tr':
            print("Encountered a start tag:", tag)
            self.table.addRow()
        if tag == 'th':
            print("Encountered a start tag:", tag)
            self.table.rows[-1].addCol(ColType.TH)
            self.data_expected = True
        if tag == 'td':
            print("Encountered a start tag:", tag)
            self.table.rows[-1].addCol(ColType.TD)
            self.data_expected = True

    def handle_endtag(self, tag):
        if tag == 'table':
            print("Encountered an end tag :", tag)
        if tag == 'tr':
            print("Encountered an end tag :", tag)
        if tag == 'th':
            print("Encountered a end tag:", tag)
            self.data_expected = False
        if tag == 'td':
            print("Encountered a end tag:", tag)
            self.data_expected = False

    def handle_data(self, data):
        if self.data_expected == True:
            print("Encountered some data:", data.splitlines())
            self.table.rows[-1].cols[-1].data = data

def read_and_parse_url_connection():
    print("run read_and_parse_url_connection")
    # Install Certificates.command or:
    ssl._create_default_https_context = ssl._create_unverified_context
    f = urllib.request.urlopen(url)
    content_as_string = str(f.read())
    parser = MyHTMLParser()
    parser.feed(content_as_string)
    return MyHTMLParser.table

def print_table():
    print("run print_table")
    print(len(MyHTMLParser.table.rows))

if __name__ == '__main__':
    read_and_parse_url_connection()
    print_table()
