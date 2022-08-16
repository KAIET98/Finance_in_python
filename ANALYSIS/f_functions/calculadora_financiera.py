import numpy_financial as npf
import numpy as np
import matplotlib.pyplot as plt

class net_worth_dev:
    
    def __init__(self, rent, daily_food, month_entert_budge, month_unfor_exp, salario, tax_rate):
        
        
        # Calculate your monthly food budget assuming 30 days per month
        self.monthly_food_budget = daily_food*30
        
        self.rent = rent
        
        
        
        self.month_entert_budge = month_entert_budge
        
        self.month_unfor_exp  = month_unfor_exp
        
        self.salary = salario
        
        self.tax_rate = tax_rate
        
        
        
    def calc_intermedios(self):
        
        # Next, calculate your total monthly expenses
        self.monthly_expenses = self.rent+self.monthly_food_budget+self.month_entert_budge+self.month_unfor_exp
        print("Monthly expenses: " + str(round(self.monthly_expenses, 2)))


        self.salary_after_taxes = self.salary*(1-self.tax_rate)
        
        self.monthly_takehome_salary = self.salary_after_taxes/12

        # Finally, calculate your monthly take-home savings
        monthly_savings = self.monthly_takehome_salary - self.monthly_expenses
        print("Monthly savings: " + str(round(monthly_savings, 2)))
        
    
    def forecast_salary_growth_living(self, month_forecast, annual_salary_growth):
        
        # Calculate your equivalent monthly salary growth rate
        monthly_salary_growth = (1 + annual_salary_growth)**(1/12)-1

        # Forecast the cumulative growth of your salary
        cumulative_salary_growth_forecast = np.cumprod(np.repeat(1 + monthly_salary_growth, month_forecast))

        # Calculate the actual salary forecast
        self.salary_forecast = self.monthly_takehome_salary * cumulative_salary_growth_forecast

        # Plot the forecasted salary
        plt.plot(self.salary_forecast, color='blue')
        plt.title('SALARY FORECAST')
        plt.show()
        
    def forecast_growing_expenses_inflation(self, inflation,month_forecast):
        
        # Calculate the equivalent monthly inflation rate
        monthly_inflation = (1+inflation)**(1/12)-1

        # Forecast cumulative inflation over time
        cumulative_inflation_forecast = np.cumprod(np.repeat( 1 + monthly_inflation, month_forecast))

        # Calculate your forecasted expenses
        self.expenses_forecast = self.monthly_expenses * cumulative_inflation_forecast

        # Plot the forecasted expenses
        plt.plot(self.expenses_forecast, color='red')
        plt.title('EXPENSES FORECAST')
        plt.show()
        
    def your_net_worth(self):
        
        # Calculate your savings for each month
        savings_forecast = self.salary_forecast - self.expenses_forecast

        # Calculate your cumulative savings over time
        cumulative_savings = np.cumsum(savings_forecast) 

        # Print the final cumulative savings after 15 years
        final_net_worth = cumulative_savings[-1]
        print("Your final net worth: " + str(round(final_net_worth, 2)))

        # Plot the forecasted savings
        plt.plot(cumulative_savings, color='blue')
        plt.title('NET FORECAST')
        plt.show()
        
        
   
        
        
        
        
    
    
    
    
    #month_forecast
    
    #annual_salary_growth
    
    #annual_inflation
    
    #investment_anual_rate
    
    #monthly_investment_percentage