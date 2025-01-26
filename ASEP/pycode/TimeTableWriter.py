import csv

while True:
  FromTo = input("Enter from to : ").split(' TO ')
  Timing = input("Enter timing : ")
  data = [{'FROM': FromTo[0], 'TO': FromTo[1], 'TIMING': Timing}]
  print(data)
  with open('timeTable.csv', 'a', newline='') as csvfile:
      fieldnames = ['FROM', 'TO', 'TIMING']
      writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
      # writer.writeheader()
      writer.writerows(data)
      read_data = input("Do you want to read the data from the CSV file? (yes/no): ")
      if read_data.lower() == 'yes':
          with open('timeTable.csv', 'r') as csvfile:
              reader = csv.DictReader(csvfile)
              for row in reader:
                  print(row)