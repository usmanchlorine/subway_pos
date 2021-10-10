import xlwt

from xlwt import Workbook
x=str(input("enter the word"))
w=str(input(("enter the word")))
t = x.upper ( )
Wb=Workbook()

sheet=Wb.add_sheet('sheet 1')
sheet.write(4,3,w)

sheet.write(3,3,x.capitalize())

Wb.save('xlwt example.xls')