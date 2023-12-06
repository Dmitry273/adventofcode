file = []
for line in open('Day5/day5mat.txt', 'r'):
    if line.strip() != '': file.append(line.strip())

headers = [i for i in file if i.count(':') == 1]

seeds = list(map(int, headers[0][headers[0].index(':')+2:].split()))
seeds = [[a, a+b] for a, b in zip(seeds[::2], seeds[1::2])]
seeds.sort(key= lambda x: x[0])

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

seedtosoil = [[i[0]-i[1], [i[1], i[1]+i[2]]] for i in seedtosoil]
soiltofert = [[i[0]-i[1], [i[1], i[1]+i[2]]] for i in soiltofert]
ferttowatr = [[i[0]-i[1], [i[1], i[1]+i[2]]] for i in ferttowatr]
watrtolght = [[i[0]-i[1], [i[1], i[1]+i[2]]] for i in watrtolght]
lghttotemp = [[i[0]-i[1], [i[1], i[1]+i[2]]] for i in lghttotemp]
temptohumd = [[i[0]-i[1], [i[1], i[1]+i[2]]] for i in temptohumd]
humdtolctn = [[i[0]-i[1], [i[1], i[1]+i[2]]] for i in humdtolctn]

def IntInRange(num: int, section: list[int]) -> bool:
    return section[0] <= num and num < section[1]

def SrcToDest(maps, sections):
    breakpoints = []
    for mapp in maps:
        for section in sections:
            if IntInRange(mapp[1][0], section):
                breakpoints.append(mapp[1][0])
            if IntInRange(mapp[1][1], section):
                breakpoints.append(mapp[1][1])

    for point in breakpoints:
        insert_point = [j for j, section in enumerate(sections) if IntInRange(point, section)][0]
        old = sections[insert_point]
        sections.insert(insert_point, [old[0], point])
        sections[insert_point+1] = [point, old[1]]

    for j, section in enumerate(sections):
        shift = 0
        for mapp in maps:
            if IntInRange(section[0], mapp[1]):
                shift = mapp[0]
                break
        sections[j] = [section[0]+shift, section[1]+shift]
        
    return sections

locations = SrcToDest(humdtolctn, SrcToDest(temptohumd, SrcToDest(lghttotemp, SrcToDest(watrtolght, SrcToDest(ferttowatr, SrcToDest(soiltofert, SrcToDest(seedtosoil, seeds)))))))
print(min([min(i) for i in locations]))
