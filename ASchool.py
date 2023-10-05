score = int (input())

if 90 <= score <= 100:
   print('A')
elif 85 <= score <= 89: 
   print('B+')
elif 80 <= score <= 84:
   print('B')
elif 75 <= score <= 79:
   print('C+')
elif 70 <= score <= 74:
   print('C')
elif 65 <= score <= 79:
   print('D+')
elif 60 <= score <= 64:  
   print('D')
elif 0 <= score <= 59:
   print('F')