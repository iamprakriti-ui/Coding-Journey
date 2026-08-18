# Get input for rows and columns
rows = int(input())
cols = int(input())

# Outer loop for rows
row_string = ""
for i in range(rows):
    # Inner loop for columns
    row = ""
    for j in range(cols):
        row += "*"
        # Print the completed row
    print(row)
