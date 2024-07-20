import pandas as pd 
import numpy as np
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


#------------------------------------------#

#solve with formula

b0 = model.intercept_
b1 = model.coef_
ans = b0 + b1 * area
print("ans = ", ans)

'''
Linear Regression:
    - it is a statistical method for predictive analysis.
    - it can make prediction for continuous/real or numeric variables such as price, salary, etc.
    - Linear regression is used to find out how the value of dependent variable is changing according to the value of independent variable.

Type of Relationship:
    -Regression line can show two types of relationship:
        -Positive Linear Relationship:
                In this the value of y increases as the value of x increases.
        -Negative Linear Relationship
                In this the value of y ddecreses as the value of x increases.

'''

