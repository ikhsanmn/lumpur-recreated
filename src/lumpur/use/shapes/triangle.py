# triangle.py
# triangle module
# Sparisoma Viridi | https://github.com/dudung

# 20230524
#   0508 Start this module.
#   1737 Rename r0, r1, r2 to p0, p1, p2.

from butiran.math.vect3 import Vect3
from butiran.entity.color2 import Color2

class Triangle:
  def __init__(
    self, id="0000", m=0, q=0, b=0,
    color=Color2(),
    p0=Vect3(0, 0, 0),
    p1=Vect3(1, 0, 0),
    p2=Vect3(0, 1, 0)
  ):
    self.id = id
    self.p0 = p0
    self.p1 = p1
    self.p2 = p2
    self.m = m
    self.q = q
    self.b = b
    self.color = Color2() 
  
  def __str__(self):
    str = '{\n'
    str += f'  "id": "{self.id}"' + ',\n'
    str += f'  "p0": {self.p0}' + ',\n'
    str += f'  "p1": {self.p1}' + ',\n'
    str += f'  "p2": {self.p2}' + ',\n'
    str += f'  "m": {self.m}' + ',\n'
    str += f'  "q": {self.q}' + ',\n'
    str += f'  "b": {self.b}' + ',\n'
    str += f'  "color": {self.color}' + ',\n'
    str += '}'
    return str
