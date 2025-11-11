class NotEligible(Exception):
    pass

age = int(input("Enter age: "))
try:
    if age >= 18:
        print("Eligible to Vote!")
    else:
        raise NotEligible("Not Eligible to Vote!")
except NotEligible as e:
    print(e)
    print("Years left to vote:", 18 - age)
