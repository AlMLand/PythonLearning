list_int: my_list[int] = [1, 2, 3, 4, 5]

for index, value in enumerate(list_int):
    print(f"track each index: {index} and item: {value}")

dictionary_str: dict[str, str] = {
    "a": "1", "b": "2", "c": "3", "d": "4"
}
for key in dictionary_str:
    print(key)
for value in dictionary_str.items():
    print(value)
for key, value in dictionary_str.items():
    print(f"{key} -- {value}")

my_list = [1, 2, 3, 4, 5]
for i in my_list:
    if i == 1:
        continue
    elif i == 3:
        pass
    elif i == 2:
        print(i)
    elif i == 4:
        break
