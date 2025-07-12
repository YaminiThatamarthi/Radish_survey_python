import sys
with open("D:/Yamini/NOtepad_notes/radishsurvey.txt",'r') as file:
    data=file.readlines()
    brands=[]
    voters=[]
    for line in data:
        word=line.split(' - ')
        #print(word)
        #brands.append(word[1].strip().lower())
        #voters.append(word[0].strip().lower())
        for1_word=word[0].strip().lower()
        for1_word.replace(" ","")
        voters.append(" ".join(for1_word.split()))
        for_word=word[1].strip().lower()
        for_word.replace(" ","")
        brands.append(" ".join(for_word.split()))
#print(brands)
#print(len(brands))
#print(brands.count(brands[0]))
uniq_brands=set(brands)
#print(uniq_brands)
#print(len(uniq_brands))
brand_count=[]
max_val=0
max_ele=0
min_val=sys.maxsize
min_ele=0
for ele in uniq_brands:
    brand_count.append(brands.count(ele))
    if brands.count(ele)>max_val:
        max_val=brands.count(ele)
        max_ele=ele
    if brands.count(ele)<min_val:
        min_val=brands.count(ele)
        min_ele=ele
#print(len(brand_count))
print(max_ele,":",max_val)
print(min_ele,":",min_val)
#print(voters)
#print(len(voters))
uniq_voters=set(voters)
votes_count=[]
for ele in uniq_voters:
    votes_count.append(voters.count(ele))
    if voters.count(ele)>1:
        print(ele,"voted more than once that is",voters.count(ele))
#print(votes_count)


