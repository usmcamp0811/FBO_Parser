import pandas as pd
import json
import os


def js_writer(fbo_file):
    f = "fs.writeFileSync('fbo_data.json', JSON.stringify(parser.parse(fs.readFileSync('"
    s = "', 'UTF-8'))));"
    file = open('fbo_parser.js', 'w')
    file.write('var fs = require("fs"); \n')
    file.write('var parser = require("./index"); \n')
    file.write(f + fbo_file + s)
    file.close()

def fbo_loader(fbo_json='fbo_data.json'):
    with open(fbo_json) as json_data:
        d = json.load(json_data)

    data = pd.DataFrame()
    for i in range(len(d)):
        data = data.append(pd.DataFrame.from_dict(d[i][0]).T)
    data_cols = list(data.columns)
    data = data.reset_index()
    data_cols.insert(0, 'STATUS')
    data.columns = data_cols
    return data

def fbo_parse(fbo_file):
    js_writer(fbo_file)
    # !node fbo_parser.js #for jupyter notebooks
    os.system('node fbo_parser.js')
    data = fbo_loader()

    return data

if __name__ == "__main__":
    data = fbo_parse('FBOFeed20020129')
    print(data)