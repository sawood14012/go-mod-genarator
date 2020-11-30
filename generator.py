import json
import random

def select_random10vuls(data):
    list_data = random.sample(data,10)
    #list_data = []
    #for i in range(10):
    #    list_data.append(random.choice(data))
    return list_data

def listToString(s):  
    str1 = ""  
    return (str1.join(s))

def get_package_version(data):
    listt = []
    for i in data:
        length_v = len(i['versions'])
        if length_v == 0:
            version = " "
        else:
            version_index = random.randrange(0, length_v)
            version = i['versions'][version_index]
        PVS = i['package_name'][0] + " " + version + " \n"
        listt.append(PVS)
    return listToString(listt)
    

def modfile_gen(data, file_no):
    filename = "mods/"+str(file_no) + "_go.mod"
    with open(filename, "w") as temp:
        module = "module github.com/fabric8-analytics/fabric8-analytics-common\n"
        version = "go 1.15\n"
        start = "require (\n"
        deps = get_package_version(data)
        end = ")\n"
        temp.write(module)
        temp.write(" \n")
        temp.write(version)
        temp.write(" \n")
        temp.write(start)
        temp.write(deps)
        temp.write(end)
        

    

with open("vuln.json", "r") as f:
    data = json.load(f)
    number_of_vulns = len(data)
    for i in range(38):
        out = select_random10vuls(data)
        filename = "json/" + str(i) + "_mod.json"
        modfile_gen(out, i)
        with open(filename, "w") as temp_writer:
            json.dump(out, temp_writer)
