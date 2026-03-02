from math import factorial as f

print("1. ", [n**2 for n in range(1, 11)])

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print("2. ", dict((day, x) for x, day in enumerate(days_of_week, 1)))

libs = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
print("3. ", set(lib.lower() for lib in libs))

arr = [1, 3, 4, 87, 98, 15, 7, 4]
print("4. ", [x for x in arr if x % 2 == 0])

print("5. ", dict((n, f(n)) for n in range(1, 6)))