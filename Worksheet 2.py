courses = ["Math", "Physics", "Biology", "Chemistry"]

print(courses)

print(sorted(courses))
print(sorted(courses, reverse=True))

courses.sort()
print(courses)

courses.reverse()
print(courses)

courses.append("English")
courses.insert(0, "History")
print(courses)

courses.pop()
courses.remove("Math")
print(courses)

for course in courses:
    print(course)

data = [(1, "Math"), (2, "Physics")]

for item in data:
    print(item[0], item[1])