import time
def addgrades(midterm,final,project):
    return {"midterm": midterm,"final": final, "project": project}

def takelessons():
    lessonlist=list()
    while True:
        lessons=input("Enter lessons(Min:3 Max:5):")
        lessonlist.append(lessons)
        if lessons=="S":
            print ("Sending your lessons...")
            time.sleep(2)
            print ("Checking your lessons...")
            time.sleep(3)
            if len(lessonlist) < 3:
                return "You failed in class."
                exit()
            elif len(lessonlist) > 5:
                print("Enter max 5 lessons!")
                continue
            else:
                lessonlist.remove("S")
                return(f"Thank you! Your lessons: {lessonlist}")
                break
    exit()



def lettergrade(finalscore):
    finalscore=float(finalscore)
    if (finalscore) >= 90:
     return "Your Grade is AA!"
    elif 70 <= (finalscore) < 90:
        return "Your Grade is BB!"
    elif 50 <= (finalscore) < 70:
        return "Your Grade is CC!"
    elif 30 <= (finalscore) < 50:
        return "Your Grade is DD!"
    else:
        return "Your Grade is FF! YOU FAILED!"

print("""
**************************************************
---STUDENT MANAGEMENT SYSTEM---
**************************************************
""")
name = input("ENTER YOUR NAME:")
print(f"Your name: {name}")
chance=3
while 1<=chance:
    check = input("Is the name correct? Enter your name again:")
    if chance==1:
        print("Please try again later!")
        exit()
    if name==check:
        print(f"Welcome {name}!")
        break
    else:
        print("Enter your name in correct way!")
        chance-=1
        continue

print("""
---------------------------
ENTER YOUR LESSONS!
IF YOU TAKE LESS THAN 3, YOU FAIL!
TO SEND IT TO SYSTEM PRESS S!
---------------------------
""")
print(takelessons())

print("""
---------------------------
CHOOSE A LESSON AND ENTER GRADES FOR CALCULATION!
MIDTERM:30% FINAL:50% PROJECT:20%
LETTER NOTES:
  GRADE>=90 AA
  70<=GRADE<90 BB
  50<=GRADE<70 CC
  30<=GRADE<50 DD
  GRADE<30  FF
---------------------------
""")
chosenlesson=input("Choose a lesson:")
print("Enter your grades for chosen lesson:")
midterm=input("Enter your midterm:")
final=input("Enter final midterm:")
project=input("Enter your project:")

print(addgrades(midterm,final,project))
finalscore = (int(midterm) * (0.3)) + (int(final) * (0.5)) + (int(project) * (0.2))
print (f"Your final score: {finalscore}")
print(lettergrade(finalscore))
