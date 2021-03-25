class Matrix(object):
	def __init__(self, matrix_string):
		self.matrix = matrix_string.split('\n')
		for row_string in self.matrix:
			row_index = self.matrix.index(row_string)
			row_array = row_string.split(' ')
			for string_entry in row_array:
				col_index = row_array.index(string_entry)
				int_entry = int(string_entry)
				row_array[col_index] = int_entry
			self.matrix[row_index] = row_array

	def row(self, index):
		index -= 1
		row_array = self.matrix[index]
		return row_array

	def column(self, index):
		index -= 1
		column_array = []
		for row in self.matrix:
			column_array.append(row[index])
		return column_array
