def welcome():
    print("Welcome to the Tip Calculator")
    bill = float(input("What was the total bill?\n"))
    people = int(input("How many people to split the bill?\n"))
    tip = int(input("What % tip would you like to give?\n"))
    tip_as_percent = tip / 100
    total_tip = bill * tip_as_percent
    total_bill = bill + total_tip
    bill_per_person = total_bill / people
    final_bill = "{:.2f}".format(bill_per_person, 2)
    print(f'Each person should pay: ${final_bill}')


welcome()


def bmi_calc():
    weight = input('Enter Weight: \n')
    height = input('Enter Height in inches: \n')
    bmi = int(weight)*703 / float(height) ** 2
    bmi_int = int(bmi)
    print(bmi_int)


bmi_calc()
