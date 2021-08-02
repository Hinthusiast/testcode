
import csv
listoflists=[["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open('filcsv.csv', 'w') as f:
    write=csv.writer(f, delimiter=',')
    for data in listoflists:
        write.writerow(data)
