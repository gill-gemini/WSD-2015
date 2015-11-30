#!/usr/bin/python

import math
class Point:
	
	def __init__(self, x , y ):
		self.x=x
		self.y=y
		
		
	def distance_from(self,p):
		p1=math.pow((self.x-p.x),2)
		p2=math.pow((self.y-p.y),2)
		result=math.sqrt(p1+p2)
		
		return result
		

class Circle(Point):
	
	def __init__(self,center, radius):
		self.center=center
		self.radius=radius
		
	def is_inside(self,p):
		p3= math.pow((p.x - self.center.x),2) 
		p4= math.pow((p.y - self.center.y),2) 
		p5 =math.pow((self.radius),2)
		result= p3 + p4 
		if result < p5:
			return True
		else:
			return False
		
#p1 = Point(0,0)
#p2 = Point(2,4)

#k=p1.distance_from(p2)

#circle = Circle(p2,4)
#if(circle.is_inside(p2)):
#	print(False)

#if(circle.is_inside(Point(2,2))):
#	print(True)

#print(k)	
