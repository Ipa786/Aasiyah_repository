temperature = int(input("Enter today's temperature in Celsius: "))
if temperature < 20:
    outfit = "jacket"
    print("It is cold today.")
    print("Wear a", outfit)
else:
    outfit = "t-shirt"
    print("It is warm today.")
    print("Wear a", outfit)
is_raining = input("It is raining today? (yes/no): ")
if is_raining == "yes":
    print("Bring an umbrella!")
wind_speed = int(input("Enter today's wind speed in km/h: "))
print("The wind speed is", wind_speed, "km/h.")
