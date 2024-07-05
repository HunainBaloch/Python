def print_sum(first, second):
    print(first + second)


print_sum(2,3)    


def calculate_average(*args):
    if not args:
        return 0
    return sum(args) / len(args)

print(calculate_average(1, 2, 3, 4, 5)) 
print(calculate_average(10, 20))        
print(calculate_average())            


def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())       
print(greet("Alice")) 


def describe_car(make, model, **kwargs):
    description = f"{make} {model}"
    for key, value in kwargs.items():
        description += f", {key}: {value}"
    return description

car_description = describe_car("Toyota", "Camry", color="blue", year=2020, mileage=15000)
print(car_description)


