number = int(input())
size = 5 * number
for index in range(number // 2):
    dots = number + index
    print("." * dots + "#" * (size - (dots * 2)) + "." * dots)
for index in range((number // 2) + 1):
    dots = number + (number // 2) + index
    print("." * dots + '#' + "." * (size - (dots * 2) - 2) + "#" + "." * dots)
dots = size - number
print("." * (dots // 2) + "#" * number + "." * (dots // 2))
new_dots = size - (number + 4)
for index in range(number//2):
    print("." * (new_dots // 2) + "#" * (number + 4) + "." * (new_dots // 2))
dance = size - 10
print("." * (dance // 2) + "D^A^N^C^E^" + "." * (dance // 2))
for index in range(number//2 + 1):
    print("." * (new_dots // 2) + "#" * (number + 4) + "." * (new_dots // 2))
