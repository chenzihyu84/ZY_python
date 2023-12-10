import math
import pyinputplus as pyip

def circle_area(radius):
    area = radius ** 2 * math.pi
    return area





radius = pyip.inputFloat("請輸入半徑:")
print(radius)
area = circle_area(radius)
print(f"半徑{radius},園面積是{area}")