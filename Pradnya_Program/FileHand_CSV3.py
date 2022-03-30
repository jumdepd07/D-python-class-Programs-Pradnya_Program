print("Program to print the particular cell value ")
import openpyxl
file_name = r"D:\\python class\\Programs\\Pradnya_Program\\Openpyxl Data1.xlsx"

wb = openpyxl.load_workbook(file_name)

ws = wb.active

read_cell = ws.cell(row=2,column=3)

print(read_cell.value)
