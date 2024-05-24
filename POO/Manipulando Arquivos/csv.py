import csv 

with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["nome", "idade"])
    writer.writerow(["Camila", 29])
    writer.writerow(["Marilia", 31])