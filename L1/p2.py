import pandas as pd 
from sklearn.linear_model import LinearRegression

data = pd.read_csv("home_prices_1.csv")
print(data)

feature = data[["area"]]
target = data[["price"]]

model = LinearRegression()
model.fit(feature, target)

area = float(input("Enter area: "))
price = model.predict([[area]])
print("area = ", area, "price = ", price)


