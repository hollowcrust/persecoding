for i in range(3):
  a = int(input())
  if(a <= 50):
    if(a&1):
      print('south')
    else:
      print('north')
  else:
    if(a&1):
      print('west')
    else:
      print('east')
