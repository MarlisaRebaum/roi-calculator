class ROICaluclator():
    """
    This calculator is used to calculate the return on investment (ROI) on 
    a rental property.

    Attributes for the ROICaclulator:
    -income: float
    -expenses: float
    -cash_flow: float
    -investment: float
    -roi: float

    """

    def __init__(self, income, expenses, cash_flow, investment, roi):
        self.income = income
        self.expenses = expenses
        self.cash_flow = cash_flow
        self.investment = investment
        self.roi = roi

    def calc_income(self):
        print("Please input the following MONTHLY income. If not applicable, please input 0.")
        self.income += float(input("Total rental income: "))
        self.income += float(input("Total laundry room income: "))
        self.income += float(input("Total rental storage income: "))
        self.income += float(input("Other income: "))
        print(f"Total monthly income: ${round(self.income, 2)}.")

    def calc_expenses(self):
        print("Please input the following MONTHLY expenses. If not applicable, please input 0.")
        self.expenses += float(input("Taxes: "))
        self.expenses += float(input("Insurance: "))
        self.expenses += float(input("Utilites: "))
        self.expenses += float(input("HOA fee: "))
        self.expenses += float(input("Garden care: "))
        self.expenses += float(input("Vacancy (typically 5 percent of total income): "))
        self.expenses += float(input("Repairs (typically $50-100 per unit per month): "))
        self.expenses += float(input("Capital expenditure (typically $100 per month): "))
        self.expenses += float(input("Poperty management (typically 10 percent of monthly income): "))
        self.expenses += float(input("Mortage: "))
        print(f"Total monthly expenses: ${round(self.expenses, 2)}.")

    def calc_cash_flow(self):
        self.cash_flow = (self.income - self.expenses) * 12
        print(f"Total annual cash flow: ${round(self.cash_flow, 2)} ")

    def calc_investment(self):
        print("Please input the following expenses for buying the property.")
        self.investment += float(input("Down Payment: "))
        self.investment += float(input("Closing Costs: "))
        self.investment += float(input("Rehab Budget: "))
        self.investment += float(input("Misc Other: "))
        print(f"Total investment: ${round(self.investment, 2)} ")

    def calc_roi(self):
        self.roi = (self.cash_flow / self.investment) * 100
        print(f"Total ROI on the rental property is: {round(self.roi, 2)}%")


current_calculation = ROICaluclator(0, 0, 0, 0, 0)

def run_calculator(): 

    while True:

        response = input("Thanks for using our ROI calculator. This calculator is used to calculate the total return on invesment for a potential rental property. \
            \nWould you like to start now? Enter 'yes' to start and 'quit' to stop. ")

        if response.lower() == 'quit':
            print('Thanks for using our calculator and good luck with your rental property!')
            break
        elif response.lower() == 'yes':
            current_calculation.calc_income()
            current_calculation.calc_expenses()
            current_calculation.calc_cash_flow()
            current_calculation.calc_investment()
            current_calculation.calc_roi()
        else:
            print("Invalid input. Please enter 'yes' to continue or 'quit' to exit the calculator. ")

run_calculator()
