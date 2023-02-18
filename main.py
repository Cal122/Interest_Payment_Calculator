# A = P * (1 + r/n)^(n*t)

def calculator(principal, apr, years):
    monthly_rate = apr / 12
    time = years * 12
    amount = principal * (1 + monthly_rate) ** time
    return amount


principal_input = float(input("How much money?: "))
years_input = int(input("How many years?: "))
apr_input = float(input("At what APR rate?: "))

result = calculator(principal_input, apr_input, years_input)

print(f"After {years_input} years, £{principal_input} at an APR of {apr_input} would end up being £{result:.2f} ")