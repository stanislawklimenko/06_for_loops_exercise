# 1 Fill the missing pieces
words = ["PYTHON", "JOHN", "chEEse", "hAm", "DOE", "123"]
upper_case_words = []
sum_of_values = 0

for i in words:
    if i.isupper():
        upper_case_words.append(i)

assert upper_case_words == ["PYTHON", "JOHN", "DOE"]

# 2 Calculate the sum of dict values
magic_dict = dict(val1=44, val2="secret value", val3=55.0, val4=1)
# Your implementation
for i in magic_dict:
    if isinstance(magic_dict[i], int):
        sum_of_values += magic_dict[i]
    elif isinstance(magic_dict[i], float):
        sum_of_values += int(magic_dict[i])

assert sum_of_values == 100

# 3 Create a list of strings based on a list of numbers
numbers = [1, 3, 4, 6, 81, 80, 100, 95]
my_list = []
# Your implementation
for i in numbers:
    if i % 5 == 0 and i % 2 != 0:
        my_list.append("five odd")
    elif i % 5 == 0 and i % 2 == 0:
        my_list.append("five even")
    elif i % 2 != 0:
        my_list.append("odd")
    elif i % 2 == 0:
        my_list.append("even")

assert my_list == [
    "odd",
    "odd",
    "even",
    "even",
    "odd",
    "five even",
    "five even",
    "five odd",
]