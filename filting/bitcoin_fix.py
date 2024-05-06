import csv

dic_bit = []

with open('bitcoin_2010-07-27_2024-04-25.csv', mode = 'r') as bitFile:
    datafile = csv.reader(bitFile)
    for lines in datafile:
        dic = {}
        dic['date'] = lines[0]
        dic['open'] = lines[2]
        dic['close'] = lines[3]
        dic['low'] = lines[4]
        dic['high'] = lines[5]
        dic['volume'] = lines[6]
        dic_bit.append(dic)

bitcoin_file = "bitcoin_data.csv"

with open(bitcoin_file, mode = 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(dic_bit)






# df = pd.read_csv("bitcoin_2010-07-27_2024-04-25.csv")
# print(df)

