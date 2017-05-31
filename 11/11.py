

grid_file = file("./grid.txt")

# Create 2D Grid
grid_matrix = []
for line in grid_file:
    line_list = str(line).replace('\n','').split(" ")
    grid_matrix.append(map(int,line_list))

max_product = 0

def vertical_pairs():
    m = 0
    for x in range(0,20):
        for y in range(0,17):
            a = grid_matrix[y][x]
            b = grid_matrix[y+1][x]
            c = grid_matrix[y+2][x]
            d = grid_matrix[y+3][x]
            local_product =  a*b*c*d
            if local_product > m:
                m = local_product
    return m

def horizontal_pairs():
    m = 0
    for x in range(0,17):
        for y in range(0,20):
            a = grid_matrix[y][x]
            b = grid_matrix[y][x+1]
            c = grid_matrix[y][x+2]
            d = grid_matrix[y][x+3]
            local_product =  a*b*c*d
            if local_product > m:
                m = local_product
    return m

def diag_max_ud():
    m = 0
    for x in range(0, 17):
        for y in range(0, 17):
            a = grid_matrix[y][x]
            b = grid_matrix[y+1][x + 1]
            c = grid_matrix[y+2][x + 2]
            d = grid_matrix[y+3][x + 3]
            local_product = a * b * c * d
            if local_product > m:
                m = local_product
    return m

def diag_max_du():
    m = 0
    for x in range(3,20):
        for y in range(3, 20):
            a = grid_matrix[y][x]
            b = grid_matrix[y-1][x - 1]
            c = grid_matrix[y-2][x - 2]
            d = grid_matrix[y-3][x - 3]
            local_product = a * b * c * d
            if local_product > m:
                m = local_product
    return m

product_max = [vertical_pairs(), horizontal_pairs(), diag_max_ud(), diag_max_du()]
print max(product_max)