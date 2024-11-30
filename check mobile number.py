#created by athul raj
#date:30-11-2024
def mobilenumbercheck():
    mobilenumber = input('enter the number')
    if len(mobilenumber)==10 and mobilenumber[0] in '789':
        print("the mobile number is valid")
    else:
        print("the mobile number is not valid")
mobilenumbercheck()
