names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
city = ["New York", "Los Angeles", "Chicago"]

#Using zip() for parallel iteration
for name, age, city in zip(names, ages, city):
    print(f"{name} is {age} years old and lives in {city}")