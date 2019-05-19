from xlsxwriter import Workbook


excel_file = Workbook("teste.xlsx")
planilha = excel_file.add_worksheet()

planilha.set_column('A:A', 20)
planilha.set_column('B:B', 20)

bold = excel_file.add_format({'bold': True})

planilha.write(0, 0, "FRUTAS", bold)
planilha.write(0, 1, "LEGUMES", bold)

planilha.write("A2", "Maca")
planilha.write("B2", "Cenoura")

planilha.write("A3", "Pera")
planilha.write("B3", "Batata")

planilha.write("A4", "Morango")
planilha.write("B4", "Cebola")

planilha.write("A5", "Limao")
planilha.write("B5", "Beringela")

planilha.insert_image("D1", "logo.png")

excel_file.close()
