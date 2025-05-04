from geometry import *
#после создания __init__.py
b = stereometry.Ball(5)
a = planimetry.Circle(5)
print(a.square(), b.V())



#до создания __init__.py
#import geometry
#b = geometry.stereometry.Ball(5)
'''AttributeError: module 'geometry' has no attribute 'stereometry. Происходит из-за того, что не указан конкретный файл stereometry'''