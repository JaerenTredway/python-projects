class MuffledCalculator:
    muffled = 0
    def calc(self,expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print("Division by zero error.")
            else:
                raise
        
try:
    x = (input("Enter the first number: "))
    y = (input("Enter the second number: "))
    x = int(x)
    y = int(y)
    print(x/y)

# except ZeroDivisionError:
#     print("The second number can't be zero!")
# except TypeError:
#     print("That wasn't a number!")

# except(ZeroDivisionError,TypeError), e:
#     # print("Bad mojo fo the mofo.")
#     print e

except:
    print("Bad poop on that one.")

finally:
    print("You done sucka")

#*****************
try:
    print("Raising axception")
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Div by zero bra")

#*******************
info = {
    "firstName" : "Bobba",
    "lastName" : "Fett"
}
# catch any and all errors:
try:
    print(info['firstName'])
# except Exception as e:
#     print(type(e))
except KeyError as e:
    print("no key bubb")
    print(e) 
    print(f"Key: {e}")
except Exception as f: #catch any other error:
    print(f)
else:
    print("It worked!")
finally: #close handlers or logins:
    print("done.")