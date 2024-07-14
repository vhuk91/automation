import math

print(dir(int))




dict={"a":1, "b":2, "c":3, "d":4, "e":5}
val=3

def reverse_dict(dict):
   return{value:key for key, value in dict.items()}



rev=reverse_dict(dict)

print(rev.get(val))
