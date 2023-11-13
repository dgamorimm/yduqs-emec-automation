

def read_excel_all(file):
    for row in file.iter_rows(min_row=2, max_row=file.max_row):
        yield [cell.value for cell in row]

def read_excel(file, column_idx:int):
    for idx in range(2, file.max_row):
        yield file.cell(row=idx, column=column_idx).value