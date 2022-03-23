#11-1
def city_function(city,country,population=''):
    """storage city and country"""
    if population:
        full_name = city + ', ' + country
        full_name = full_name.title()
        full_name += ' -population ' + str(population)
        print(type(population))
    else:
        full_name = city + ', ' + country
        full_name = full_name.title()
    return full_name

city_function('santiago','country',5000000)
