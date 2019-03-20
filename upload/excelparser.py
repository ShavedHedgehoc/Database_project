class ExcelParser(object, excel_name):
    def read_excel(self):
        xl = pd.ExcelFile(excel_name)
        sh = xl.sheet_names[0]
        r_df = pd.read_excel(xl, sheet_name=sh, dtype=str)