

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

if bmi >= 30:
    print("BMI Category: Obesity")
elif bmi >= 25:
    print("BMI Category: Overweight")
elif bmi >= 18.5:
    print("BMI Category: Normal")
else:
    print("BMI Category: Underweight")

print()



australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name: ")

if city in australia:
    print(city, "is in Australia")
elif city in uae:
    print(city, "is in UAE")
elif city in india:
    print(city, "is in India")
else:
    print("City not found")

print()


city1 = input("Enter first city: ")
city2 = input("Enter second city: ")

def find_country(city):
    if city in australia:
        return "Australia"
    elif city in uae:
        return "UAE"
    elif city in india:
        return "India"
    else:
        return None

country1 = find_country(city1)
country2 = find_country(city2)

if country1 and country2 and country1 == country2:
    print("Both cities are in", country1)
else:
    print("They don't belong to the same country")
