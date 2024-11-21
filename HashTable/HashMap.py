#Creating hash map
d = {'greg':1,'steve':2,'joe':3}
print(d)

#adding key value in dict - O(1)
d['monicq']=4
print('Added: ',d)

#check take - O(1)
if 'joe' in d:
    print(True)

# check val in map tak - O(1)
print('val check: ',d['joe'])

#Loop over key val takes - O(n)
for key,val in d.items():
    print(f'key {key} : value {val}')




