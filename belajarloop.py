print("Test loop")
a = range(0, 10) #ini untuk string yang mao di looping
for _ in a:
  print(_)
  
b = [f**2 for f in a]
#tambah list compre dari team 1
c =[f+f for f in b]

#tambah lagi deh
d = [f+f+f for f in c for f in a]
  
  
