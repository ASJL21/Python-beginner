#type conversion int float 
# first = int(input("first: "))
# second = int(input("second: "))
# sum = first + second
# print("sum is: " + str(sum))

#strings 
# course = "python for beginners"

# print(course.upper())
# print(course.find('t')) #indexing
# print(course.replace('for', '4')) #replace
# print(course)

#arithmatic operations
# print(10 + 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3) #power

# x = 10 
# x = x + 3
# x += 3 #shorthand for x = x + 3

# x = 10 + 3 * 2 #order of operations, PEMDAS
# print(x)

#comparision operators true or false 
# x = 3 > 2 
# x = 2 == 3
# x = 3 != 2 
# print(x)


#logical operators and, or, not

# price = 25
# print(price > 10  and price < 30) #true
# print( price > 30 or price < 40) #true
# print(not price > 3)

#if statements 

# temp = 5 
# if temp > 30: 
#     print( "it's a hot day ")
#     print("drint plenty of water")
# elif temp > 20:
#     print(" its a nice day") 
# elif temp  > 10:
#     print("its bit cold")
# else:
#     print("its cold day")
# print("done")

# exercise
weight = input("weight: ")
unit = input("(L)bs or (K)g: ") # unit of the weight entered by the user
if unit.upper() == "K" :
    converted = float(weight) / 0.45
    print("weight in lbs:" + str(converted))
else:
    converted = float(weight) * 0.45
    print("weight in kg:" + str(converted))
