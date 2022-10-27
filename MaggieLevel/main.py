import requests
import time
import csv

while True:

  response = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes") 

  datos=response.json()
  
  quote : str = datos[0]['quote']
  character : str = datos[0]['character']

  print(quote)
  print(character)

  my_dict ={"quote":quote,"character":character}

  with open('general.csv', 'a') as csvfile: #Todas las frases se guardan en general.csv
      w = csv.DictWriter(csvfile, my_dict.keys())
      w.writerow(my_dict)

  if character == 'Lisa Simpson': #Además, si el personaje es Lisa, se introduce la frase en lisa.csv
    my_dict ={"quote":quote,"character":character}
    with open('lisa.csv', 'a') as csvfile: 
      w = csv.DictWriter(csvfile, my_dict.keys())
      w.writerow(my_dict)
  
  elif character == 'Homer Simpson': #Además, si el personaje es Homer, se introduce la frase en homer.csv
    my_dict ={"quote":quote,"character":character}
    with open('homer.csv', 'a') as csvfile: 
      w = csv.DictWriter(csvfile, my_dict.keys())
      w.writerow(my_dict)
    
  time.sleep(30) #cada 30 segundos se repite el bucle