# Harishankar Vashishtha
name=str(input("Your Name:- "))
print("\nHello! and Welcome! "+name+", Calculate your each Semester TGPA and Overall CGPA.")
print("Dear "+name+", Write your each subject Credit and Grade point somewhere and then give your input accordingly")

print(name+", If you know your grade points then give YES as input, else NO.")
grade=str(input("YES/NO :- "))

if (grade=="YES" or grade=="yes"):
    print("Okay "+name+",so you know your Subject Grade Points")
else:
    print("\nO Grade = 10 points")
    print("A+ Grade = 9 points")
    print("A Grade = 8 points")
    print("B+ Grade = 7 points")
    print("B Grade = 6 points")
    print("C Grade = 5 points")
    print("D Grade = 4 points")
    print("E Grade(Re-appear) = 0 points")
    print("F Grade(Fail) = 0 points")
    print("G Grade(Backlog) = 0 points")
    print("I Grade(Incomplete Result) = 0 points")
    print("Okay,so now give your input accrodingly")

sem=int(input("\nHow many semesters have you completed "+name+"? :- "))
tempcgpamarkstuple=0
tempcgpacredtuple=0

for i in range(1,sem+1):

    tempcred = 0
    tempmarks = 0
    credtuple = (0)
    markstuple = (0)
    print("\n**** Give your semester '"+str(i)+"' Grade Points and Credits ****")
    totsub=int(input(name+", How many subjects do you have in semester '"+str(i)+"' :- "))

    for x in range(1,totsub+1) :

        cred=int(input("\nGive your Subject '"+str(x)+"' Credits:- "))
        credtuple=(cred)
        cred=tempcred+cred
        tempcred=cred

        marks = int(input("Give your Subject '"+str(x)+"' Grade Points:- "))
        markstuple=(marks)
        marks = tempmarks+(markstuple*credtuple)
        tempmarks = marks
        tgpa=marks/cred

    cgpamarkstuple=tempcgpamarkstuple +marks
    tempcgpamarkstuple=cgpamarkstuple
    cgpacredtuple = tempcgpacredtuple + cred
    tempcgpacredtuple = cgpacredtuple

    print("\nDear "+name+", Your semester '"+str(i)+"' T.G.P.A is '"+str(tgpa)+"'.")

cgpa=cgpamarkstuple/cgpacredtuple
print("\nCongratulations! "+name+" Your Overall C.G.P.A of B.Tech after '"+str(sem)+"' semester is '"+str(cgpa)+"'.")
print("\nAre you getting error/wrong result above ? if yes then give YES as input in next line else NO.")
error=str(input("YES/NO :- "))
if (error=="YES") or (error=="yes"):
    print("\nDear "+name+", Click on the below given site and then share your error with us on the site form.")
    print("https://vashishthahari.weebly.com/feedback")
else:
    print("\nIf you get correct result, then don't forget to give your feedback on my site given below.")
    print("https://vashishthahari.weebly.com/feedback")