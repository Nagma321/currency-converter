💱 Currency Converter – Overview

This project is a simple Currency Converter built using Python. It converts a given amount in INR (Indian Rupees) to major foreign currencies such as USD, EUR, and GBP.
The program fetches the latest exchange rates from a real-time API, ensuring accurate currency conversion.

🚀 Features

Converts INR to:

USD – United States Dollar

EUR – Euro

GBP – British Pound

Uses live exchange rates from an online API

Simple user input

Fast and accurate calculation

Beginner-friendly Python project

🔧 How It Works

The user enters an amount in INR.

The program sends a request to:

https://api.exchangerate-api.com/v4/latest/INR


It receives real-time currency data in JSON format.

It multiplies the INR amount with the exchange rates for USD, EUR, and GBP.

The converted values are displayed with two decimal places.

🧩 Technologies Used

Python

requests module

ExchangeRate-API (Live currency data)

📌 Example Output
💱 Currency Converter (INR to others)
Enter amount in INR: 1000

Converted Amounts:
USD: 12.03
EUR: 11.10
GBP: 9.55
