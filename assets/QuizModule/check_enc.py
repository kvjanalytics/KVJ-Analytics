import chardet
path = r'c:\Users\kj anand\Downloads\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data.js'
with open(path, 'rb') as f:
    rawdata = f.read(2000)
    print(chardet.detect(rawdata))
