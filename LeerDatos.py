from openpyxl import load_workbook

filesheet = "./demosheet.xlsx"

wb = load_workbook(filesheet)

sheet = wb.active

a2 = sheet['A8'].value
b2 = sheet['B8'].value
c2 = sheet['C8'].value

celdas = [a2,b2,c2]

for celda in celdas:
    print(celda)