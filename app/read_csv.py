import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    # print(header)
    for row in reader:
      # print('***'*5)
      # print(row)
      iterable = zip(header, row)
      # print(list(iterable))
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
      # print(country_dict)
    return data

def read_column(path):
  with open(path,'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data_country = []
    data_percentaje = []
    # print(header)
    for row in reader:
      # print('***'*5)
      # print(row)
      iterable = zip(header, row)
      # print(list(iterable))
      country_pais = {key: value for key, value in iterable if key == 'Country/Territory'}
      percentaje_pais = {key: value for key, value in iterable if key == 'World Population Percentage'}
      # country_dict = {key: value for key, value in iterable if key == 'World Population Percentage'}
      data_percentaje.append(percentaje_pais)
      data_country.append(country_pais)
      # data.append(country_dict)
      # print(country_dict)
    return data_country

def read_column_2(path):
  with open(path,'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data_country = []
    data_percentaje = []
    # print(header)
    for row in reader:
      # print('***'*5)
      # print(row)
      iterable = zip(header, row)
      # print(list(iterable))
      percentaje_pais = {key: value for key, value in iterable if key == 'World Population Percentage'}
      country_pais = {key: value for key, value in iterable if key == 'Country/Territory'}
      # country_dict = {key: value for key, value in iterable if key == 'World Population Percentage'}
      data_percentaje.append(percentaje_pais)
      data_country.append(country_pais)
      # data.append(country_dict)
      # print(country_dict)
    return data_percentaje

if __name__ == '__main__':
  # data = read_csv('./app/data.csv')
  # print(data)
  
  data = read_column('./app/data.csv')
  print(data)

    