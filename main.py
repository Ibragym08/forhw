# assignment operator

# a = 42
#
# a = a + 5


# shorthand operators (assignment operators)
# a += 5
#
# a -= 7
#
# a /= 2
#
# a //= 2
#
# a **= 2
#
# a %= 10
#
# a *= 2

# print(a)

# arithmetic operators

# +, -, *, /, //, %, **

# comparison operators

# x = 42
# y = 13
#
# print("x =", x)
# print("y =", y)
# print("x > y :", x > y)
# print("x < y :", x < y)
# print("x >= y :", x >= y)
# print("x >= y :", x <= y)
# print("x >= y :", x == y)


# age program
# age = int(input())
#
# if age >= 18:
#     print("You are allowed")
# else:
#     print("You are not allowed")

# age = int(input())
#
# if age < 20:
#     print("You are teenager")
# elif age >= 20:
#     print("You are a student")
# elif age >= 60:
#     print("You are a retired")
# else:
#     print("You are very old person")
#
# if age == 42:
#     print("You are 42 years old")


#Task 1
# firstNumber = int(input("Enter a number:"))
#
# if firstNumber >=1 and firstNumber <= 100 :
#     if firstNumber % 5 == 0 and firstNumber % 3 == 0:
#         print("Fizz Buzz")
#     elif firstNumber % 3 == 0:
#         print("Fizz")
#     elif firstNumber % 5 == 0:
#         print("Buzz")
#     elif firstNumber % 5 or firstNumber % 3 != 0:
#         print(firstNumber)
# else:
#     print("Incorrect number")

 #Task 2
salary = 200
firstManager = int(input("Enter a first manager`s sales percentage:"))
secondManager = int(input("Enter a second manager`s sales percentage:"))
thirdManager = int(input("Enter a third manager`s sales percentage:"))

salary1 = 200
salary2 = 200
salary3 = 200

if firstManager <500:
        salary1=(salary + (firstManager * 0.03))
elif firstManager >=500 and firstManager <= 1000:
        salary1=(salary + (firstManager * 0.05))
elif firstManager>1000:
        salary1=(salary + (firstManager * 0.08))
if secondManager < 500:
        salary2=(salary + (secondManager * 0.03))
elif secondManager >= 500 and secondManager <= 1000:
        salary2=(salary + (secondManager * 0.05))
elif secondManager > 1000:
         salary2=(salary + (secondManager* 0.08))
if thirdManager < 500:
    salary3=(salary + (thirdManager * 0.03))
elif thirdManager >= 500 and thirdManager <= 1000:
       salary3=(salary + (thirdManager * 0.05))
elif thirdManager > 1000:
       salary3=(salary + (thirdManager* 0.08))


if salary1 > salary2 and salary1 > salary3:
    salary1 += 200
if salary2 > salary1 and salary2 > salary3:
    salary2 += 200
if salary3 > salary1 and salary3 > salary2:
    salary3 += 200
# if firstManager * 0.08 > secondManager * 0.08 and firstManager * 0.08 > thirdManager * 0.08:
#     print(salary + firstManager * 0.08 + 200)
# elif firstManager * 0.05 > secondManager * 0.05 and firstManager * 0.035 > thirdManager * 0.05:
#     print(salary + firstManager * 0.05 + 200)
# elif firstManager * 0.03 > secondManager * 0.03 and firstManager * 0.03 > thirdManager * 0.03:
#     print(salary + firstManager * 0.03 + 200)
# if secondManager * 0.08 > firstManager * 0.08 and secondManager * 0.08 > thirdManager * 0.08:
#     print(salary + secondManager * 0.08 + 200)
# elif secondManager * 0.05 > firstManager * 0.05 and secondManager * 0.05 > thirdManager * 0.05:
#     print(salary + secondManager * 0.05 + 200)
# elif secondManager * 0.03 > firstManager * 0.03 and secondManager * 0.03 > thirdManager * 0.03:
#     print(salary + secondManager * 0.03 + 200)
# if thirdManager * 0.08 > firstManager * 0.08 and thirdManager * 0.08 > secondManager * 0.08:
#     print(salary + thirdManager * 0.08 + 200)
# elif thirdManager * 0.05 > firstManager * 0.05 and thirdManager * 0.05 > secondManager * 0.05:
#     print(salary + thirdManager * 0.05 + 200)
# elif thirdManager * 0.03 > firstManager * 0.03 and thirdManager * 0.03 > secondManager * 0.03:
#     print(salary + thirdManager * 0.03 + 200)
# if secondManager * 0.08 == thirdManager * 0.08:
#     print(salary + secondManager * 0.08 + 200)
#     print(salary + thirdManager * 0.08 + 200)

# if firstManager > secondManager and firstManager > secondManager:
#      salary1 += firstManager
# if secondManager > firstManager and secondManager > thirdManager:
#     salary2 += secondManager
# if thirdManager > firstManager and thirdManager > secondManager:
#     salary3 += thirdManager
#
print(salary1)
print(salary2)
print(salary3)







