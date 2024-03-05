parenthesis_string = input()
max_count = 0
start_flag = False

temporary_count = 0
for symbol in parenthesis_string:
    if symbol == "(":
        if start_flag:
            temporary_count = 0
        else:
            start_flag = True
    if symbol == ")":
        if start_flag:
            temporary_count += 2
            start_flag = False
            if temporary_count > max_count:
                max_count = temporary_count
        else:
            temporary_count = 0

print(max_count)
