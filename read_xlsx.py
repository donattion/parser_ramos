import openpyxl


FILE_NAME = 'data.xlsx'
book = openpyxl.open(FILE_NAME)
sheet = book.active


def read(number: int) -> str:
    text = str(sheet[f'A{number}'].value)
    return "".join(text.split())


def write(symbol, number: int, value):
    sheet[f'{symbol}{number}'] = value


def max_rows() -> int:
    return sheet.max_row

def save():
    book.save(FILE_NAME)
