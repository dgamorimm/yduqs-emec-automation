

def read_excel(file, column_idx:int):
    max_row = file.max_row
    for idx in range(2, max_row):
        yield file.cell(row=idx, column=column_idx).value