#control statements
# if statement
# marks = int(input("Enter marks: "))
# if marks>=90:
#     print("grade: A")
# elif marks>=70:
#     print("grade: B")
# elif marks>=50:
#     print("grade: C")
# else:
#     print("grade: D")   


#temp 
temp =int(input("enter temperature: "))
if temp<=50 and temp>=30:
    print("hot")
elif temp <=24 and temp>=10:
    print("cold")
elif temp<10:
    print("extremely cold")
elif temp>50:
    print("invalid temp")


#driving eligibility 


#Ternary Operator 

age= int(input())
result = "Eligible" if age >=18 else "Not Eligible"
print(result)
