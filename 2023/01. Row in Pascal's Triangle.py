def pascal(row):
    line = [1]
    for k in range(row):
        line.append(int(line[k] * (row - k) / (k + 1)))
    return line


row_number = int(input())

print(*pascal(row_number), sep=" ")
