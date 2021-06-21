# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year%4==0:
  #check if it is divisible by 100 and not div by 400. If so, it is not a leap year
  if year%100 == 0 and year%400 != 0:
    print("Not leap year.")
  #all other exceptions to this rule if (divisible by 4) will be leap year
  else:
    print("Leap year.")
#if not divisible by 4, it is not a leap year
else:
  print("Not leap year.")

print("The leap years for the following 100 years are:")
y=year
for y in range(y,y+100):
  if y%4==0:
    if y%400==0:
      print(year)
    if y%100!=0:
      print(y)
year += 1