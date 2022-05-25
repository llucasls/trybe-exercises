from math import ceil

def paint(wall_size):
    paint_amount = wall_size / 3
    paint_cans = ceil(paint_amount / 18)
    price = 80 * paint_cans
    total_price = ceil(price)
    return (paint_cans, total_price)
