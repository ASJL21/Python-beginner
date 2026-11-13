#loops

# i = 1
# while i <=10:
#     print(i * '*')
#     i = i + 1

#Lists
import numbers


names = [ "jhon" , "bob", "mary" , "souuj" , "laya" ]

# print(names [1])
  #negative indexing if it is -2 the second last name or item is selected
# print(names[-1]) #mary
# names[0] = "jon"
# print(names)
# print(names[0:3]) #does not print index = 3 name stops right befor index is 2 so output is jon,bob,mary



#lists methods
# numbers = [1,2,3,4,5]
# numbers.append(6) #adds 6 to the end of the list
# numbers.insert(0, -1) #inserts -1 at index 0
# numbers.remove(3) #removes 3 from the list
# numbers.clear()
# print( 1 in numbers) #checks if 1 is in the list and returns true or false
# print(len(numbers)) #returns the length of the list


#FOR LOOP 
# numbers = [1,2,3,4,5]
# for item in numbers:
#     print(item)

# range function
# numbers = range(5) #sequence of numbers from 0 to 4
# numbers = range(5, 10)
# numbers = range(5,10,2) #sequence of numbers from 5 to 9 with a step of 2
# print(numbers)
# for number in numbers:
    # print(number)

#even shorter we can directly use range for loop without having and variable called numbers then assiging it with a range
# for number in range(5):
#     print(number)



#Tuples are immutable we cannot change them later on
numbers = (1,2,3,4)
# TypeError: 'tuple' object does not support item assignment
# numbers[0] = 10
 #this will give an error because tuples are immutable
numbers.count(1) #returns the number of times 1 appears in the tuple