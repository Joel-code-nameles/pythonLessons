favnumber = 52 # intiger
print(type(favnumber))
number = 5.2 #float
print(type(number))
words = "Mr. Sams work" # string
print(type(words))
trueorflase = True #boleen
print(type(trueorflase))
list = [1,2,3,4,5] #list
print(type(list))

firstnumber = int(input("Number: "))
secondnumber = int(input("Number: "))

result1 = firstnumber + secondnumber
result2 = firstnumber - secondnumber
result3 = firstnumber * secondnumber
result4 = firstnumber / secondnumber
result5 = firstnumber ** secondnumber
result6 = firstnumber % secondnumber
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)

birthyear = int(input("Birth Year: "))
current_year = int(input("Current Year: "))

result7 = (current_year - birthyear)
print(result7)

num1 = int(input("Number: "))
num2 = int(input("Number: "))

if num1 > num2:
    print("5 is Greater than 2")

if num1 == num2:
    print("5 is equal to 2")

if num1 or num2 in list:
    print("Hello World")

if num1 and num2 in list:
    print("Hello World")

subjects = ["math","english","science","history","ict"]
subject = input("Subject: ")
if subject in subjects:
    print(f"Lets do {subject}")
if subject not in subjects:
    print(f"Lets do {subject}")