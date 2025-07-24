import openpyxl
from utils.config import get_config


# Get Rows and Column  in testdata excel sheet.
def get_cell_data(row_index, column_name):
    try:
        # Get config values
        config = get_config()
        excel_path = config["excel_path"]
        sheet_name = config["sheet_name"]
        
        # Load the workbook and sheet
        workbook = openpyxl.load_workbook(excel_path)
        sheet = workbook[sheet_name]

        # Find the column number for the given column name
        header_row = sheet[1]  # The first row contains headers (1-based index)
        col_num = None
        for cell in header_row:
            if cell.value.strip().lower() == column_name.lower():
                col_num = cell.column
                break

        if col_num is None:
            raise RuntimeError(f"Column not found: {column_name}")

        # Get the value from the specified row and column
        row = sheet[row_index]  # 1-based index, so row_index=1 refers to the second row
        return row[col_num - 1].value  # openpyxl uses 0-based index for rows, so subtract 1 from col_num
    except Exception as e:
        raise RuntimeError(e)
