file = []
for line in open('Day5/day5mat.txt', 'r'):
    if line.strip() != '': file.append(line.strip())

headers = [i for i in file if i.count(':') == 1]

seeds = list(map(int, headers[0][headers[0].index(':')+2:].split()))

seedtosoil = file[file.index(headers[1])+1:file.index(headers[2])]
soiltofert = file[file.index(headers[2])+1:file.index(headers[3])]
ferttowatr = file[file.index(headers[3])+1:file.index(headers[4])]
watrtolght = file[file.index(headers[4])+1:file.index(headers[5])]
lghttotemp = file[file.index(headers[5])+1:file.index(headers[6])]
temptohumd = file[file.index(headers[6])+1:file.index(headers[7])]
humdtolctn = file[file.index(headers[7])+1:]

seedtosoil = [list(map(int, i.split())) for i in seedtosoil]
soiltofert = [list(map(int, i.split())) for i in soiltofert]
ferttowatr = [list(map(int, i.split())) for i in ferttowatr]
watrtolght = [list(map(int, i.split())) for i in watrtolght]
lghttotemp = [list(map(int, i.split())) for i in lghttotemp]
temptohumd = [list(map(int, i.split())) for i in temptohumd]
humdtolctn = [list(map(int, i.split())) for i in humdtolctn]

def SrcToDest(mapping, entry):
    for range in mapping:
        if entry < range[1]+range[2] and entry >= range[1]:
            return range[0]-range[1]+entry
    return entry

locations = []
for seed in seeds:
    locations.append(SrcToDest(humdtolctn, SrcToDest(temptohumd, SrcToDest(lghttotemp, SrcToDest(watrtolght, SrcToDest(ferttowatr, SrcToDest(soiltofert, SrcToDest(seedtosoil, seed))))))))

print(locations)
print(min(locations))