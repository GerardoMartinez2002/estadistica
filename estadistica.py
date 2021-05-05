import pandas as pd
import matplotlib.pyplot as plt
import statistics
import numpy as np
#creamos una variable que contengatodo
df = pd.read_csv('estadisticaC.csv')
velocidad = [10.3, 10.3, 10.2, 16.4, 18.8, 19.7, 15.6, 21.2, 22.6, 19.9, 24.2, 21, 21.4, 21.3, 0, 22.2, 33.8,
                      27.4, 25.7, 24.9, 23.1, 31.7, 36.3, 38.3, 42.6, 55.4, 0, 58.3, 0]
colores = np.array(["Blanco", "Amarillo", "Verde", "Verde", "Verde", "Verde", "Blanco", "Amarillo", "Na", "Blanco",
                  "Amarillo", "Blanco", "Verde", "Verde", "Amarillo", "Amarillo", "Blanco", "Amarillo", "Verde",
                  "Verde", "Amarillo", "Amarillo", "Verde", "Verde", "Verde", "Blanco", "Blanco", "Amarillo", "Verde"])
#peso------------------------------------------------------------------------------------------------
print(df.to_string())
#frecuencias absolutas
print("Frecuencias absolutas Peso")
df_peso = df["peso"].value_counts().to_frame('freq_abs1').rename_axis('peso').reset_index()
print(df_peso)


df_peso.plot(kind='bar',x='peso',y='freq_abs1',color='red')
plt.show()

#frecuencias relativas
print("frecuencias relativas")
df_peso["freq_rel1"] = df_peso["freq_abs1"]/len(df)
print(df_peso)

#pastel
plt.clf()
plt.pie(df_peso["freq_rel1"], labels=df_peso["peso"])
plt.show()



#mediana peso
peso_array = np.array(df_peso["peso"])
mediana_peso = np.median(peso_array)
print("medana de peso: "+ str(mediana_peso))

#media peso
media_peso = np.mean(peso_array)
print("media de peso: "+ str(media_peso))

#moda peso
moda_peso = statistics.mode(df_peso["peso"])
print("moda de peso: "+ str(moda_peso))

#varianza peso
varianza_peso = np.var(peso_array)
print("varianza de peso: "+ str(varianza_peso))

#desviacion estandar peso
des_peso = np.std(peso_array)
print("desviacion de peso: "+ str(des_peso))



#altura-------------------------------------------------------------------------------------------------------------------------------------------------

print("Frecuencias absolutas altura")
# nombre de variable = dataFrame ["de la columna que quieres"].value_counts().to_frame('lo que quieres hacer').rename_axis('de la columpa que quieres').reset_index()
df_altura = df["altura"].value_counts().to_frame('freq_abs2').rename_axis('altura').reset_index()
print(df_altura)

#se grafica
df_altura.plot(kind='bar',x='altura',y='freq_abs2',color='red')
plt.show()

#frecuencias relativas
print("frecuencias relativas de altura")
df_altura["freq_rel2"] = df_altura["freq_abs2"]/len(df)
print(df_altura)

#pastel
plt.clf()
plt.pie(df_altura["freq_rel2"], labels=df_altura["altura"])
plt.show()

# se crean arreglos los cuales se recorren automaticamente para encontrar los valores

#mediana peso
altura_array = np.array(df_altura["altura"])
mediana_altura = np.median(altura_array)
print("medana de la altura: "+ str(mediana_altura))

#media peso
media_altura = np.mean(altura_array)
print("media de la altura: "+ str(media_altura))

#moda peso
moda_altura = statistics.mode(df_altura["altura"])
print("moda de la altura: "+ str(moda_altura))

#varianza peso
varianza_altura = np.var(altura_array)
print("varianza de la altura: "+ str(varianza_altura))

#desviacion estandar peso
des_altura = np.std(altura_array)
print("desviacion de la altura: "+ str(des_altura))


#velocidad --------------------------------------------------------------------------------------------------------------------------------------

velocidad_cont1 = []
velocidad_cont2 = []
#recorremos los arreglos
tam = 1
largo = len(velocidad)
for i in range(1, largo-1):
    if velocidad[i] != velocidad[i-1]:
        velocidad_cont1.append(velocidad[i-1])
        velocidad_cont2.append(tam)
        tam = 1
    else:
        tam = tam+1
velocidad_cont1.append(velocidad[largo-1])
velocidad_cont2.append(tam)
tam = 1
velocidad_cont1.append(velocidad[largo-1])
velocidad_cont2.append(tam)
tam = 1
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(velocidad_cont1, velocidad_cont2)
plt.xlabel("Velocidad")
plt.show()
#plt.clf()
#plt.pie(velocidad[velocidad_cont2], labels=velocidad[velocidad_cont1])
#plt.show()
#pastel
plt.pie(velocidad_cont2, labels=velocidad_cont1)
plt.xlabel("Velocidad")
plt.show()
print("media de la velocidad: "+ str(statistics.mean(velocidad)))
print("moda de la velocidad: "+ str(statistics.median(velocidad)))
print("varianza de la velocidad: "+ str(statistics.variance(velocidad)))
print("desviacion de la velocidad: "+ str(statistics.stdev(velocidad)))

#colores---------------------------------------------------------------------------------------------------------------------
color_col = []
color_col2 = []
tam2 = 1
largo = len(colores)
for i in range(1, largo-1):
    if colores[i] != colores[i-1]:
        color_col.append(colores[i-1])
        color_col2.append(tam2)
        tam2 = 1
    else:
        tam2 = tam2+1
color_col.append(colores[largo-1])
color_col2.append(tam2)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(color_col, color_col2)
plt.xlabel("Colores")
plt.show()
#pastel
plt.pie(color_col2, labels=color_col)
plt.xlabel("Colores")
plt.show()
colorsitos = []
for i in range(1, largo-1):
    b = "Blanco"
    a = "Amarillo"
    v = "Verde"
    n = "Na"
    valor = str(colores[i])
    if(valor == b):
        colorsitos.append(1)
    elif(valor == a):
        colorsitos.append(2)
    elif(valor == v):
        colorsitos.append(3)
    elif(valor == n):
        colorsitos.append(0)

if(int(np.mean(colorsitos)) == 1):
    print("media de colores: Blanco")
if(int(np.mean(colorsitos)) == 2):
    print("media de colores: Amarillo")
if(int(np.mean(colorsitos)) == 3):
    print("media de colores: Verde")

if(int(statistics.median(colorsitos)) == 1):
    print("moda de colores: Blanco")
if(int(statistics.median(colorsitos)) == 2):
    print("moda de colores: Amarillo")
if(int(statistics.median(colorsitos)) == 3):
    print("moda de colores: Verde")

if(int(statistics.variance(colorsitos)) == 1):
    print("varianza de colores: Blanco")
if(int(statistics.variance(colorsitos)) == 2):
    print("varianza de colores: Amarillo")
if(int(statistics.variance(colorsitos)) == 3):
    print("varianza de colores: Verde")

if(int(statistics.stdev(colorsitos)) == 1):
    print("desviacion de colores: Blanco")
if(int(statistics.stdev(colorsitos)) == 2):
    print("desviacion de colores: Amarillo")
if(int(statistics.stdev(colorsitos)) == 3):
    print("desviacion de colores: Verde")
print(colorsitos)


