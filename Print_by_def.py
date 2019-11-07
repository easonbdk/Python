def boundary(column, grid_size):
    print((column*("+" + "－"*grid_size))+"+")

def middle(i, column, grid_size, row):
    for i in range(row):
        print((column*("|"+"　"*grid_size)+"|"))
        

def main():
    row = int (input ("Please input row: "))
    column = int (input ("Please input column: "))
    grid_size = int (input ("Please input grid_size: "))
    i = 0
    while i < row:
        boundary(column, grid_size)
        middle(i, column, grid_size, row)
        i = i+1
    boundary(column, grid_size)
main()
