def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    number = int(input("Пожалуйста, введите номер: "))
    print(f'Факториал числа {number} равен {factorial(number)}')

if __name__ == "__main__":
    main()
