x1, y1, x2, y2, x3, y3 = eval(input('Enter three points for a triangle: '))
side1 = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
side2 = ((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3)) ** 0.5
side3 = ((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1)) ** 0.5

s = (side1 + side2 + side3) / 2
area = (s*(s-side1)*(s-side2)*(s-side3)) ** 0.5
print(f'The area of the triangle is {area:.1f}')