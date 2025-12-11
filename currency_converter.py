import requests

print("💱 Currency Converter (INR to others)")

amount = float(input("Enter amount in INR: "))

url = "https://api.exchangerate-api.com/v4/latest/INR"
data = requests.get(url).json()

usd = amount * data["rates"]["USD"]
eur = amount * data["rates"]["EUR"]
gbp = amount * data["rates"]["GBP"]

print("\nConverted Amounts:")
print(f"USD: {usd:.2f}")
print(f"EUR: {eur:.2f}")
print(f"GBP: {gbp:.2f}")
