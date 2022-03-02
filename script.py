content = open('acro.txt', 'r').readlines()

# Setup
acros = {}
currTrack = ''
isOngoingAcro = False
currKey = ''


def getAcronymFull(line: str): return line[line.find(']')+2:-2]

# Iterate Over Acronym Document
for line in content:
    if line.strip().startswith(r'\acro{'):
        currKey = getAcronymFull(line)

    if line.startswith(r'\begin{acronym}'):
        isOngoingAcro = True

    if line.startswith(r'\end{acronym}'):
        isOngoingAcro = False
        currTrack += line
        acros[currKey] = currTrack
        currTrack = ''

    if(isOngoingAcro):
        currTrack += line

acroKeys = sorted([x for x in acros.keys()])

output = open("output.txt", "w")

for key in acroKeys:
    output.write(acros[key])
    output.write('\n')
output.close()
