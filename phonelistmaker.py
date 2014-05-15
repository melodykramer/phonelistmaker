import xlrd

book = xlrd.open_workbook("output031414.xls") # Open an .xls file

sheet = book.sheet_by_index(0) # Get the first sheet




for counter in range(10): # Loop for two times
# grab the current row
	rowValues = sheet.row_values(counter,start_colx=0, end_colx=None)
# Print the values of the row formatted to 10 characters wide
	print "<tr>"	

	print "<td>"

	print rowValues[1]

	print "</td>"


	print "<td>"

	print rowValues[5]

	print "</td>"


	print "<td>"

	print rowValues[9]

	print "</td>"


	print "<td>"

	print rowValues[10]

	print "</td>"


	print "<td>"

	print rowValues[11]

	print "</td>"


	print "<td>"

	print rowValues[12]

	print "</td>"


	print "<td>"

	print rowValues[13]

	print "</td>"


	print "<td>"

	print rowValues[14]

	print "</td>"


	print "<td>"

	print rowValues[15]

	print "</td>"


	print "<td>"

	print rowValues[16]

	print "</td>"


	print "<td>"

	print rowValues[17]

	print "</td>"


	print "<td>"

	print rowValues[18]

	print "</td>"


	print "<td>"

	print rowValues[19]

	print "</td>"


	print "<td>"

	print rowValues[20]

	print "</td>"


	print "<td>"

	print rowValues[21]

	print "</td>"


	print "<td>"

	print rowValues[22]

	print "</td>"




	print "</tr>"
