# Logical Operators

has_high_income = True
has_good_credit = True
has_criminal_record = False

# Logical AND
if has_high_income and has_good_credit:
    print("Eligible for loan")

# Logical NOT
if has_good_credit and not has_criminal_record:
    print("Good credit no criminal")

# Logical OR
# if has_high_income or has_good_credit:
#     print("Eligible for loan")
