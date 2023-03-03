s = input()
if(s == 'electric'):
  print('$0')
else:
  a = float(input())
  if s == 'hybrid':
      if(a < 1.8):
        print('$120')
      else:
        print('$140')
  if s == 'petrol':
      if(a < 1.8):
        print('$150')
      else:
        print('$170')
  if s == 'diesel':
      if(a < 1.8):
        print('$180')
      else:
        print('$200')
