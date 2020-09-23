user_name = input(prompt = "What is your name?")
income = input(prompt = "What is your income?")
retire = input(prompt = "What is your 401k?")
taxable = income - retire
state_tax = taxable * .0307
local_tax = taxable * .01
property_tax = taxable * .062
federal_tax = taxable * .1
take_home = taxable - state_tax - local_tax - property_tax - federal_tax
print(user_name, "has a take home income of $", take_home)
