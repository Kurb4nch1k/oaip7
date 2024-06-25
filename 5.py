def max_iterative(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

numbers = [2, 9, 1, 11, 6]
max_num = max_iterative(numbers)
print(f"Максимальное число в списке {numbers} равно {max_num}.")
