from xlsxwriter import Workbook


excel_file = Workbook("teste.xlsx")
planilha = excel_file.add_worksheet()

planilha.set_column('A:A', 20)
planilha.set_column('B:B', 20)

bold = excel_file.add_format({'bold': True})

# Creating DataSet to create chart
header = ['CATEGORY', 'VALUES']
data = [['Maca', 'Uva', 'Pera', 'Morango'], [30, 13, 17, 40]]

planilha.write_row('A1', header, bold)
planilha.write_column('A2', data[0])
planilha.write_column('B2', data[1])

# Creating Chart
chart = excel_file.add_chart({'type': 'pie'})
chart.add_series({
    'name': 'Fruits liked',
    'categories': ['Sheet1', 1, 0, 4, 0],
    'values': ['Sheet1', 1, 1, 4, 1]
})
chart.set_title({'name': 'My fruits most liked'})
chart.set_style(10)

planilha.insert_chart('D1', chart, {'x_offset': 20, 'y_offset': 25})

# Adding image to plan
planilha.insert_image("A20", "logo.png")

excel_file.close()
