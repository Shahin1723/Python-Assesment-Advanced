import re
data = "TODAYS DATE:01/29. This is my assessment-2! I have to submit by Tuesday!"
upper_case = re.findall('[A-Z]',data)
print("Uppercase letters are :",len(upper_case))
lower_case = re.findall('[a-z]',data)
print("Lowercase letters are :",len(lower_case))
numeric = re.findall('[0-9]',data)
print("Numeric no.s are :",len(numeric))
special = re.findall('[:!?]',data)
print("Special letters are :",len(special))
