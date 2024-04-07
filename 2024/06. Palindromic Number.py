from collections import Counter
number = input()
all_numbers = Counter(number)
odd_occurrences = 0
for element in all_numbers:
    if all_numbers[element] % 2 == 1:
        odd_occurrences += 1
if odd_occurrences > 1:
    print("No palindromic number available.")
else:
    left_output = []
    right_output = []
    numbers_to_convert = sorted(number)[::-1]
    for index in range(len(numbers_to_convert)):
        if index % 2 == 0:
            left_output.append(numbers_to_convert[index])
        else:
            right_output.append(numbers_to_convert[index])
    left_output.extend(right_output[::-1])
    for element in left_output:
        print(element, end="")
