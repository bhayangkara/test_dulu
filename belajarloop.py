print("Test loop")
a = range(0, 10) #ini untuk string yang mao di looping
for _ in a:
  print(_)
  
b = [f**2 for f in a]
g = [f*f for f in b for f in a]

  
  
