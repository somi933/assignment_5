my_dict = {
    "Kiran": 35,
    "Santosh": 67,
    "Hari": 50,
    "Madhu": 89
}

name = input("Enter the Student's name: ")
for keys in my_dict:
    if name == keys:
        print(f"{name}'s marks are: ", my_dict[name])
    else:
        print("Sorry, Student not found")
    break
