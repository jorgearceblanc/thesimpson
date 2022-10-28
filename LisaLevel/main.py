import requests
import time
import csv
import shutil
import string

def count_word(f,contador): #función para contar palabras de cada frase
  counts=contador
  words=f.split() #separar palabras por espacios
  for word in words:
    if word in counts:
      counts[word] += 1 #si la palabra ya está en la lista, suma 1 por cada vez que aparezca
    else:
      counts[word] = 1 #sino, la palabra vale 1
  return counts
contar=dict() #diccionario vacío

while True:

  response = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")  
  quote=response.json()[0]["quote"]
  character=response.json()[0]["character"]
  image=response.json()[0]["image"]
  print(quote)
  print(character)
  url=image
  r=requests.get(image, stream=True)

  simbolos='!”#$%&()*+,-./:;<=>?@[\]^_`{|}~' #todos los símbolos que queremos cambiar por un espacio. (') lo dejamos
  nueva_frase=quote.translate(str.maketrans('', '', simbolos)) #cambiamos los símbolos por espacio
  contar=count_word(nueva_frase,contar) #añade a la suma las nuevas palabras
  
  print(contar) #cuenta de cada palabra
  
  time.sleep(3) #tiempo de espera

  with open('Contador.csv', 'w') as csv_file: #crea archivo Contador, en el cual se cuentan las palabras
    writer = csv.writer(csv_file)
    for key, value in contar.items():
       writer.writerow([key, value]) 

  with open(f'{character}.png', 'wb') as f: #mete la imagen en el archivo creado por (personaje).png
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
    
  data={"quote":quote,"character":character}

  if character == 'Homer Simpson':
    with open('homer.csv', 'a', newline='') as f:
      a=csv.DictWriter(f,data.keys())
      a.writerow(data) 
  elif character == 'Lisa Simpson':
    with open('lisa.csv', 'a', newline='') as g: 
      a=csv.DictWriter(g,data.keys())
      a.writerow(data)
  else:
    with open('general.csv', 'a', newline='') as h: 
      a=csv.DictWriter(h,data.keys())
      a.writerow(data)