class DecodingSecretMessage:

    def __init__(self):
        self.url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"

    def read_url_connection(self):
        print("read_url_connection " + self.url)
        return "table"

    def parse_url_content(self, table):
        print("parse_url_content String " + table)
        return "grid"

    def patch_with_unicode(self, grid):
        print("patch_with_unicode GRID[] " + grid)
        return "grid"

    def to_matrix(self, list):
        print("to_matrix String[][] " + grid)
        return "matrix"

    def print_matrix(self, matrix):
        print("print_matrix " + matrix)
        return "matrix"


if __name__ == '__main__':

    decoder = DecodingSecretMessage()
    table = decoder.read_url_connection()
    grid = decoder.parse_url_content(table)
    grid = decoder.patch_with_unicode(grid)
    matrix = decoder.to_matrix(grid)
    decoder.print_matrix(matrix)
