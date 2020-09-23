user_name = input(prompt = "What is your name?")
income = input(prompt = "What is your income?")
retire = input(prompt = "What is your 401k?")
taxable = income - retire
state_tax = taxable * .0307
local_tax = taxable * .01
property_tax = taxable * .062
federal_tax = taxable * .1
