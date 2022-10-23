class MyException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return(self.value)

try:
    num = input("Enter the number: ")
    if num == '2':
        raise MyException("ohh")
    else:
        print("Number entered is not 2.")

except MyException:
    print("MyException occurred.")