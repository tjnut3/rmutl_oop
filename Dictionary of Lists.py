# Dictionary of lists: Mapping cities to their temperatures
cities = {
    'New York': [32, 25, 30, 28, 35],
    'Los Angeles': [75, 68, 72, 70, 80],
    'Chicago': [20, 18, 22, 25, 15],
}

# Calculate average temperature for each city
averages = {city: sum(temps) / len(temps) for city, temps in cities.items()}
print("Average temperatures:", averages)
# Output: {'New York': 30.0, 'Los Angeles':73.0, 'Chicago': 20.0}