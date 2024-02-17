# Input: Column and row numbers for two cells on a chessboard
column1 = int(input("Enter the column number of the first cell: "))
row1 = int(input("Enter the row number of the first cell: "))
column2 = int(input("Enter the column number of the second cell: "))
row2 = int(input("Enter the row number of the second cell: "))

# Determine the color of each cell (even+even or odd+odd are black; otherwise white)
cell1_color = (column1 + row1) % 2
cell2_color = (column2 + row2) % 2

# Check if both cells are of the same color
if cell1_color == cell2_color:
    output = "Yes"
else:
    output = "No"

# Print the output message
print(output)
