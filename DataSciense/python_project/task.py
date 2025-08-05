students = ["Ama", "Kojo", "Yaw", "Kevin","Joseph"]
grade = [0,75,47,45,0]
name = input("Student Name: ")

if name == "Ama" and "Ama" in students:
    print(grade[0])
    if grade[0] > 50:
        print("fail")
    elif grade[0] <= 50:
        print("pass")

if name == "Kojo" and "Kojo" in students:
    print(grade[1])
    if grade[0] > 50:
        print("fail")
    elif grade[0] <= 50:
        print("pass")

if name == "Yaw" and "Ama" in students:
    print(grade[2])
    if grade[0] > 50:
        print("fail")
    elif grade[0] <= 50:
        print("pass")

if name == "Kevin" and "Ama" in students:
    print(grade[3])
    if grade[0] > 50:
        print("fail")
    elif grade[0] <= 50:
        print("pass")

if name == "Joseph" and "Ama" in students:
    print(grade[4])
    if grade[0] > 50:
        print("fail")
    elif grade[0] <= 50:
        print("pass")

    else:
        print("Student not found")