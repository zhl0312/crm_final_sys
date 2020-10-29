import xlrd


class OperationExcel:
    def __init__(self,path,sheet_name):
        self.workbook = xlrd.open_workbook(path)
        self.sheet = self.workbook.sheet_by_name(sheet_name)

    def get_ncol(self):
        return self.sheet.ncols

    def get_row(self):
        return self.sheet.rows

    def get_cell(self,row,col):
        cell_v = self.sheet.cell_value(row,col)
        if cell_v == 'null':
            return ''
        return cell_v