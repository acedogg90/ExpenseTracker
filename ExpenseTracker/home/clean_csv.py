import csv

input_file_path = 'ExpenseTracker\data\BooksDistributionExpenses.csv'  # Replace with your CSV file path
output_file_path = 'ExpenseTracker\data\BookDistroExpenses2.csv'  # Replace with your desired output file path

with open(input_file_path, 'r', newline='') as infile, open(output_file_path, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        # Strip any empty strings from the end of the row
        clean_row = [value for value in row if value.strip()]
        writer.writerow(clean_row)
