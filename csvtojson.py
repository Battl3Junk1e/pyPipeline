import pandas

#Takes csv file path as input, returns the csv converted to json
def csv_to_json(csv_file):
    df = pandas.read_csv(csv_file)
    df.to_json("data.json", orient= "records", indent = 4, force_ascii = False)



if __name__ == '__main__':
    csv_to_json("profiles1.csv")