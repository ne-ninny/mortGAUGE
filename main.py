def mortgage_calculator(gross_annual_income):
    two_hundred_percent = gross_annual_income * 2
    two_hundred_fifty_percent = gross_annual_income * 2.5
    
    return f"You can afford between a ${two_hundred_percent} and a ${two_hundred_fifty_percent} house"

def main():
    test = mortgage_calculator(1_000_000)

    print(test)

main()