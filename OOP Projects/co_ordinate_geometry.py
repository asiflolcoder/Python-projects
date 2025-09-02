class Point:
  def __init__(self,x,y):
    self.x_cod = x
    self.y_cod = y
  
  def __str__(self):
    return '<{},{}>'.format(self.x_cod,self.y_cod)
    
  
  def euclidean_distance(self,other):
    x = (self.x_cod - other.x_cod)**2
    y = (self.y_cod - other.y_cod)**2
    return ((x+y)**0.5)
    
  def distance_from_origin(self):
    x = self.x_cod**2
    y = self.y_cod **2
    distance = (x+y)**0.5
    return distance
  ## return self.euclidean_distance(self,Point(0,0))

class Line:
  def __init__(self,A,B,C):
    self.a = A
    self.b = B
    self.c = C
  
  def __str__(self):
    return '{}x + {}y + {}'.format(self.a,self.b,self.c)
  
  def point_on_line(line,point):
    lhs = line.a * point.x_cod + line.b * point.y_cod + line.c
    if lhs == 0:
      return "Point lies on the line"
    else:
      return "Does not lies on the line"
  
  def distance_from_line(line,point):
    x = abs(line.a * point.x_cod + line.b * point.y_cod + line.c)
    y = (line.a**2 + line.b**2)**0.5
    return x/y
    
# l1 = Line(1,1,-2)
# print(l1)

# p1 = Point(1,2)
# # p2 = Point(7,8)
# print(p1)

# print(l1.point_on_line(p1)) #l1 is 1st argument and p1 is 2nd argument

# # print(p1.euclidean_distance(p2))
# print(p1.distance_from_origin())

#if two classes /objects are in the 

l1 = Line(1,1,-2)
p1 = Point(1,1)
print(l1.distance_from_line(p1))