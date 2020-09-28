#This asks the user for their name
user_name = input(prompt = "What is your name?")
#Asks user for income
income = input(prompt = "What is your income?")
#asks user for retirement plan
retire = input(prompt = "What is your 401k?")
#next 5 lines calculate the taxes
taxable = income - retire
state_tax = taxable * .0307
local_tax = taxable * .01
property_tax = taxable * .062
federal_tax = taxable * .1

#calculates take home value by subtracting taxes
take_home = taxable - state_tax - local_tax - property_tax - federal_tax
#prints takehome value
print(user_name, "has a take home income of $", take_home)