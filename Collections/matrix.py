matrix = [[1,2,3], 
          [4,5,6], 
          [7,8,9,10]]

rows = len(matrix)

for i in range(rows):
	col = len(matrix[i])
	for j in range(col):
		print(matrix[i][j])


