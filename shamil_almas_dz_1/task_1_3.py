def transform_string(number: int) -> str:
    n = ''
    return n
special_numbers = {11,12,13,14}
for n in range(100):
    n = n + 1
    if n in special_numbers:
        print(n, "процентов")
    elif n % 10 == 1:
        print(n, "процент")
    elif n % 10 > 1 and n % 10 <5:
        print(n,"процента")
    else:
        print(n, "процентов")

print(transform_string(n))