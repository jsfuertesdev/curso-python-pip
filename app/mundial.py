import utils
import read_csv
import charts

# data = [
#   {
#     'Country':'Colombia',
#     'Population':500
#   },
#   {
#     'Country':'Bolivia',
#     'Population':300
#   }
# ]

def run():

  data_country = read_csv.read_column('./app/data.csv')
  data_percentaje = read_csv.read_column_2('./app/data.csv')
  # print(data_country)
  print(data_country)
  print(data_percentaje)
  # country = input('Type Country => ')

  # result = utils.countries_in_same_list(data_country)
  # print(result)

  labels = utils.get_values(data_country)
  values = utils.get_values(data_percentaje)

  print(labels)
  print(values)

  if len(labels) > 0 and len(values) > 0:
    charts.generate_pie_chart(labels,values)
  
  # if len(result) > 0 and len(data_percentaje) > 0:
  #   country = result
  #   print(country)
  #   labels,values = utils.get_population_percentaje(country)
  #   print(labels)
  #   print(values)
  #   # print(keys,values)
  #   charts.generate_pie_chart(labels,values)
  
  # print(result)
  # country = input('Type Country => ').lower().title()
  
  # result = utils.population_by_country(data,country)
  # print(result)

    # vector = [
#     {"pais": "country1", "porcentaje": 0.1},
#     {"pais": "country2", "porcentaje": 0.2},
#     {"pais": "country3", "porcentaje": 0.3},
# ]

# vector = [{k["pais"]: k["porcentaje"]} for k in vector]

# print(vector)
# # Output: [{'country1': 0.1}, {'country2': 0.2}, {'country3': 0.3}]

if __name__ == '__main__':
  run()