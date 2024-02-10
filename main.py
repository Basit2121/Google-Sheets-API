def enter_data_in_sheet(generated_data):
    sa = gspread.service_account(filename='noble-beanbag-402311-a10998e0a452.json')
    sheet = sa.open("SCRAPING OUTPUT")
    work_sheet = sheet.worksheet("Blad1")

    columns = ["B","C", "D", "E", "F", "G", "H", "I"]

    values_in_columns = []

    for column_letter in columns:
        values_in_column = work_sheet.col_values(ord(column_letter) - ord('A') + 1)
        empty_cell_index = len(values_in_column) + 1
        cell = f"{column_letter}{empty_cell_index}"
        if len(generated_data) > 0:
            value = generated_data.pop(0)

            if isinstance(value, int):
                value = str(value)
            work_sheet.update_acell(cell, value)
