 # declare a list
list=[10,501,22,37,100,999,87,351]
#create a happy number list
def is_happy_number_efficient(n):
    seen = set()
    while n != 1:
        if n in seen:
            return False  # Cycle detected, not a happy number
        seen.add(n)
        n = sum(int(digit)**2 for digit in str(n)) #More concise way to calculate the sum of squares
    return True

def find_happy_numbers_efficient(numbers):
    return [num for num in numbers if is_happy_number_efficient(num)]

happy_numbers_efficient = find_happy_numbers_efficient(list)
print(f"Happy numbers in the list (efficient): {happy_numbers_efficient}")

