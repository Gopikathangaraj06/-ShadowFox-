

def format_number(num, specifier):
    return format(num, specifier)

result = format_number(145, 'o')
print("Formatted value:", result)
print("Representation: Octal")


pi = 3.14
radius = 84

area = pi * radius * radius
print("Area of the pond:", area)

water_per_sq_meter = 1.4
total_water = area * water_per_sq_meter

print("Total water in the pond:", int(total_water))

distance = 490  # meters
time_minutes = 7
time_seconds = time_minutes * 60

speed = distance / time_seconds
print("Speed in meters per second:", int(speed))
