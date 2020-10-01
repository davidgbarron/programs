class Converter:
    def __init__(self):
        self.sel = input("Please type f for Fahrenheit to Celsius, or type \
c for Celsius to Fahrenheit. Type q to quit:")
        if "f" in self.sel:
            Converter.far(self)
            return None
        if "c" in self.sel:
            Converter.cel(self)
            return None
        if "q" in self.sel:
            print("\n")
            print(bye)
            return None
        else:
            print("invalid input")
            Converter()                      
    def far(self):
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
bye = "Goodbye"
fdegrees = "Fahrenheit"
cdegrees = "Celsius"
Converter()
