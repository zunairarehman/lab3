#program 1
first_number = str(input("Enter first number:"))
second_number = str(input("Enter second number:"))
sum = (first_number + second_number)
print("The addition of two numbers is:", sum)
#program 2
a=5
print("a=", a, sep='0', end=',\n')
#program 3
name= input ("Enter employee name:")
salary= input ("Enter salary:")
company= input ("Enter company name:")
print("PRINTING EMPLOYEE DETAILS")
print("NAME","SALARY","COMPANY")
print(name, salary, company)
#program 4
name=input("Enter your name:")
dob=input("Enter date of birth:")
rollno=input("Enter your roll no:")
section=input("Enter your section:")
per=input("Enter your matriculation percentage:")
grade=input("Enter your matriculation grade:")
per1=input("Enter your intermediate percentage:")
grade1=input("Enter your intermediate grade:")
print("\t***BIO-DATA***")
print(name,"\n",dob,"\n",rollno,"\n",section,"\n",per,"\n",grade,"\n",per1,"\n",grade1)
#program 5
print("What kind of food would you like?")
food=input()
print("Let me find the best",food.upper(),"for you")
#program 6
course1,course2,course3,course4,course5=eval(input("Enter marks of 5 subjects:"))
total=course1+course2+course3+course4+course5
average=total/5
per=(total*100)/250
print("The total marks are:",total,",average is:",average,"and the percentage is:",per,"%")
