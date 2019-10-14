def check_input(a):
    validations =[]
    if a.isalnum():
        validations.append(True)
    if a.isalpha():
        validations.append(True)
    if a.isdigit():
        validations.append(True)
    if a.lower():
        validations.append(True)
    if a.upper():
        validations.append(True)
    else:
        validations.append(True)
    
    return validations

print(check_input("qA2"))