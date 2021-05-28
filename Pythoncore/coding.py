# find common substring in list of string
def find_long_subs(l1):
    first=l1[0]
    temp=[]
    for i,j in enumerate(first):
        s = ''
        for x in range(i,len(first)):
            s+=first[x]
            for k in range(1,len(l1)):
                if s in l1[k]:
                    if s not in temp:
                        temp.append(s)
                else:
                    if s in temp:
                        temp.remove(s)
                    break
    print(temp)
    max_substr=max(temp,key=len)

    return (max_substr)
if __name__ == "__main__":
    l2 = ["aabcdcadrer", "asjcarer", "qiwqcacaerer","treeecaprer"]
    print(find_long_subs(l2))













