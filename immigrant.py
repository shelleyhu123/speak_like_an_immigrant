from __future__ import unicode_literals
import sys
import random
import spacy

input_file_name = sys.argv[1]

nlp = spacy.load('en')
text = open(input_file_name, "r").read().decode('utf8', errors="replace")
doc = nlp(text)

space = " "

## below for chapter 1

all_lines = []

for line in open(input_file_name, "r"):
    line = line.strip()
    all_lines.append(line)

# propst = []
# for item in doc:
#     if item.pos_ == 'ADP':
#         propst.append(item.text)

for item in all_lines:
    right_part = space.join(space.join((space.join((space.join(item.split(" the "))).split(" of "))).split(" to ")).split(" for "))[:-5]
    if len(item) < 40:
        print item, space*(40-len(item)), right_part.lower();

    else:
        print item[:40], space*4, right_part.lower()[:20]
        print item[40:] #space*10, right_part.lower()[-20:]

##above ends for chapter 1
##below chapter 2

#random.shuffle(all_lines)
print
for item in all_lines:
    if len(item) < 30:
        print item, space*(38-len(item)), item

random.shuffle(all_lines)
for item in all_lines:
    if len(item) < 30:
        print item, space*(38-len(item)), item


##above chapter 2

## below for chapter 3 left part 

nouns = []
for item in doc:
    if item.pos_ == 'NOUN' or item.pos_ =='PROPN' or item.pos_ == 'PRON':
        nouns.append(item.text)

all_nouns = space.join(nouns)[:80]

#print all_nouns
first = all_nouns[:20]
second = all_nouns[20:40]
third = all_nouns[40:60]
forth = all_nouns[60:]

print 
print first, space*(32-len(first)), all_nouns[:32]
print second, space*(32-len(second)), all_nouns[20:52]
print third, space*(32-len(third)), all_nouns[40:72]
print forth, space*(32-len(forth)), all_nouns[60:92]

## above ends chapter 3 

## below is last part
random.shuffle(nouns)

print 
for item in nouns[:5]:
    print item, space*(25-len(item)), random.choice(all_lines)[:45]

all_lines_alt = []
for line in open(input_file_name, "r"):
    line = line.strip()
    all_lines_alt.append(line)


print
print nouns[5], space*10, all_lines_alt[0] + " " + all_lines_alt[0][:15]
print nouns[5], space*10, all_lines_alt[0][15:] + " " + all_lines_alt[1][:-2]
print nouns[5], space*10, all_lines_alt[1][-2:] + " " + all_lines_alt[2] + " " + all_lines_alt[3]
print nouns[5], space*10, all_lines_alt[4]

## above is last part

