"""
You are given a rectangle in a plane. The corner coordinates of this rectangle is provided to you.
You have to print the amount of area of the plane covered by this rectangles.
The end coordinates are provided as four integral values: x1, y1, x2, y2. It is given that x1 < x2 and y1 < y2.
"""
# Write your code here
x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())
print((x_2-x_1)*(y_2-y_1))