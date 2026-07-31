strs = ["eat","tea","tan","ate","nat","bat"]

hm = {}

for s in strs:
    ordered_anagram = "".join(sorted(s)) #aet
    if ordered_anagram in hm:
        hm[ordered_anagram].append(s)
    else:
        hm[ordered_anagram] = [s] # aet: [eat, ...]
print( hm.values() )



