import csv
import matplotlib.pyplot as plt

mileage = []
price = []

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        mileage.append(float(row[0] )/10000)
        price.append(float(row[1] )/10000)

var_x = 0.0
var_y = 0.0
errore = 0.0
learning_rate = 0.01  # va adattato ai dati
iterations = 100000
m = len(mileage)

for _ in range(iterations):
# while(True):
    sum_error = 0.0
    sum_error_x = 0.0

    for i in range(m):
        prezzo = price[i]
        km = mileage[i]

        previsione = var_x + var_y * km
        errore = previsione - prezzo
        sum_error += errore
        sum_error_x += errore * km

    mean_error = sum_error / m
    mean_error_x = sum_error_x / m

    tmp_var_x = var_x - learning_rate * mean_error
    tmp_var_y = var_y - learning_rate * mean_error_x

    # if (tmp_var_x / var_x)*100 < 0.01:
    #     break
    # if (tmp_var_y / var_y)*100 < 0.01:
    #     break
    var_x = tmp_var_x
    var_y = tmp_var_y

with open("gradient.txt", "w") as file:
    file.write(str(var_x))
    file.write("\n")
    file.write(str(var_y))

plt.scatter(mileage, price, color="blue", label="Dati reali")

# linea di regressione
predicted = []
for km in mileage:
    predicted.append(var_x + var_y * km)

plt.plot(mileage, predicted, color="red", label="Modello")

plt.xlabel("Km")
plt.ylabel("Prezzo")
plt.title("Linear Regression")
plt.legend()

plt.show()