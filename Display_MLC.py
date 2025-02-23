from Mortgage_Loan_Calculator import MortgageLoanCalculator
import sys
from time import sleep

def menu():
    print("Welcome to the Mortgage Loan Calculator")
    print("Please select an option")
    print("1. Calculate Monthly Payment")
    print("2. Calculate Total Payment")
    print("3. Calculate Total Interest")
    print("4. Calculate Payoff Date")
    print("5. Plot Amortization Schedule")
    print("6. Display Summary")
    print("7. Calculate Early Payoff Amount")
    print("8. Calculate New Term with Extra Payment")
    print("9. Calculate Extra Payment to Retire Debt")
    print("10. Plot Balance and Cumulative Interest")
    print("11. Exit")

def get_loan_details():
    loan_amount = float(input("Enter loan amount: "))
    interest_rate = float(input("Enter interest rate: "))
    loan_term = int(input("Enter loan term in years: "))
    start_date = input("Enter start date (YYYY-MM-DD): ")
    return MortgageLoanCalculator(loan_amount, interest_rate, loan_term, start_date)

def main():
    while True:
        menu()
        choice = input("Enter choice: ")
        if choice == '1':
            m = get_loan_details()
            print(f"Monthly payment: {m.monthly_payment_str()}")
        elif choice == '2':
            m = get_loan_details()
            total_payment = m.monthly_payment * m.term_months
            print(f"Total payment: ${total_payment:,.2f}")
        elif choice == '3':
            m = get_loan_details()
            total_interest = m.monthly_payment * m.term_months - m.principal
            print(f"Total interest: ${total_interest:,.2f}")
        elif choice == '4':
            m = get_loan_details()
            print(f"Payoff date: {m.calculate_payoff_date()}")
        elif choice == '5':
            m = get_loan_details()
            m.plot_amortization()
        elif choice == '6':
            m = get_loan_details()
            m.display_summary()
        elif choice == '7':
            m = get_loan_details()
            period = int(input("Enter period to payoff loan early: "))
            print(f"Early payoff amount at month {period}: ${m.early_payoff_amount(period):,.2f}")
        elif choice == '8':
            m = get_loan_details()
            extra_payment = float(input("Enter extra payment amount: "))
            print(f"New term with extra payment: {m.new_term_with_extra_payment(extra_payment)}")
        elif choice == '9':
            m = get_loan_details()
            years = int(input("Enter years to retire debt: "))
            extra_payment, new_monthly_payment = m.extra_payment_to_retire_debt(years)
            print(f"Extra monthly payment to retire debt in {years} years: ${extra_payment:,.2f}")
            print(f"New monthly payment: ${new_monthly_payment:,.2f}")
        elif choice == '10':
            m = get_loan_details()
            m.plot_balance_and_interest()
        elif choice == '11':
            print("The End!")
            sys.exit()
        else:
            print("Invalid choice")
        sleep(2)
    
if __name__ == '__main__':
    main()


