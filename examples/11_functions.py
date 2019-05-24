def person_data(name, age, current_year=2019):
    """function doc string, this function return year of birth"""
    born_on = current_year - age
    return "{} born on {}".format(name, born_on)


print(person_data("Abolfazl", 24, 2020))        # name, age and current_year are given
print(person_data("Abolfazl", 23))              # current_year keep it’s default value 2019
print(person_data(age=23, name="Abolfazl"))     # name and age are given as keywords
