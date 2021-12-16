
def type_logger(tl):
   def decor(*args):
      result = tl(*args)
      return f'{result}: <class "int">\ncalc_cube({result}: <class "int">)'
   return decor

@type_logger
def calc_cube(x):
   return x ** 3

print(calc_cube(5))