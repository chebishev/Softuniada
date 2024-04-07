input_list = [int(x) for x in input().split()]
large_numbers_count = int(input())
step = len(input_list) - large_numbers_count
large_numbers = sorted(input_list)
for x in large_numbers[step:]:
    print(x)
    