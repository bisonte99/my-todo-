# average numbers

"""def get_average():
    with open("files/data.txt", "r") as file:
        data = file.readlines()

    values = data[1:]
    values = [float(i) for i in values]

    average_local = sum(values) / len(values)  # change to average_local because it was grey
    return average_local


average = get_average()
print(average)"""

# Function to Process a List 1
"""def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    return maximum

print(get_max())"""



# Function to Process a Lis get max and min
"""def get_max():
    grades = [9.6, 9.2, 9.7]

    maximum = max(grades)

    minimum = min(grades)

    message = f"Max:{maximum}, Min{minimum}"

    return message

print(get_max())"""

#Function to Process a String
"""def format_filename():
    filename = "report.txt"
    new_file = filename.capitalize()[:6]
    return new_file


file = format_filename()
print(file)"""


# Function to Process a Number
"""def square_number():
    number = 5
    result = number ** 2
    return result
print(square_number())  """


#Liters Converter Function
"""def liters_to_m3(liters):
    m3 = liters / 1000
    return m3"""




"""# Define a function named strength that takes one parameter, password
def strength(password):
    # Create an empty dictionary to store the strength attributes
    result = {}

    # Check the length of the password

    # Check if the password contains a digit and an uppercase letter
    digit = False
    uppercase = False

    # Iterate over each character in the password
    for i in password:
        # Check if the character is a digit
        if i.isdigit():
            digit = True
        # Check if the character is an uppercase letter
        if i.isupper():
            uppercase = True

    # Store the results in the dictionary
    result["digits"] = digit
    result["upper-case"] = uppercase

    # Check if all the strength attributes are True
    if all(result.values()):
        # Return "Strong Password" if all attributes are True
        return "Strong Password"
    else:
        # Return "Weak Password" if any attribute is False
        return "Weak Password"
    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False"""

# Average Function
"""def foo(mylist):
    return sum(mylist) / len(mylist)"""


"""def foo(name):
    return f"Hi {name}"""

# Concatenation Function #"PARAMETRAS TAS  KUR SKLIAUSTUOSE"
"""def foo(a1, a2):
    return a1 + a2"""

# Greeting Function and String Manipulation
"""def greet(name):
    return f"Hi {name.title()}"""


"""def speed(distance, time):
    return distance / time


print(speed(300, 5))"""


# Age Function
"""def get_age( year_of_birth, current_year=2025):
    age = current_year - year_of_birth
    return age"""

# Split Function
"""def get_nr_items(user_input):
    items = user_input.split(",")
    return len(items)"""

# Temperature Checker
"""def foo(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"""

# Password Length Checker
"""def foo(password):
    if len(password) >= 8:
        return True
    else:
        return False
print(foo("jhuolkhgd"))"""

# Water State Checker
"""def water_state(temperature):
    if temperature <= 0:
        return "solid"
    elif 0 < temperature < 100:
         return "Liquid"
    else:
         return "Gas"""

"""FREEZING_POINT = 0
BOILING_POINT = 100

def water_state(temperature):
    if temperature <= FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"""







