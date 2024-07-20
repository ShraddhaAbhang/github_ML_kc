import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("home_prices_1.csv")
print(data)

area = data["area"].tolist()
price = data["price"].tolist()

plt.scatter(area, price)
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Lonaval Prices")

plt.show()

