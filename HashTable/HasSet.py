# creating hash set
s = set()
#print(s)

#Adding item into set - O(1)
s.add(1)
s.add(2)
s.add(3)
#print(s)

#Lookup if item in set will take - O(1)
#if 1 in s :
#    print(True)

#Remove item from set - (1)
s.remove(3)
#print(s)

#set construction -O(s) length of the set string
string = 'aaaaabbbbccccdddddeeeee'
sett = set(string)
#print(sett)

#loop over items in hash set -o(n)
for x in sett:
    print(x)

