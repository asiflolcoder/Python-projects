print("Creating our own data type-fraction")

class Fraction:
  #parameterized constructor
  def __init__(self,x,y): 
    self.num = x
    self.den = y
    print("Object created")
    
  def __str__(self):
    return '{}/{}'.format(self.num,self.den)
  
  def __add__(self,other):
      new_num = self.num *other.den + self.den *other.num
      new_den = self.den * other.den
      return '{}/{}'.format(new_num , new_den)
    
  def __sub__(self,other):
    new_num = self.num * other.den - other.num * self.den
    new_den = self.den * other.den
    return '{}/{}'.format(new_num,new_den)

  def __mul__(self,other):
    new_num = self.num * other.num 
    new_den = self.den * other.den
    return '{}/{}'.format(new_num,new_den)
  
  def __truediv__(self,other):
    new_num = self.num * other.den
    new_den = self.den * other.num
    return '{}/{}'.format(new_num,new_den)
  
  
fr1 = Fraction(4,5)
fr2 = Fraction(5,6)
print(fr1+fr2)
print(fr1-fr2)
print(fr1*fr2)
print(fr1/fr2)