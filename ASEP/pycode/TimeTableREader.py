import csv
read_data = input("Do you want to read the data from the CSV file? (yes/no): ")
if read_data.lower() == 'yes':
    with open('timeTable.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        print(reader)
        for row in reader:
            
            print(row['FROM'], row['TO'], row['TIMING'])