# Assignment 1
student_data = {
    "id1": {"name": "John", "age": 20, "major": "Computer Science"},
    "id2": {"name": "Alice", "age": 22, "major": "Mathematics"},
    "id3": {"name": "John", "age": 20, "major": "Computer Science"},
    "id4": {"name": "Bob", "age": 21, "major": "Arts"}
}

result = {}
seen_keys = []

for key, value in student_data.items():
    if value not in seen_keys:
        result[key] = value
        seen_keys.append(value)
        
for key, value in result.items():
    print(f"ID: {key}, Name: {value['name']}, Age: {value['age']}, Major: {value['major']}")

# Assignment 2
test_dict = {
    "Codingl" : 2,
    "Is" : 2, 
    "Best" : 2,
    "for" : 2,
    "Coding ": 2
}

print("The original dictionary is :" + str(test_dict))
k = 2
result = 0


for key in test_dict:
    if test_dict[key] == k:
        result += 1

print("The number of keys having the value " + str(k) + " is : " + str(result))

#assignment 3
country_code = {
    "USA": 1,
    "Canada": 2,
    "Mexico": 3
}

print("The country codes for USA::")
print(country_code.get("USA", "Country not found"))