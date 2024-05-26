from collections import Counter

def count_numbers(lst):
    counter = Counter(lst)
    count_dict = dict(counter)
    print(count_dict)

numbers = [1, 1, 1, 2, 2, 2, 2, 6, 8, 8, 4, 4, 4, 3, 3, 3, 9, 9, 9, 5, 5, 7, 7]

count_numbers(numbers)
