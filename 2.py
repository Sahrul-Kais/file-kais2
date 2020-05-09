import re

def usernameCheck(username):
    if(re.match("^[a-z][a-z0-9._]{8,12}$",username)):
        return True
    else:
        return False

def passwordCheck(password):
    if(re.match("^(?=.*[0-9])(?=.*[a-zA-Z!@#$%\^&*+=._-]).{9}$",password)):
        return True 
    else:
        return False

print(usernameCheck("sahrul.kais"))
print(passwordCheck("s4hRu!kAi"))