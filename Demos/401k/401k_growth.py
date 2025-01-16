# Script to calculate 401(k) investment growth with and without company match


# Hardcoded initial salary
initial_salary =  int(input("Enter base salary for calculations: "))


# Ask for user inputs
investment_percentage = float(input("Enter the percentage of your salary to invest in the 401(k): ")) / 100
annual_contribution = initial_salary * investment_percentage
monthly_contribution = annual_contribution / 12
print(round(annual_contribution), round(monthly_contribution))
years_to_retirement = int(input("Enter the number of years to retirement: "))


# Calculate the annual investment and company match
annual_investment = initial_salary * investment_percentage
company_match = initial_salary * min(investment_percentage, 0.03)  # Match 100% of the first 3%


# Display the table header
print("\n401(k) Investment Growth Over Time (With and Without Match):")
print(f"{'Growth Rate':<15}{'Final Value (No Match) ($)':<25}{'Final Value (With 3%s Match) ($)':<30}")
print("-" * 60)


# Loop through growth rates from 5% to 15% (inclusive)
for growth_rate in range(5, 16):  # 5% to 15% inclusive
    annual_rate = growth_rate / 100
    months = years_to_retirement * 12  # Convert years to months
    monthly_rate = annual_rate / 12  # Monthly growth rate
    monthly_investment = annual_investment / 12  # Convert annual investment to monthly
    monthly_match = company_match / 12  # Convert annual match to monthly

    # Future value calculation for employee contributions only
    final_value_no_match = monthly_investment * (((1 + monthly_rate) ** months - 1) / monthly_rate)

    # Future value calculation with employer match
    final_value_with_match = (monthly_investment + monthly_match) * (((1 + monthly_rate) ** months - 1) / monthly_rate)

    # Print the results
    print(f"{growth_rate}%{' ':<7}{final_value_no_match:,.2f}{' ':<15}{final_value_with_match:,.2f}")
