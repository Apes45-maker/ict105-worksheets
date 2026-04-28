students = {
    1001: ["CS101", "MATH101"],
    1002: ["CS101"]
}

print("Student Courses:")
for student, courses in students.items():
    print("Student ID:", student)
    print("Courses:", courses)
    print()

names = []

while True:
    name = input("Enter name (type 'exit' to stop): ").strip()

    # ignore empty input
    if name == "":
        continue

    # stop condition
    if name.lower() == "exit":
        break

    names.append(name)

print("\nList of names:", names)

count = 0

print("\nPrinting Hello 3 times:")
while count < 3:
    print("Hello")
    count += 1