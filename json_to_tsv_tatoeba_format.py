import os
import json
import csv
import pandas as pd

json_filename = "YOUR FILENAME.json"
contents = []

#Open json file and extract sentences
try:
    with open(json_filename,"r", encoding='utf-8') as f:
        contents = json.load(f)
except Exception as e:
    print(e)
sentences = [item.get('jap') for item in contents]

#Generate ids and language strings to follow tatoeba tsv format
ids = np.arange(0,len(sentences))
strings = ["jpn" for i in range(0,len(sentences))]

#Create pandas dataframe to save to tsv
data = pd.DataFrame(
    {'id': ids,
     'language': strings,
     'sentence': sentences
    })

#For sentences with \n characters, replaces them so they do not break lines when writing tsv file
data.sentence = data.sentence.str.replace('\n', "\\n")

#Writes tsv file. To make mine follow the tatoeba format, I called it "jpn_sentences_database".
filename="YOUR FILENAME.tsv"
with open(filename,'w', encoding='utf-8') as write_tsv:
    write_tsv.write(data.to_csv(sep='\t', index=False, header=False, line_terminator=""))

#Removes empty lines from saved file
def remove_empty_lines(filename):
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    with open(filename, encoding='utf-8') as filehandle:
        lines = filehandle.readlines()
    with open(filename, 'w', encoding='utf-8') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines) 

remove_empty_lines(filename)