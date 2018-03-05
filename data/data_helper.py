import csv

FILE_TRAIN = "train.csv"

def toLowerCase(s):
    #Convert a sting to lowercase. E.g., 'BaNaNa' becomes 'banana'

    return s.lower()


def stripNonAlpha(s):
    # Remove non alphabetic characters. E.g. 'B:a,n+a1n$a' becomes 'Banana'
    return ''.join([c for c in s if c.isalpha()] )

def readData(file_path):
    """
    read data
    :param file_path: path
    :return: dict
    """
    csvFile = open(file_path, "r")
    reader = csv.reader(csvFile)
    result = {}
    for item in reader:
        # igonre the first line
        if reader.line_num == 1:
            continue
        #print item: item[0]: id; item[1]: text; item[2:]: label
        text = toLowerCase(item[1])
        text = text.replace("\n","")
        result[text] = [eval(i) for i in item[2:]]
    csvFile.close()
    return result

train_data = readData(FILE_TRAIN)
print train_data.items()[0]