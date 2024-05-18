def isvalidaadhar(Aadhar):
    if Aadhar.isdigit() and len(Aadhar)==12:
        return True
    else:
        return False
 
def isvalidpan(pan):
    if len(pan)==10 and pan.isupper() and pan[5:-2].isdigit() and pan[0:5].isalpha() and pan[-1:].isalpha():
        return True
    else:
        return False

def isvalidname(name):
    n = name.split()
    if len(n)==3 and n[0].isalpha() and n[1].isalpha() and n[2].isalpha():
        return True
    else:
        return False