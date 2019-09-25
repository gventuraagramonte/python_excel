from openpyxl import load_workbook

filesheet = "./demosheet.xlsx"

wb = load_workbook(filesheet)

sheet = wb.active

datos = [('id', 'nombre','edad'),
        (0,'Jose',29),
        (1,'Sofia',24),
        (2,'Carlos',36)]


for row in datos:
    sheet.append(row)


wb.save(filesheet)