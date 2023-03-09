#En caso de ver el error: ModuleNotFoundError: No module named 'dateutil'
#"Settings" > "Project" > "Python Interpreter" and search for python-dateutil and install the package
from datetime import datetime
from dateutil import relativedelta

# CONSTANTS
PARSER_FMT = "%Y-%m-%d"
CURRENT_DATE = datetime.now()
SILENT_GEN_END = 1939
BOOMERS_GEN_END = 1959
GEN_X_END = 1979
GEN_Y_END = 1989

# USER INPUTS
birthday_str = input(f"Birthdate ({PARSER_FMT})?")

# LOGIC
birthday = datetime.strptime(birthday_str, PARSER_FMT)
delta = relativedelta.relativedelta(CURRENT_DATE, birthday)
print(f"Age: {delta.years} years, {delta.months} months, {delta.days} days, {delta.minutes} minutes, {delta.seconds} seconds")

birthday_celebrated = (birthday.month >= CURRENT_DATE.month) and (birthday.day >= CURRENT_DATE.day)
print(f"Birthday: {birthday_celebrated}")

if birthday.year <= SILENT_GEN_END:
    print("Silent generation")
elif birthday.year <= BOOMERS_GEN_END:
    print("Baby boomers")
elif birthday.year <= GEN_X_END:
    print("Generation X")
elif birthday.year <= GEN_Y_END:
    print("Generation Y or millennials")
else:
    print("Generation Z")