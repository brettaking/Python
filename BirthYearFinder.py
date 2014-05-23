#Date You Were Born

#Input age and if had Birthday yet
current_age = raw_input("What is your current age? ")
current_age = int(current_age)
has_had_Birthday = raw_input("Have you had your birthday yet this year? ").lower()

#find birth year
import datetime
now = datetime.datetime.now()
current_year = now.year
birth_year = current_year - current_age

if (has_had_Birthday == "yes"):
    print "You were born in %d" % birth_year
elif (has_had_Birthday == "no"):
    print "You were born in %d" % (birth_year - 1)
else:
    print "Please Enter yes or no"
    




