student_database=[]
def deco_add(f):
    def w(*a,**k):
        print("\n>>> add_student_data START")
        r=f(*a,**k)
        print("<<< add_student_data END\n")
        return r
    return w
def deco_record(f):
    def w(*a,**k):
        print("\n>>> record_marks START")
        r=f(*a,**k)
        print("<<< record_marks END\n")
        return r
    return w
def deco_remove(f):
    def w(*a,**k):
        print("\n>>> remove_student START")
        r=f(*a,**k)
        print("<<< remove_student END\n")
        return r
    return w
def deco_show(f):
    def w(*a,**k):
        print("\n>>> show_results START")
        r=f(*a,**k)
        print("<<< show_results END\n")
        return r
    return w
@deco_add
def add_student_data():
    name=input("Student Name : ").strip()
    roll=int(input("Roll Number  : "))
    subjects=input("Comma-Separated Subjects (blank if none): ").split(",")
    subjects=[s.strip() for s in subjects if s.strip()]
    marks={}
    if input("Provide Marks Now? (y/n): ").lower()=="y":
        for sub in subjects:
            marks[sub]=int(input(f"{sub} Marks: "))
    grades={sub:None for sub in subjects}
    grades.update(marks)
    student_database.append({"name":name.title(),"roll_no":roll,"grades":grades})
    print("✓ Student Added.")
@deco_record
def record_marks():
    roll=int(input("Roll Number : "))
    stu=next((s for s in student_database if s["roll_no"]==roll),None)
    if not stu:
        print("✖ Roll Number not found.")
        return
    while True:
        subj=input("Subject (blank to stop): ").strip()
        if not subj:
            break
        mark=int(input(f"{subj} Marks: "))
        stu["grades"][subj]=mark
    print("✓ Marks Recorded.")
@deco_remove
def remove_student():
    roll=int(input("Roll Number : "))
    for i,s in enumerate(student_database):
        if s["roll_no"]==roll:
            student_database.pop(i)
            print(f"✓ Removed (Roll {roll}).")
            return
    print("✖ Roll Number not found.")
@deco_show
def show_results():
    try:
        pass_mark=int(input("Pass Mark (default 40): ") or 40)
    except ValueError:
        pass_mark=40
    if not student_database:
        print("No student data.")
        return
    for s in student_database:
        scores=[m for m in s["grades"].values() if m is not None]
        if not scores:
            print(f"{s['name']} (Roll {s['roll_no']}): marks pending.")
            continue
        total=sum(scores)
        avg=total/len(scores)
        status="PASS" if all(m>=pass_mark for m in scores) else "FAIL"
        print("="*48)
        print(f"{s['name']} (Roll {s['roll_no']})")
        print("Grades :",s["grades"])
        print("Total  :",total)
        print(f"Average: {avg:.2f}")
        print("Result :",status)
while True:
    print("""
╔═══════════════════════╗
║ Student DataBase MENU ║
╠═══════════════════════╣
║ 1. Add the Student    ║
║ 2. Record the Marks   ║
║ 3. Remove the Student ║
║ 4. Show the Results   ║
║ 5. Exit Dashboard     ║
╚═══════════════════════╝
""")
    try:
        choice=int(input("Enter Your Choice (1-5): "))
    except ValueError:
        print("Enter a Valid Number (1-5).")
        continue
    if choice==1:
        add_student_data()
    elif choice==2:
        record_marks()
    elif choice==3:
        remove_student()
    elif choice==4:
        show_results()
    elif choice==5:
        print("Thank You, Visit Again")
        break
    else:
        print("Invalid Choice")