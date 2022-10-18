import requests
import time
import csv

while True:

  response = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")

  datos=response.json()
  
  quote_simpson : str = datos[0]['quote']
  personaje_simpson : str = datos[0]['character']

  print(quote_simpson)
  print(personaje_simpson)

  if personaje_simpson == 'Lisa Simpson':
    my_dict ={"quote":quote_simpson,"character":personaje_simpson}
    with open('lisa.csv', 'a') as csvfile: 
      w = csv.DictWriter(csvfile, my_dict.keys())
      w.writerow(my_dict)
  
  elif personaje_simpson == 'Homer Simpson':
    my_dict ={"quote":quote_simpson,"character":personaje_simpson}
    with open('homer.csv', 'a') as csvfile: 
      w = csv.DictWriter(csvfile, my_dict.keys())
      w.writerow(my_dict)
    
  elif personaje_simpson != 'Lisa Simpson' and personaje_simpson != 'Homer Simpson':
    my_dict ={"quote":quote_simpson,"character":personaje_simpson}
    with open('general.csv', 'a') as csvfile: 
      w = csv.DictWriter(csvfile, my_dict.keys())
      w.writerow(my_dict)
  time.sleep(10)