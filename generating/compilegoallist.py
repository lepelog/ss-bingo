import json
import csv

goallist = [[] for i in range(25)]
with open('goals.csv') as glf:
    goalreader = csv.reader(glf)
    for goal in list(goalreader)[1:]:
        # ignore empty space
        if goal[0].strip() != '':
            difficulty = int(goal[2])
            goal = {'name':goal[0], 'types':goal[1].split(',')}
            goallist[difficulty].append(goal)

# dump the json into a js function for easy import
with open('../tables/bingolists.js','w',encoding='utf8') as bf:
    bf.write('const bingoLists = {normal:')
    json.dump(goallist, bf, ensure_ascii=False, indent=4)
    bf.write('};')

with open('normal.json','w',encoding='utf8') as f:
    json.dump(goallist, f, ensure_ascii=False, indent=4)