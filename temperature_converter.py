"""this is a simple temperature converter"""
class Converter:
    """this chooses which function to call to convert"""
    def __init__(self):
        self.sel = input("Please type f for Fahrenheit to Celsius, type \
c for Celsius to Fahrenheit, or type k for Fahrenheit to Kelvin. Type q to quit:")
        if "f" in self.sel:
            Converter.far(self)
            return None
        if "c" in self.sel:
            Converter.cel(self)
            return None
        if "k" in self.sel:
            Converter.kel(self)
            return None
        
        if "q" in self.sel:
            print("\n")
            print(bye)
            return None
        else:
            print("invalid input")
            Converter()                      
    def far(self):
        """this defines the function to convert fahrenheit to celsius"""
        if "f" in self.sel:
            self.f = input("please type degrees Fahrenheit:")
            self.f = int(self.f)
            print((self.f - 32) * 5 / 9, "degrees {}".format(cdegrees))
            print("\n")
            self.again = input("would you like to convert something else? type y or n:")
            if "y" in self.again:
                Converter()
            while "n" in self.again:
                print("\n")
                print(bye)
                break
    def cel(self):
        """this defines the function to convert celsius to fahrenheit"""
        if "c" in self.sel:
            self.c = input("please type degrees Celsius:")
            self.c = int(self.c)
            print(self.c * 9 / 5 + 32, "degrees {}".format(fdegrees))
            print("\n")
            self.again = input("would you like to convert something else? type y or n:")
            if "y" in self.again:
                Converter()
            while "n" in self.again:
                print("\n")
                print(bye)
                break
    def kel(self):
        """this defines the function to convert fahrenheit to kelvin"""
        if "k" in self.sel:
            self.k = input("please type degrees Fahrenheit:")
            self.k = int(self.k)
            print((self.k - 32) * 5 / 9 + 273.15, "degrees {}".format(kdegrees))
            print("\n")
            self.again = input("would you like to convert something else? type y or n:")
            if "y" in self.again:
                Converter()
            while "n" in self.again:
                print("\n")
                print(bye)
                break
"""the following defines the variables used to format, as well as calls the class/program
to execute"""
bye = "Goodbye"
fdegrees = "Fahrenheit"
cdegrees = "Celsius"
kdegrees = "Kelvin"
Converter()
