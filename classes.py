# new types using classes
class Point:                  #define new types
    def move(self):           #methods that we define
        print('move')
    def draw(self):
        print('draw')

point1 = Point()
point1.x = 10                #attributes
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)
