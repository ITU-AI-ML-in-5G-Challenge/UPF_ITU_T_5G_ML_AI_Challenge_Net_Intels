import csv 
#The below array 'a' should contain the values of respective data from Throughput/RSSI/SINR
a=[]
with open("Combined_rssi_corrected_proper.csv", 'r') as input, open('Combined_rssi_corrected_proper_sinr.csv', 'w') as output:
    reader = csv.reader(input, delimiter = ',')
    writer = csv.writer(output, delimiter = ',')


    row = next(reader)  # read title line
    row.append("SINR") # name according to data to be appended
    writer.writerow(row)  # write enhanced title line

    it = a.__iter__()  # create an iterator on the result

    for row in reader:
        if row:  # avoid empty lines that usually lurk undetected at the end of the files
            try:
                row.append(next(it))  # add a result to current row
            except StopIteration:
                row.append("N/A")     # not enough results: pad with N/A
            writer.writerow(row)

