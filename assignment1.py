#You're building a system to manage student data for a university. Each student is identified by a unique student ID and has the following details)
#- Name
#- Major
#- Enrolled Courses (each course has a course name and a dictionary of assessment scores like midterm, final, and project)
 #Sample Data (Nested Dictionary):*/

university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },  # <-- Missing comma added here
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

print(university_data)

#printing names with their majors
for stud_id,info in university_data.items():
    name=info["name"]
    ma=info["major"]
    print(f"Name:{name},Major:{ma}")
# Name:Alice Johnson,Major:Computer Science
# Name:Bob Smith,Major:Mathematics
# Name:Clara Lopez,Major:P

