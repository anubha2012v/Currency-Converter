#here we have taken currency.txt as it will fetch data from there.
with open('currencydata.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter Amount:\n"))
print("Enter the name of the Currency you wnat to convert"
      "this amount to? Availabe options:\n")
[print(item) for item in currencyDict.keys()]
currency = input("Please Enter one of these Values")
print(f"{amount} INR is equal to {amount * float(currencyDict[currency])} {currency}")

