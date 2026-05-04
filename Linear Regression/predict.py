with open("gradient.txt") as file:
    x = float(file.readline())
    y = float(file.readline())

km = float(input("Input the km: "))
price = x + y * (km / 10000)
price = int(price * 10000)
print(f"The price for a car with {km} km is {price} euro")