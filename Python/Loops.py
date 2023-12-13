# While Loop

i = 1

while i <= 6:
      print("You Are The Best")
      
      i+=1
      
      
# print number using while loop

i =1

while i<=10 :
      print(i)
      i+=1
      
# print even number using while loop

i=0

while i<=10 :
      if i % 2 == 0:
            print(i)
      i+=1
      
# print sum of numbers

i =1
add=0

while i<=10:
      add+=i
      print(add)
      i+=1
      
      
# For Loop

n= int(input())

for i in range(1,12):
      print(i*n)
      
      
# print simple pattern

for i in range(4):
      for j in range(4):
            print("*", end=" ")
      print()
      
      
# Star pattern

n= int(input())

for i in range(1,n+1):
      for j in range(i):
            print("*", end=" ")
      print()
      
      
# Break continue statment


for i in range(1,10):
      if i ==5:
            continue
      print(i)
      
      
for i in range(1,10):
      if i ==5:
            continue
      print(i)




