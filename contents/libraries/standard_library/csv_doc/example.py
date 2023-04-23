import csv

with open("example.csv") as csvfile:

   # Read the file as a dictionary for each row ({header : value})
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["name"], row["height"])

    print("\n==\n")

    # Reset o arquivo para o começo, pois o csv.DictReader
    # consome as linhas do arquivo, ou seja, a partir daqui o
    # arquivo não tem mais linhas para serem lidas    
    csvfile.seek(0)

   # Read the file as a list of lists
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
