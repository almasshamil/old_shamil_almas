def sum_list_1(dataset: list) -> int:
    sum = 0

    for num in dataset:
        num_sum = 0
        divisible_by_seven = False

        for c in str(num):
            num_sum = num_sum + int(c)

        if (num_sum % 7 == 0):
            divisible_by_seven = True

        if (divisible_by_seven):
            sum = sum + num

    return sum


def sum_list_2(dataset: list) -> int:
    new_dataset_added_seven = []

    for e in dataset: new_dataset_added_seven.append(e + 17)

    sum = sum_list_1(new_dataset_added_seven)

    return sum


# Lets collect all the odd numbers
my_list = []
for i in range(1001):
    if i % 2 == 1:
        my_list.append(i ** 3)

result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)