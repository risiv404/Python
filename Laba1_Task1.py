numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
total_sum = sum(n if n is not None else 0 for n in numbers)
count = len(numbers)
average = total_sum / count if count > 0 else 0
updated_numbers = [average if x is None else x for x in numbers]
print("Измененный список:", updated_numbers)
