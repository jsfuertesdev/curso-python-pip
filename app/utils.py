def get_population(country_dict):
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  # keys = ['col','bol']
  # values = [300,400]
  # return keys, values
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values

def population_by_country(data,country):
  result = list(filter(lambda item:item['Country/Territory']==country,data))
  return result

def countries_in_same_list(data):
  invdata = {}
  # invdata = {v: k for k, v in data.items()}
  invdata = [{k["Country/Territory"]: k["porcentaje"]} for k in data]
  # final_dict = {}
  # for item in invdata:
  #   print(item)
  #   final_dict.update(item)  
  #   print(final_dict)
  # return final_dict
  return invdata

def get_population_percentaje(country_dict):
  population_percent = {
    country_dict['Country/Territory'] : float(country_dict['World Population Percentage'])
  }
  
  labels = population_percent.keys()
  values = population_percent.values()
  return labels, values

def get_values(random_list):
  result = [list(dictionary.values())[0] if dictionary else None for dictionary in random_list]
  return result

# [
#   {
#     'Country':'Colombia',
#     'Population':500
#   },
#   {
#     'Country':'Colombia',
#     'Population':300
#   }
# ]
  