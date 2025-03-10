import urllib.request
from enum import Enum

class HTML(Enum):
    TABLE_B = "<table"
    TABLE_E = "</table>"
    TR_B = "<tr"
    TR_E = "</tr>"
    TD_B = "<td"
    TD_E = "</td>"
    TD_VALUE_B = "<span class="
    TD_VALUE_E = "</span>"

class GRID:
    def __init__(self, x=0, c="", y=0):
        self.x = x
        self.c = c
        self.y = y


class DecodingSecretMessage:

    def __init__(self):
        self.url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"

    def read_url_connection(self):
        print("read_url_connection")
        f = urllib.request.urlopen(self.url)
        content_as_string = str(f.read())
        start = content_as_string.index(HTML.TABLE_B.value)
        end = content_as_string.index(HTML.TABLE_E.value) + len(HTML.TABLE_E.value)
        return content_as_string[start:end]

    def parse_url_content(self, table):
        print("parse_url_content")
        # extract tr
        table_as_string = str(table)
        tr_list = []
        start = 0
        while True:
            fr = table_as_string.find(HTML.TR_B.value, start)
            if fr == -1:
                break
            to = table_as_string.index(HTML.TR_E.value, start)
            tr = table_as_string[fr : to + len(HTML.TR_E.value)]
            tr_list.append(tr)
            start = to + 1

        # skip table header
        tr_list.pop(0)

        # extract td values
        start = 0
        grid_list = []
        for tr in tr_list:
            # x coordinate
            fr = tr.index(HTML.TD_B.value, start)
            to = tr.index(HTML.TD_E.value, start)
            td = tr[fr : to]
            start = to + 1
            fr = td.index(HTML.TD_VALUE_B.value)
            to = td.index(HTML.TD_VALUE_E.value)
            td_value = td[fr : to]
            fr = td_value.index(">")
            to = len(td_value)
            td_x_value = td_value[fr + 1 : to]
            # character
            fr = tr.index(HTML.TD_B.value, start)
            to = tr.index(HTML.TD_E.value, fr)
            td = tr[fr : to]
            start = to + 1
            fr = td.index(HTML.TD_VALUE_B.value)
            to = td.index(HTML.TD_VALUE_E.value)
            td_value = td[fr : to]
            fr = td_value.index(">")
            to = len(td_value)
            td_c_value = td_value[fr + 1 : to]
            # y coordinate
            fr = tr.index(HTML.TD_B.value, start)
            to = tr.index(HTML.TD_E.value, fr)
            td = tr[fr : to]
            fr = td.index(HTML.TD_VALUE_B.value)
            to = td.index(HTML.TD_VALUE_E.value)
            td_value = td[fr : to]
            fr = td_value.index(">")
            to = len(td_value)
            td_y_value = td_value[fr + 1 : to]
            start = 0
            grid = GRID(int(td_x_value), td_c_value, int(td_y_value))
            grid_list.append(grid)
        return grid_list

    def patch_with_unicode(self, grid):
        print("patch_with_unicode")
        for i in range(len(grid)):
            match i:
                case 0 | 1 | 2:
                    grid[i].c = "\u2588"
                case _:
                    grid[i].c = "\u2580"
        return grid

    def to_matrix(self, grid_list):
        x_max = 0
        y_max = 0
        for g in grid_list:
            x_max = max(x_max, g.x)
            y_max = max(y_max, g.y)
        x_max += 1
        y_max += 1
        rows, cols = (y_max, x_max)
        matrix = [[None for i in range(cols)] for j in range(rows)]
        for g in grid_list:
            matrix[g.y][g.x] = g.c
        return matrix

    def print_matrix(self, matrix):
        print("print_matrix")
        for m in matrix:
            print()
            for ch in m:
                str = ""
                if ch != None:
                    str = str + ch
                else:
                    str = str + ' '
                print(str, end='')



if __name__ == '__main__':

    decoder = DecodingSecretMessage()
    table = decoder.read_url_connection()
    grid = decoder.parse_url_content(table)
    grid = decoder.patch_with_unicode(grid)
    matrix = decoder.to_matrix(grid)
    decoder.print_matrix(matrix)
