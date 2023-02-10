import read_csv as leer

data = leer.read_csv('./app/data.csv')
# print(data)

country = list(filter(lambda item: item['Country/Territory'] == 'Colombia', data))
print(country)