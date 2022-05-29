num_of_edus = 5
segs = ['']*num_of_edus
with open("doc2.txt.merge") as f:
    lines = f.read().split('\n')
    for line in lines:
        line = line.split('\t')
        segs[int(line[-1])-1] = segs[int(line[-1])-1] + line[2] + ' '

with open("EDUS.txt","w") as file:
    for edu in segs:
        file.write(edu+'\n')