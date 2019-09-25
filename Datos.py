from openpyxl import load_workbook

filesheet = "./demosheet.xlsx"

wb = load_workbook(filesheet)

sheet = wb.active

sheet['C2'] = 345

sheet['A2'] = 23

sheet['B5'] = 10

wb.save(filesheet)