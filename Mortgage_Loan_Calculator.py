from dateutil import parser as dt
from dateutil import relativedelta as rd
import matplotlib.pyplot as plt
import numpy_financial as npf
import pandas as pd

class MortgageLoanCalculator:
    def __init__(self, principal, annual_rate, term_years, start_date):
        self.principal = principal
        self.annual_rate = annual_rate
        self.monthly_rate = annual_rate / 12 / 100
        self.term_months = term_years * 12
        self.start_date = start_date
        self.schedule = self.generate_schedule()
        self.monthly_payment = self.compute_monthly_payment()
        self.monthly_payment_str=f"${self.monthly_payment:,.2f}"
        self.amortization_schedule = self.generate_amortization_schedule()
        self.amortization_table = self.create_amortization_table()
        
    def generate_schedule(self):
        start_date = dt.parse(self.start_date)
        schedule = pd.date_range(start_date, periods=self.term_months, freq='MS')
        schedule.name = 'Payment Date'
        return schedule
    
    def compute_monthly_payment(self):
        payment = -npf.pmt(self.monthly_rate, self.term_months, self.principal)
        return payment
    
    def generate_amortization_schedule(self):
        payment = self.compute_monthly_payment()
        principal = self.principal
        amortization = []
        for period in range(1, self.term_months + 1):
            interest = principal * self.monthly_rate
            principal -= (payment - interest)
            amortization.append((period, payment, interest, principal))
        return amortization
    
    def create_amortization_table(self):
        amortization = self.generate_amortization_schedule()
        table = pd.DataFrame(amortization, columns=['Period', 'Payment', 'Interest', 'Principal'])
        table.set_index('Period', inplace=True)
        table['Balance'] = self.principal - table['Principal'].cumsum()
        table = table.round(2)
        return table
    
    def plot_amortization(self):
        table = self.amortization_table
        ax = table[['Principal', 'Interest']].plot(kind='line', stacked=True, figsize=(12, 6))
        ax.set_title('Mortgage Amortization Schedule')
        ax.set_xlabel('Period')
        ax.set_ylabel('Amount')
        plt.show()

    def display_summary(self):
        print(f'Loan Amount: ${self.principal:,.2f}')
        print(f'Annual Interest Rate: {self.annual_rate:.2f}%')
        print(f'Loan Term: {self.term_months} months')
        print(f'Monthly Payment: ${self.monthly_payment_str}')
        print(f'Total Payment: ${self.monthly_payment * self.term_months:,.2f}')
        print(f'Total Interest: ${self.monthly_payment * self.term_months - self.principal:,.2f}')
        print(self.amortization_table)

    def early_payoff_amount(self, period):
        if period < 1 or period > self.term_months:
            return 'Invalid period'
        table = self.amortization_table
        principal = table.loc[period, 'Balance']
        interest = principal * self.monthly_rate
        payoff_amount = principal + interest
        return payoff_amount

    def new_term_with_extra_payment(self, extra_payment):
        new_term = npf.nper(self.monthly_rate, self.monthly_payment + extra_payment, -self.principal)
        return f'{round(new_term / 12, 2)} years'

    def extra_payment_to_retire_debt(self, years_to_debt_free):
        base_payment = self.compute_monthly_payment()
        extra_payment = 1
        while npf.nper(self.monthly_rate, base_payment + extra_payment, -self.principal) / 12 > years_to_debt_free:
            extra_payment += 1
        return extra_payment, base_payment + extra_payment

    def plot_balance_and_interest(self):
        table = self.amortization_table
        table['Cumulative Interest'] = table['Interest'].cumsum()
        plt.figure(figsize=(10, 5))
        plt.plot(table.index[::6], table['Balance'][::6], label='Remaining Balance', markersize=3)
        plt.plot(table.index[::6], table['Cumulative Interest'][::6], label='Cumulative Interest Paid', markersize=3)
        plt.title('Mortgage Balance and Cumulative Interest')
        plt.xlabel('Period')
        plt.ylabel('Amount')
        plt.legend(loc='best')
        plt.grid(axis='y', alpha=0.5)
        plt.show()

    def calculate_payoff_date(self):
        last_payment_date = self.schedule[-1]
        return last_payment_date.strftime('%Y-%m-%d')

