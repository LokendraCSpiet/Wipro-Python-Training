import re
 
def isvalidpan(pan):
    pattern = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
    if re.search(pattern,pan):
        return True
    else:
        return False
 
def isvalidaadhar(aadhar):
    pattern = "[0-9]{12}"
    if re.search(pattern,aadhar):
        return True
    else:
        return False
 
print(isvalidpan("CEHPm4327K"))
print(isvalidaadhar("123412341234"))