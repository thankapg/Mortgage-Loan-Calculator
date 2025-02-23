# Mortgage-Loan-Calculator

Overview:
This Mortgage Loan Calculator is a Python-based tool designed to help users analyze mortgage payments, generate amortization schedules, and explore early payoff options. It provides a user friendly interface through a menu-driven system, allowing users to calculate monthly payments, total interest, payoff dates, and more. Additionally, it visualizes loan amortization and balance trends using matplotlib.

Features:
Monthly Payment Calculation: Computes the fixed monthly payment based on loan amount, interest rate, and term.
Total Payment and Interest: Calculates the total cost of the loan, including total interest paid over the loan term.
Amortization Schedule: Generates a detailed table showing payment breakdowns for each period.
Early Payoff Calculation: Estimates the amount required to pay off the loan early.
Extra Payment Impact: Determines how additional monthly payments can shorten the loan term.
Graphical Representations: Visualizes amortization schedules and balance reduction over time.

Implementation Details
MortgageLoanCalculator.py
This module defines the MortgageLoanCalculator class, which implements all financial calculations and visualization functions. It uses the following libraries:
numpy_financial for financial calculations (e.g., payment calculations).
pandas for handling amortization schedules.
matplotlib.pyplot for data visualization.

dateutil for handling dates and generating payment schedules.

Key Methods:

compute_monthly_payment(): Calculates the fixed monthly mortgage payment.

generate_amortization_schedule(): Creates a table with the breakdown of principal and interest payments.

create_amortization_table(): Constructs a Pandas DataFrame for easy analysis.

early_payoff_amount(period): Determines the amount required to settle the loan at a specific month.

new_term_with_extra_payment(extra_payment): Estimates the new loan term if extra monthly payments are made.

extra_payment_to_retire_debt(years_to_debt_free): Calculates the additional monthly amount needed to retire the debt within a given time frame.

plot_amortization(): Visualizes the principal vs. interest payments over time.

plot_balance_and_interest(): Plots the remaining loan balance and cumulative interest paid.

Display_MLC.py

This script provides a command-line interface for user interaction. It presents a menu with multiple options, allowing users to enter loan details and receive calculated results. Users can also generate visual charts and explore early payoff strategies interactively.
