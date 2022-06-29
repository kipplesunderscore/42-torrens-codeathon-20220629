from decimal import *

# Factor class
# contains constand values for the weight of each factor.
class Factor:
    FOUNDER = Decimal('0.3')
    INDUSTRY = Decimal('0.3')
    TRACTION = Decimal('0.35')
    GUT = Decimal('0.05')

class Startup:
    # Startup constructor
    # name: string
    # founder: Decimal
    # industry: Decimal
    # traction: Decimal
    # gut: Decimal
    def __init__(self, name, founder, industry, traction, gut):
        self.name = name
        self.founder = founder
        self.industry = industry
        self.traction = traction
        self.gut = gut

    # Calculate the rating based off the factor weights.
    # make sure to round to 2 decimal places.
    def calculate_rating(self):
        return Decimal(sum([
            self.founder * Factor.FOUNDER,
            self.industry * Factor.INDUSTRY,
            self.traction * Factor.TRACTION,
            self.gut * Factor.GUT])).quantize(Decimal('0.01'))

    # Calculate the classification based off the rating value.
    def calculate_classification(self):
        rating = self.calculate_rating()
        if (rating >= 4.0):
            return "P1"
        elif (rating >= 2.5):
            return "P2"
        elif (rating >= 1.0):
            return "P3"
        else:
            return "R"

    # Helper debug util to display the class as a formatted string
    def __repr__(self):
        return f"""name = {self.name}
founder = {self.founder}
industry = {self.industry}
traction = {self.traction}
gut = {self.gut}
rating = {self.calculate_rating()}
classificatin = {self.calculate_classification()}"""

# function to determine if string 'dec' is a Decimal value
def is_decimal(dec):
    try:
        Decimal(dec)
        return True
    except InvalidOperation:
        return False

# function to determine of 'dec' is a valid factor.
# valid factors should be between 0 and 5 inclusive.
def is_valid_factor_range(dec):
    return Decimal(dec) >= 0.00 and Decimal(dec) <= 5.00

# function takes a string and parses it into a Startup class.
# will return a Startup class on success.
# return False on Error.
# function will display a error message if there happens to be an error.
def parse_startup_string(info):
    arr = info.split(",")
    # not enough arguments given print error and return.
    if (len(arr) < 5):
        print("\033[0;31mInput Error:\033[0m please enter structure like name,factor1,factor2,factor3,factor4")
        return (False)
    # extract the relevant values from the split string
    # strip any whitespace characters before or after the value.
    name = arr[0].strip()
    founder = arr[1].strip()
    industry = arr[2].strip()
    traction = arr[3].strip()
    gut = arr[4].strip()

    # check the strings for errors.
    # checking for invalid Decimal values.
    # checking for invalid factor ranges.
    error = False
    for i in range(1, 5):
        factor = arr[i].strip()
        if (not is_decimal(factor)):
            print(f'\033[0;31mInput Error:\033[0m Factor {i} has invalid input, please input a decimal value i.e. (4.25)')
            error = True
        elif(not is_valid_factor_range(factor)):
            print(f'\033[0;31mInput Error:\033[0m Factor {i} value is outside range (0.00 - 5.00)')
            error = True
    if error:
        return False

    # input was valid return new Startup object
    return Startup(name, Decimal(founder), Decimal(industry), Decimal(traction), Decimal(gut))
