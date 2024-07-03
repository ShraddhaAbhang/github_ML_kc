import pandas as pd

data = pd.read_csv("home_prices_1.csv")
print(data)

x = data["area"].to_list()
y = data["price"].to_list()

print(x)
print(y)

r1 = 0
for i in range(len(x)):
    r1 = r1 + x[i]
print(r1)

r2 = 0
for i in range(len(y)):
    r2 = r2 + y[i]
print(r2)

r3 = 0
for i in range(len(x)):
    r3 = r3 + x[i] * x[i]
print(r3)

r4 = 0
for i in range(len(y)):
    r4 = r4 + y[i] * y[i]
print(r4)

r5 = 0
for i in range(len(x)):
    r5 = r5 + x[i] * y[i]
print(r5)


N = len(x)
num = (N * r5) - (r1 * r2)
den = (N * r3) - (r1 * r1)

b1 = num / den
print(b1)

b0 = r2 / N - b1 * r1 / N
print(b0)

x = float(input("enter area: "))
y = b0 + b1 * x
print("print = ", y)