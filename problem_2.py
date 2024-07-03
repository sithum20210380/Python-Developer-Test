def square_evens(numbers: list) -> list:
    return [num**2 for num in numbers if num % 2 == 0]

print(square_evens([1, 2, 3, 4, 5]))