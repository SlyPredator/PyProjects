def find_max(numbers):
    maximum = numbers[0]
    for each in numbers:
        if each > maximum:
            maximum = each
    return maximum
