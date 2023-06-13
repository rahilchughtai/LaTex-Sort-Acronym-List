acros = [l.strip() for l in open('acro.txt', 'r').readlines() if len(l.strip()) >0  ]
def getAcronymFull(line: str): return line[line.find(']')+2:-1]
acros.sort(key=lambda x:getAcronymFull(x))
output = open("output.txt", "w")
for a in acros:
    output.write(a)
    output.write('\n')
output.close()
