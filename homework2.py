fname=input("Enter first name:")
lname=input("Enter last name:")
age=input("Enter age:")
yearofbirth=input("Enter year of birth:")
list=[fname,lname,age,yearofbirth]

for i in list:
    print(i)
age=int(age)
if age<18:
    print("You can't go out because it's too dangerous.")
else:
    print("You can go out to the street.")