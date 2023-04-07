print('start csv read application')

import pandas

df = pandas.readcsv ('pokemon.csv')
print(df('name'))
print(df('total'))

for r,rij in df.iterrows():
    #   print(r)
    #  print(rij)
        print(rij('name'))
