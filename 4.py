def prime_iterative(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

number = int(input("Введите номер: "))
if prime_iterative(number):
    print(f"Число {number} является простым.")
else:
    print(f"Число {number} не является простым.")
