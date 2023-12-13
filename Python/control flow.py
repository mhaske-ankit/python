# If else statment

age =int(input())

if age > 18 :
      print("you can drive")
      
else:
      print("wait till you turn 18")
      
      
# Nested If else

age = int(input())

if age > 18 :
      if age >=65 :
            print("take rest")
      else:
            print("you can drive")
else:
      print("wait till you turn 18")
      
# If elif and else

num = int(input())

if num > 0 :
      print("positive")
      
elif num == 0:
      print("Zero")
else:
      print("Negative") 
      
      
# Challenge print highest marks

marks =[90,30,100,46,79,80]

highest= marks[0]
for i in marks:
      if i > highest:
            highest = i
print(highest)