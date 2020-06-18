import os, sys, glob
import random
sys.path.append(os.path.join(os.path.dirname(__file__), 'site-packages'))
import openpyxl as px

EXCEL_FILE = '../excels/'
def find():
    files = glob.glob('{}/*.xls*'.format(EXCEL_FILE))

    all_data = []
    for f in files:
        wb=px.load_workbook(f, data_only=True)
        ws = wb.worksheets[0]
        if ws.cell(row=1, column=1).value == "当たり！":
            print(f)
            break

if __name__ == '__main__':
    find()
