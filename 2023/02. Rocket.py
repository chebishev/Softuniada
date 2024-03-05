rocket_size = int(input())

first_row = "_" * (int(rocket_size / 2) + 2) + "^" + "_" * (int(rocket_size / 2) + 2)
print(first_row)

second_row = "_" * (int(rocket_size / 2) + 1) + "/|\\" + "_" * (int(rocket_size / 2) + 1)
print(second_row)

for i in range(int(rocket_size / 2 + 1)):
    print("_" * (int(rocket_size / 2) - i) + "/" + "." * i + "|||" + "." * i + "\\" + "_" * (int(rocket_size / 2) - i))

middle_row = "_/" + "." * (int(rocket_size / 2) - 1) + "|||" + "." * (int(rocket_size / 2) - 1) + "\\_"
print(middle_row)

for i in range(rocket_size):
    print("_" * int(rocket_size / 2 + 1) + "|||" + "_" * int(rocket_size / 2 + 1))

down_middle_row = "_" * int(rocket_size / 2 + 1) + "~~~" + "_" * int(rocket_size / 2 + 1)
print(down_middle_row)

for i in range(int(rocket_size / 2)):
    print("_" * (int(rocket_size / 2) - i) + "//" + "." * i + "!" + "." * i + "\\\\" + "_" * (int(rocket_size / 2) - i))
