import openpyxl
lst=[
    [1,2,3],
    [4,5,6]
]
workbook=openpyxl.workbook
sheet=workbook.create_sheet('测试.xlsx')
for i in lst:
    sheet.append(i)
workbook.save('测试.xlsx')
print(workbook.sheetnames)