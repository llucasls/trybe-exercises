def star_block(side):
    for index in range(side):
        print('*' * side)

def block(side):
    SQUARE = '██'
    for index in range(side):
        print(SQUARE * side)
