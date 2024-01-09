import pandas as pd
import matplotlib.pyplot as plt


X=5
Y=17

df = pd.read_csv('data.csv')
df.plot(title='Toate valorile')
plt.show()

df.head(X).plot(title=f'primele {X} valori')
plt.show()

df.tail(Y)[['Durata', 'Puls']].plot(title=f'ultimele {Y} valori')
plt.show()